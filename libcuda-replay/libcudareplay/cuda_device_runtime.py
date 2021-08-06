#!/usr/bin/env python3
#
# cuda_device_runtime.py
#
# "Implementation" of the CUDA device runtime API, actually just maintains API state.
#
# Author: Sreepathi Pai
# Author: Amr Elhelw
#
# Copyright (C) 2019, University of Rochester

import logging

from harmonv import nvfatbin, compression, loader
from .cuda_api_objects import *
from .cuda_devices import *
from .cuda_remote_devices import *
import itertools

_logger = logging.getLogger(__name__)

class CUDADefaultFactory(object):
    gpu = CUDAGPU
    function = CUDAFunction
    module = CUDAModule
    memory_region = CUDAMemoryRegion
    stream = CUDAStream
    context = CUDAContext

class CUDARemoteFactory(object):
    gpu = RemoteCUDAGPU
    function = CUDAFunction
    module = CUDAModule
    memory_region = CUDAMemoryRegion
    stream = CUDAStream
    context = CUDAContext

def check_retval(f):
    def checker(self, *args, **kwargs):
        if self.callee_ctx.retval is not None and self.callee_ctx.retval != 0:
            _logger.warning(f"Function call {f.__name__} failed in trace with error code {self.callee_ctx.retval}, not calling handler")
            return

        return f(self, *args, **kwargs)

    return checker

class CUDADeviceAPIInstr(object):
    # set of API functions that should be instrumented
    instr_fns = None

    def __init__(self):
        self.instr_fns = set()

    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount, _data, _gpudata):
        pass

class CUDADeviceAPIHandler(object):
    """Tracks state across CUDA Device API calls. Called by the TraceHandler."""
    def __init__(self, binary, factory, config = None):
        self.binary = binary
        self._factory = factory
        self.gpu_handles = CUDAHandles("CUDevice")
        self.thread_contexts = CUDAHandles("CUcontext")
        self.function_handles = CUDAHandles("CUfunction")
        self.module_handles = CUDAHandles("CUmodule")
        self.memory_handles = CUDAHandles("CUdeviceptr")
        self.stream_handles = CUDAHandles("CUstream")
        self.config = config

        if self.config and self.config.api_instr:
            self.api_instr = self.config.api_instr
        else:
            self.api_instr = CUDADeviceAPIInstr()

        self.gpu_kwargs = {}
        if self.config and self.config.emu_class:
            self.gpu_kwargs['emu_cls'] = self.config.emu_class

        self.gpus = []
        self.main_module = self.load_binary(self.binary)

    def load_binary(self, binary):
        fatbin = nvfatbin.NVFatBinary(binary, compression.DefaultDecompressor)
        fatbin.parse_fatbin()

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
        self.gpus = [self._factory.gpu(i, **self.gpu_kwargs) for i in range(count)]

    @check_retval
    def cuDeviceGet(self, device, ordinal):
        self.gpu_handles.register(device, self.gpus[ordinal])

    @check_retval
    def cuDeviceGetName(self, name, dev):
        self.gpu_handles[dev].name = name

    @check_retval
    def cuDeviceTotalMem(self, bytes_, dev):
        self.gpu_handles[dev].total_memory = bytes_

    @check_retval
    def cuDeviceGetAttribute(self, pi, attrib, dev):
        # this is not a typo, we're recording the values returned by the trace
        self.gpu_handles[dev].set_attribute(attrib, pi)

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

    def _load_module(self, gpu, module):
        elf = loader.extract_elf(module, gpu.cc)
        ptx, compat_ptx = loader.extract_ptx(module, gpu.cc)
        for m in itertools.chain(elf, ptx, compat_ptx):
            m.parse()

        mod = self._factory.module(gpu.cc, elf, ptx, compat_ptx)
        gpu.register_module(mod)
        return mod

    @check_retval
    def cuModuleGetFunction(self, hfunc, hmod, name):
        # I'm assuming the current context determines which variant of a function is loaded ...
        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        _logger.info(f'cuModuleGetFunction {name} for compute capability {gpu.compute_capability}')

        # this implicit registration is because the CUDA Runtime seems
        # to register modules for the main executable out-of-band.
        if hmod not in self.module_handles:
            # module handles are per context,
            # each context contains one gpu device
            self.module_handles.register(hmod, self._load_module(gpu,
                                                                 self.main_module))

        module = self.module_handles[hmod]

        assert len(module.elf) > 0 or len(module.ptx) > 0 or len(module.compat_ptx) > 0, "Unable to find ELF suitable for arch {cc}, or any PTX at all"

        elf = None
        ptx = None
        for m in module.elf:
            for g in m.get_globals():
                if g.name == name:
                    elf = m
                    break

        nb = name.encode('ascii')
        for m in itertools.chain(module.ptx, module.compat_ptx):
            a = m.get_data()
            #print(a)
            if nb in a:
                #TODO: need to parse ptx to get globals...
                ptx = m
                break

        _logger.info(f"Using ELF:{elf} and PTX:{ptx} for {name}")
        assert not (elf is None and ptx is None), "Unable to find ELF/PTX containing function {name}"

        self.function_handles.register(hfunc, self._factory.function(name, elf, ptx))

    @check_retval
    def cuMemAlloc(self, dptr, bytesize):
        ctx = self._get_thread_ctx()

        _logger.info(f'cuMemAlloc on device {ctx.dev}: {bytesize} bytes at 0x{dptr:x}')

        # TODO: actually convey to GPU that memory has been allocated
        gpu = self.gpu_handles[ctx.dev]

        mr = self._factory.memory_region(ctx.dev, dptr, bytesize)

        assert gpu.alloc_memory_region(mr) is not None

        self.memory_handles.register(dptr, mr)

        if 'cuMemAlloc' in self.api_instr.instr_fns:
            self.api_instr.cuMemAlloc(dptr, bytesize)

    @check_retval
    def cuMemFree(self, dptr):
        mr = self.memory_handles[dptr]

        # TODO: convey to GPU that memory has been freed
        gpu = self.gpu_handles[mr.dev]
        assert gpu.dealloc_memory_region(mr) is not None

        _logger.info(f'cuMemFree on device {mr.dev}: {mr.bytesize} bytes at 0x{mr.dptr:x}')
        self.memory_handles.unregister(dptr)
        if 'cuMemFree' in self.api_instr.instr_fns:
            self.api_instr.cuMemFree(dptr)

    @check_retval
    def cuMemcpyHtoD(self, dstDevice, srcHost, ByteCount, _data):
        # TODO: handle multi-GPU correctly
        # i.e. identify gpus from dstDevice pointers

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        assert gpu.has_dptr(dstDevice, ByteCount)
        #_logger.info(f'cuMemcpyHtoD on device {ctx.dev}: {ByteCount} bytes to 0x{dstDevice:x} from 0x{srcHost:x}')
        gpu.set_memory(dstDevice, _data)
        if 'cuMemcpyHtoD' in self.api_instr.instr_fns:
            self.api_instr.cuMemcpyHtoD(dstDevice, srcHost, ByteCount, _data)

    @check_retval
    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount, _data):
        # this function really has no meaning in a trace, however we
        # simply implement a byte-wise comparison with the _data
        # recorded at runtime

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        assert gpu.has_dptr(srcDevice, ByteCount)
        _logger.info(f'cuMemcpyDtoH on device {ctx.dev}: {ByteCount} bytes from device 0x{srcDevice:x} to host 0x{dstHost:x}')

        if 'cuMemcpyDtoH' in self.api_instr.instr_fns:
            # TODO: should we send gpu object?
            self.api_instr.cuMemcpyDtoH(dstHost, srcDevice, ByteCount, _data,
                                        gpu.get_memory(srcDevice, ByteCount))

    @check_retval
    def cuLaunchKernel(self, f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams):
        assert f in self.function_handles

        if hStream not in self.stream_handles:
            self.stream_handles.register(hStream, self._factory.stream())

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        gpu.launch_kernel(self.function_handles[f],
                          dim(gridDimX, gridDimY, gridDimZ),
                          dim(blockDimX, blockDimY, blockDimZ),
                          sharedMemBytes,
                          self.stream_handles[hStream],
                          kernelParams)

        if 'cuLaunchKernel' in self.api_instr.instr_fns:
            self.api_instr.cuLaunchKernel(self.function_handles[f].name, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, self.stream_handles[hStream], kernelParams)

    @check_retval
    def cuModuleUnload(self, hmod):
        # TODO: check _retval
        if hmod in self.module_handles:
            self.module_handles.unregister(hmod)
