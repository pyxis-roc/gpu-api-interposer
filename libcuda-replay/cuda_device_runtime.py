#!/usr/bin/env python3
#
# cuda_device_runtime.py
#
# "Implementation" of the CUDA device runtime API, actually just maintains API state.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester

import logging
import memregions
from harmonv.cuda.constants import *
from harmonv.cuda import devspecs
from harmonv import nvfatbin, ptxextract
import mmap
import ctypes

_logger = logging.getLogger(__name__)

class CUDAHandles(object):
    """Generic class to keep track of all handles in the API"""
    def __init__(self, type_):
        self.type_ = type_
        self.handles = {}

    def register(self, handle, obj):
        self.handles[handle] = obj

    def unregister(self, handle):
        del self.handles[handle]

    def __getitem__(self, handle):
        return self.handles[handle]

    def __contains__(self, handle):
        return handle in self.handles

class CUDAContextThreadStack(object):
    def __init__(self):
        self.stack = []

    def push(self, ctx):
        self.stack.append(ctx)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    @property
    def top(self):
        return self.stack[-1]

class CUDAGPU(object):
    """Represents a CUDA GPU"""
    def __init__(self, ordinal):
        self.gpu_ordinal = ordinal
        self.name = None
        self.total_memory = None
        self.attributes = {}
        self.uuid = None
        self.primary_ctx = None
        self.memory_regions = memregions.MemoryRegions()
        self.cc = None

    @property
    def compute_capability(self):
        if self.cc is not None: return self.cc

        major = None
        minor = None

        if CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR in self.attributes:
            major = self.attributes[CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR]

        if CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR in self.attributes:
            minor = self.attributes[CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR]

        if major is None:
            if self.name in devspecs.DEV_SPECS_BY_NAME:
                specs = devspecs.DEV_SPECS_BY_NAME[self.name]

            major = specs.cc_major
            minor = minor if minor is not None else specs.cc_minor


        # add this gpu to devspecs if this assertion fails
        assert major is not None and minor is not None, "Unrecognized GPU {self.name}"

        self.cc = (major, minor)

        return self.cc

    def primary_ctx_retain(self, ctx):

        # The interaction between the Primary Context Management
        # functions and Context Management is really not well
        # specified, especially as used by the CUDA runtime API. In
        # particular, cuCtxSetCurrent comes up with a context without
        # creating one, that is then returned by PrimaryContextRetain
        # as the device context. More work needs to be done.

        if self.primary_ctx is None:
            self.primary_ctx = CUDAContext(ctx)

        self.primary_ctx.usage_count += 1

    def primary_ctx_release(self):
        self.primary_ctx.usage_count -= 1
        if self.primary_ctx.usage_count == 0:
            self.primary_ctx = None

    def has_dptr(self, dptr, dsize = 1):
        r = self.memory_regions.at(dptr)
        if r is not None:
            if (dptr + dsize - 1) > r.end:
                _logger.error(f'Region {dptr:x} to {(dptr+dsize-1):x} is out of bounds [0x{r.start:x},0x{r.end:x}]')

            return True

        return False

    def init_memory(self, memobj):
        self.mem = memobj

    def alloc_memory_region(self, cumemregion):
        assert cumemregion.dev == self.gpu_ordinal

        if not self.memory_regions.add(memregions.MemoryRegion(cumemregion.dptr,
                                                               cumemregion.dptr + cumemregion.bytesize - 1)):
            _logger.error(f'alloc_memory_region: Failed to alloc memory region {cumemregion.dptr}')
            return False

        if self.mem.mem is None:
            self.mem.alloc_memory()

        self.mem.rebase(cumemregion.dptr)

        return True

    def dealloc_memory_region(self, cumemregion):
        assert cumemregion.dev == self.gpu_ordinal

        self.memory_regions.remove(memregions.MemoryRegion(cumemregion.dptr,
                                                           cumemregion.dptr + cumemregion.bytesize - 1))

        return True

    def set_memory(self, dptr, data):
        self.mem.copy(dptr, data)

class CUDAFunction(object):
    """Represents a CUDA Function"""
    def __init__(self, name):
        self.name = name

class CUDAModule(object):
    """Represents a CUDA Module"""
    def __init__(self):
        pass

class CUDAMemoryRegion(object):
    """Represents a CUDA Memory Region"""
    def __init__(self, dev, dptr, bytesize):
        self.dev = dev
        self.dptr = dptr
        self.bytesize = bytesize

class CUDAStream(object):
    """Represents a CUDA Stream"""
    pass

class CUDAContext(object):
    usage_count = 0

    def __init__(self, addr = None):
        self.addr = addr

class RebaseableMemory(object):
    """A memory object that can be rebased dynamically, and because it is
       using mmap can also be shared with child processes."""

    def __init__(self, bytesize):
        self.bytesize = bytesize
        self.mem = None
        self.baseaddr = None
        self._highest_write_addr = None

    def alloc_memory(self):
        self.mem = mmap.mmap(-1, # anonymous
                             self.bytesize)

    def rebase(self, new_base):
        assert self.mem is not None, "Must call alloc_memory before calling rebase"

        if self.baseaddr is None or new_base == self.baseaddr:
            self.baseaddr = new_base
            return

        if new_base > self.baseaddr:
            _logger.debug(f'New base addr 0x{new_base:x} is greater than old: 0x{self.baseaddr:x}, not rebasing.')
            return

        if self._highest_write_addr is None:
            # no data has been written yet, so just rebase
            self.baseaddr = new_base
            return

        #TODO: prevent execution when we're moving data

        move_to = self.baseaddr - new_base
        move_size = self._highest_write_addr - self.baseaddr + 1

        _logger.info(f'Rebasing from {self.baseaddr:x} to {new_base:x}, moving {move_size} bytes to {move_to:x}.')

        self.mem.move(move_to, 0, move_size)
        self.baseaddr = new_base
        self._highest_write_addr += move_to

    def set_highest_write_addr(self, addr):
        if addr > self._highest_write_addr:
            self._highest_write_addr = addr

    def copy(self, addr, data):
        assert addr >= self.baseaddr

        offset = addr - self.baseaddr
        self.mem[offset:offset+len(data)] = data
        self.set_highest_write_addr(addr + len(data) - 1)

class CUDADefaultFactory(object):
    gpu = CUDAGPU
    function = CUDAFunction
    module = CUDAModule
    memory_region = CUDAMemoryRegion
    stream = CUDAStream
    context = CUDAContext
    memory = RebaseableMemory

def check_retval(f):
    def checker(self, *args, **kwargs):
        if self.callee_ctx.retval is not None and self.callee_ctx.retval != 0:
            _logger.warning(f"Function call {f.__name__} failed in trace with error code {self.callee_ctx.retval}, not calling handler")
            return

        return f(self, *args, **kwargs)

    return checker

class CUDADeviceAPIHandler(object):
    """Tracks state across CUDA Device API calls. Called by the TraceHandler."""
    def __init__(self, binary, factory):
        self.binary = binary
        self._factory = factory
        self.gpu_handles = CUDAHandles("CUDevice")
        self.thread_contexts = CUDAHandles("CUcontext")
        self.function_handles = CUDAHandles("CUfunction")
        self.module_handles = CUDAHandles("CUmodule")
        self.memory_handles = CUDAHandles("CUdeviceptr")
        self.stream_handles = CUDAHandles("CUstream")

        self.gpus = []
        self.main_module = self.load_binary(self.binary)

    def load_binary(self, binary):
        fatbin = nvfatbin.NVFatBinary(binary)
        fatbin.parse_fatbin()
        for cc, ptx in ptxextract.extract_ptx(fatbin):
            cc.uncompressed_data = ptx
            # TODO: parse the ptx and extract functions

        return fatbin

    def set_callee_context(self, ctx):
        self.callee_ctx = ctx

    @check_retval
    def cuDriverGetVersion(self, driverVersion):
        _logger.debug(f'Setting driverVersion to {driverVersion}')
        self.driverVersion = driverVersion

    @check_retval
    def cuInit(self, Flags):
        _logger.info(f"cuInit called from thread {self.callee_ctx.thread_id}")

    @check_retval
    def cuDeviceGetCount(self, count):
        self.gpus = [self._factory.gpu(i) for i in range(count)]

    @check_retval
    def cuDeviceGet(self, device, ordinal):
        self.gpu_handles.register(device, self.gpus[ordinal])

    @check_retval
    def cuDeviceGetName(self, name, dev):
        self.gpu_handles[dev].name = name

    @check_retval
    def cuDeviceTotalMem(self, bytes_, dev):
        self.gpu_handles[dev].total_memory = bytes_
        self.gpu_handles[dev].init_memory(self._factory.memory(bytes_))

    @check_retval
    def cuDeviceGetAttribute(self, pi, attrib, dev):
        self.gpu_handles[dev].attributes[attrib] = pi

    @check_retval
    def cuDeviceGetUuid(self, uuid, dev):
        self.gpu_handles[dev].uuid = uuid

    @check_retval
    def cuCtxGetCurrent(self, pctx):
        tid = self.callee_ctx.thread_id
        if tid  not in self.thread_contexts:
            self.thread_contexts.register(tid, CUDAContextThreadStack())

        if pctx == 0:
            assert self.thread_contexts[tid].is_empty(), "Per-thread context stack is not empty, state inconsistent!"
        else:
            assert self.thread_contexts[tid].top.addr == pctx, "State inconsistent"

    @check_retval
    def cuCtxSetCurrent(self, ctx):
        tid = self.callee_ctx.thread_id
        if tid  not in self.thread_contexts:
            self.thread_contexts.register(tid, CUDAContextThreadStack())

        self.thread_contexts[tid].push(CUDAContext(ctx))

    @check_retval
    def cuDevicePrimaryCtxRetain(self, ctx, dev):
        self.gpu_handles[dev].primary_ctx_retain(ctx)

    @check_retval
    def cuDevicePrimaryCtxRelease(self, dev):
        self.gpu_handles[dev].primary_ctx_release()

    @check_retval
    def cuCtxGetDevice(self, dev):
        tid = self.callee_ctx.thread_id
        if tid not in self.thread_contexts:
            self.thread_contexts.register(tid, CUDAContextThreadStack())

        assert not self.thread_contexts[tid].is_empty(), "Stack is empty, inconsistent state"

        self.thread_contexts[tid].top.dev = dev

    def _get_thread_ctx(self):
        # errors here indicate inconsistent state ...
        # not handling right now

        tid = self.callee_ctx.thread_id
        assert tid in self.thread_contexts

        assert not self.thread_contexts[tid].is_empty()
        ctx = self.thread_contexts[tid].top

        return ctx

    @check_retval
    def cuModuleGetFunction(self, hfunc, hmod, name):
        # I'm assuming the current context determines which variant of a function is loaded ...
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        _logger.info(f'cuModuleGetFunction {name} for compute capability {gpu.compute_capability}')

        # this implicit registration is because the CUDA Runtime seems
        # to register modules for the main executable out-of-band.
        if hmod not in self.module_handles:
            self.module_handles.register(hmod, self._factory.module())

        self.function_handles.register(hfunc, self._factory.function(name))

    @check_retval
    def cuMemAlloc(self, dptr, bytesize):
        ctx = self._get_thread_ctx()

        _logger.info(f'cuMemAlloc on device {ctx.dev}: {bytesize} bytes at 0x{dptr:x}')

        # TODO: actually convey to GPU that memory has been allocated
        gpu = self.gpu_handles[ctx.dev]

        mr = self._factory.memory_region(ctx.dev, dptr, bytesize)

        assert gpu.alloc_memory_region(mr) is not None

        self.memory_handles.register(dptr, mr)

    @check_retval
    def cuMemFree(self, dptr):
        mr = self.memory_handles[dptr]

        # TODO: convey to GPU that memory has been freed
        gpu = self.gpu_handles[mr.dev]
        assert gpu.dealloc_memory_region(mr) is not None

        _logger.info(f'cuMemFree on device {mr.dev}: {mr.bytesize} bytes at 0x{mr.dptr:x}')
        self.memory_handles.unregister(dptr)

    @check_retval
    def cuMemcpyHtoD(self, dstDevice, srcHost, ByteCount, _data):
        # TODO: handle multi-GPU correctly
        # i.e. identify gpus from dstDevice pointers

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        assert gpu.has_dptr(dstDevice, ByteCount)
        _logger.info(f'cuMemcpyHtoD on device {ctx.dev}: {ByteCount} bytes to 0x{dstDevice:x} from 0x{srcHost:x}')
        gpu.set_memory(dstDevice, _data)

    @check_retval
    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount):
        # there is really nothing to do here in a trace
        pass

    @check_retval
    def cuLaunchKernel(self, f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams):
        assert f in self.function_handles

        if hStream not in self.stream_handles:
            self.stream_handles.register(hStream, self._factory.stream())

    @check_retval
    def cuModuleUnload(self, hmod):
        # TODO: check _retval
        if hmod in self.module_handles:
            self.module_handles.unregister(hmod)
