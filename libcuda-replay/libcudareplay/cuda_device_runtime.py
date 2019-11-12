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

from harmonv import nvfatbin, compression
from cuda_api_objects import *
from cuda_devices import *
from cuda_remote_devices import *

_logger = logging.getLogger(__name__)

class CUDADefaultFactory(object):
    gpu = CUDAGPU
    function = CUDAFunction
    module = CUDAModule
    memory_region = CUDAMemoryRegion
    stream = CUDAStream
    context = CUDAContext

class CUDARemoteFactory(object):
    gpu = CUDARemoteGPU
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
        fatbin = nvfatbin.NVFatBinary(binary, compression.DecompressorCuobjdump)
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
        self.gpu_handles[dev].init_memory()

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
            module = self.main_module
        else:
            _logger.info(f'cuModuleGetFunction {name} on {hmod:x}, but module not found!')
            assert False

        # need to separate this out to a loader ...
        arch_exact = []
        arch_relevant = []
        arch = gpu.compute_capability[0]*10+gpu.compute_capability[1]

        for c in module.cubins:
            for cc in c.parts:
                if cc.arch != arch and cc.type == nvfatbin.CUBIN_ELF:
                    _logger.info(f'Skipping over ELF for arch {cc.arch} (need {arch})')
                    continue

                if cc.arch == arch:
                    _logger.info(f'Found exact match for arch {arch} (type {cc.type})')
                    arch_exact.append(cc)
                    continue

                if cc.arch != arch and cc.type == nvfatbin.CUBIN_PTX:
                    _logger.info(f'Found PTX for arch {cc.arch}')
                    arch_relevant.append(cc)

        assert len(arch_exact) > 0 or len(arch_relevant) > 0, "Unable to find ELF suitable for arch {cc}, or any PTX at all"

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
    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount, _data):
        # this function really has no meaning in a trace, however we
        # simply implement a byte-wise comparison with the _data
        # recorded at runtime

        ctx = self._get_thread_ctx()
        gpu = self.gpu_handles[ctx.dev]

        assert gpu.has_dptr(srcDevice, ByteCount)
        _logger.info(f'cuMemcpyDtoH on device {ctx.dev}: {ByteCount} bytes from device 0x{srcDevice:x} to host 0x{dstHost:x}')

        if gpu.get_memory(srcDevice, ByteCount) != _data:
            # legitimate reasons exist for data not to match (e.g. floating point data)
            _logger.warning(f'cuMemcpyDtoH on device {ctx.dev}: {ByteCount} bytes from 0x{srcDevice:x} did not match original trace!')

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
