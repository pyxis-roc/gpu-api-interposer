#!/usr/bin/env python3
#
# cuda_device_runtime.py
#
# "Implementation" of the CUDA device runtime API, actually just maintains API state.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester

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

class CUDAGPU(object):
    """Represents a CUDA GPU"""
    def __init__(self, ordinal):
        self.gpu_ordinal = ordinal
        self.name = None
        self.total_memory = None
        self.attributes = {}
        self.uuid = None

    def primary_ctx_retain(self, ctx):
        pass

    def primary_ctx_release(self):
        pass

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

class CUDADefaultFactory(object):
    gpu = CUDAGPU
    function = CUDAFunction
    module = CUDAModule
    memory_region = CUDAMemoryRegion
    stream = CUDAStream

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

    def cuDriverGetVersion(self, driverVersion):
        self.driverVersion = driverVersion

    def cuInit(self, Flags):
        pass

    def cuDeviceGetCount(self, count):
        self.gpus = [self._factory.gpu(i) for i in range(count)]

    def cuDeviceGet(self, device, ordinal):
        self.gpu_handles.register(device, self.gpus[ordinal])

    def cuDeviceGetName(self, name, dev):
        self.gpu_handles[dev].name = name

    def cuDeviceTotalMem(self, bytes_, dev):
        self.gpu_handles[dev].total_memory = bytes_

    def cuDeviceGetAttribute(self, pi, attrib, dev):
        self.gpu_handles[dev].attributes[attrib] = pi

    def cuDeviceGetUuid(self, uuid, dev):
        self.gpu_handles[dev].uuid = uuid

    # need a cleaner way to handle _tid?
    def cuCtxGetCurrent(self, pctx, _tid):
        self.thread_contexts.register(_tid, pctx)

    def cuCtxSetCurrent(self, ctx, _tid):
        self.thread_contexts.register(_tid, ctx)

    def cuDevicePrimaryCtxRetain(self, ctx, dev):
        self.gpu_handles[dev].primary_ctx_retain(ctx)

    def cuDevicePrimaryCtxRelease(self, dev):
        self.gpu_handles[dev].primary_ctx_release()

    def cuCtxGetDevice(self, dev):
        pass

    def cuModuleGetFunction(self, hfunc, hmod, name):
        if hmod not in self.module_handles:
            self.module_handles.register(hmod, self._factory.module())

        self.function_handles.register(hfunc, self._factory.function(name))

    def cuMemAlloc(self, dptr, bytesize):
        self.memory_handles.register(dptr, self._factory.memory_region(bytesize))

    def cuMemFree(self, dptr):
        self.memory_handles.unregister(dptr)

    def cuMemcpyHtoD(self, dstDevice, srcHost, ByteCount, _data, _tid):
        # use _tid to find thread context?
        # use thread context to find current device
        # then copy to that device?
        # can dstDevice pointer identify GPU in multidevice contexts?

        pass

    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount):
        # there is really nothing to do here in a trace
        pass

    def cuLaunchKernel(self, f, gridDimX, gridDimY, gridDimZ, blockDimX, blockDimY, blockDimZ, sharedMemBytes, hStream, kernelParams):
        assert f in self.function_handles

        if hStream not in self.stream_handles:
            self.stream_handles.register(hStream, self._factory.stream())

    def cuModuleUnload(self, hmod):
        # TODO: check _retval
        if hmod in self.module_handles:
            self.module_handles.unregister(hmod)
