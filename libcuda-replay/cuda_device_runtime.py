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

class CUDAPrimaryContext(object):
    usage_count = 0

class CUDAGPU(object):
    """Represents a CUDA GPU"""
    def __init__(self, ordinal):
        self.gpu_ordinal = ordinal
        self.name = None
        self.total_memory = None
        self.attributes = {}
        self.uuid = None
        self.primary_ctx = None

    def primary_ctx_retain(self, ctx):
        if self.primary_ctx is None:
            self.primary_ctx = CUDAPrimaryContext()

        self.primary_ctx.usage_count += 1

    def primary_ctx_release(self):
        self.primary_ctx.usage_count -= 1
        if self.primary_ctx.usage_count == 0:
            self.primary_ctx = None


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
    def __init__(self, bytesize):
        self.bytesize = bytesize

class CUDAStream(object):
    """Represents a CUDA Stream"""
    pass

class CUDAContext(object):
    pass

class CUDADefaultFactory(object):
    gpu = CUDAGPU
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
    def __init__(self, factory):
        self._factory = factory
        self.gpu_handles = CUDAHandles("CUDevice")
        self.thread_contexts = CUDAHandles("CUcontext")
        self.function_handles = CUDAHandles("CUfunction")
        self.module_handles = CUDAHandles("CUmodule")
        self.memory_handles = CUDAHandles("CUdeviceptr")
        self.stream_handles = CUDAHandles("CUstream")

        self.gpus = []

    def set_callee_context(self, ctx):
        self.callee_ctx = ctx

    @check_retval
    def cuDriverGetVersion(self, driverVersion):
        _logger.debug(f'Setting driverVersion to {driverVersion}')
        self.driverVersion = driverVersion

    @check_retval
    def cuInit(self, Flags):
        print(f"cuInit called from {self.callee_ctx.thread_id}")

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

    @check_retval
    def cuDeviceGetAttribute(self, pi, attrib, dev):
        self.gpu_handles[dev].attributes[attrib] = pi

    @check_retval
    def cuDeviceGetUuid(self, uuid, dev):
        self.gpu_handles[dev].uuid = uuid

    @check_retval
    def cuCtxGetCurrent(self, pctx):
        self.thread_contexts.register(self.callee_ctx.thread_id, pctx)

    @check_retval
    def cuCtxSetCurrent(self, ctx):
        self.thread_contexts.register(self.callee_ctx.thread_id, ctx)

    @check_retval
    def cuDevicePrimaryCtxRetain(self, ctx, dev):
        self.gpu_handles[dev].primary_ctx_retain(ctx)

    @check_retval
    def cuDevicePrimaryCtxRelease(self, dev):
        self.gpu_handles[dev].primary_ctx_release()

    @check_retval
    def cuCtxGetDevice(self, dev):
        pass

    @check_retval
    def cuModuleGetFunction(self, hfunc, hmod, name):
        if hmod not in self.module_handles:
            self.module_handles.register(hmod, self._factory.module())

        self.function_handles.register(hfunc, self._factory.function(name))

    @check_retval
    def cuMemAlloc(self, dptr, bytesize):
        self.memory_handles.register(dptr, self._factory.memory_region(bytesize))

    @check_retval
    def cuMemFree(self, dptr):
        self.memory_handles.unregister(dptr)

    @check_retval
    def cuMemcpyHtoD(self, dstDevice, srcHost, ByteCount, _data):
        # use _tid to find thread context?
        # use thread context to find current device
        # then copy to that device?
        # can dstDevice pointer identify GPU in multidevice contexts?

        pass

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
