#!/usr/bin/env python3
#
# cuda_remote_devices.py
#
# Python implementations of CUDA Devices (GPU and GPU Memory) that are
# running in a different process. Decouples API handling from the
# actual emulator/simulator. Communication between these processes
# uses a stable API.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester

import mmap
import ctypes
import errno
import memregions
from harmonv.cuda.constants import *
from harmonv.cuda import devspecs
from cuda_api_objects import *
from cuda_devices import *
import logging
import capnp
import os

capnp.remove_import_hook()

rt_to_gpu = capnp.load(os.path.join(os.path.dirname(__file__), 'rt_to_gpu_protocol.capnp'))

_logger = logging.getLogger(__name__)

class NVGPUEmulatorProxy(rt_to_gpu.GPUEmulator.Server):
    def initialize_context(self, context):
        props = {'total_memory': context.params.gpu_props.totalMemory,
                 'gpu_ordinal': context.params.gpu_props.ordinal}

        self.local_impl = NVGPUEmulator(props)

    def loadImage_context(self, context):
        self.local_impl.load_image(context.params.imgId, context.params.image)

    def launchKernel_context(self, context):
        self.local_impl.launch_kernel(context.params.imgId,
                                      context.params.entry,
                                      dim(context.params.gridDimX,
                                          context.params.gridDimY,
                                          context.params.gridDimZ),
                                      dim(context.params.blockDimX,
                                          context.params.blockDimY,
                                          context.params.blockDimZ),
                                      context.params.sharedMemBytes,
                                      context.params.queue,
                                      context.params.kernelParams)

class RebaseableMemoryProxy(rt_to_gpu.RebaseableMemory.Server):
    def __init__(self, local_impl):
        self.local_impl = local_impl

    def initialize_context(self, context):
        #self.local_impl = self.local_impl_class(context.params.byteSize)
        pass

    def allocMemory_context(self, context):
        self.local_impl.alloc_memory()

    def rebase_context(self, context):
        self.local_impl.rebase(context.params.newBase)

    def copyTo_context(self, context):
        self.local_impl.copy_to(context.params.addr, context.params.data)

    def copyFrom(self, addr, byteCount, _context, **kwargs):
        return self.local_impl.copy_from(addr, byteCount)

class RemoteRestorer(rt_to_gpu.GetInterface.Restorer):
    devices = None
    def __init__(self):
        self.devices = {}

    def restore(self, ref_id):
        if ref_id.iface == 'rebaseableMemory':
            assert ref_id.ordinal in self.devices
            return RebaseableMemoryProxy(self.devices[ref_id.ordinal].local_impl.mem)
        elif ref_id.iface == 'gpuEmulator':
            if ref_id.ordinal not in self.devices:
                _logger.info("Creating new GPU Emulator proxy for ordinal {ref_id.ordinal}")
                self.devices[ref_id.ordinal] = NVGPUEmulatorProxy()

            return self.devices[ref_id.ordinal]
        else:
            assert False

class RemoteCUDAGPU(CUDAGPU):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.emu_cls = RemoteNVGPUEmulator

class RemoteNVGPUEmulator(object):
    def __init__(self, gpu_props):
        self.client = capnp.TwoPartyClient('localhost:55555')
        ref = rt_to_gpu.GetInterface.new_message(iface = 'gpuEmulator',
                                                 ordinal = gpu_props['gpu_ordinal'])

        props = rt_to_gpu.GPUProperties.new_message(ordinal = gpu_props['gpu_ordinal'],
                                                    totalMemory = gpu_props['total_memory'])
        self.re = self.client.restore(ref)
        self.re = self.re.cast_as(rt_to_gpu.GPUEmulator)
        self.re.initialize(gpu_props = props).wait()

        self.mem = RemoteRebaseableMemory(gpu_props['total_memory'], gpu_props['gpu_ordinal'])

    def load_image(self, imageId, image):
        self.re.loadImage(imgId = imageId, image=image).wait()

    def launch_kernel(self, imageId, entry, gridDim, blockDim, sharedMemBytes, queue, kernelParams):
        self.re.launchKernel(imgId = imageId, entry=entry,
                              gridDimX = gridDim.x, gridDimY = gridDim.y, gridDimZ = gridDim.z,
                              blockDimX = blockDim.x, blockDimY = blockDim.y, blockDimZ = blockDim.z,
                              sharedMemBytes=sharedMemBytes,
                              queue=0, #TODO
                              kernelParams=kernelParams).wait() #TODO: async

# this is a very thin layer and does not have the same semantics as RebaseableMemory
class RemoteRebaseableMemory(RebaseableMemory):
    def __init__(self, bytesize, ordinal):
        super(RemoteRebaseableMemory, self).__init__(bytesize)
        self.client = capnp.TwoPartyClient('localhost:55555')

        ref = rt_to_gpu.GetInterface.new_message(iface = 'rebaseableMemory', ordinal = ordinal)

        self.rb = self.client.restore(ref)
        self.rb = self.rb.cast_as(rt_to_gpu.RebaseableMemory)
        self.rb.initialize(bytesize).wait()

    def alloc_memory(self):
        self.rb.allocMemory().wait()
        self.mem = bytes()

    def rebase(self, new_base):
        self.rb.rebase(new_base).wait()

    def copy_to(self, addr, data):
        self.rb.copyTo(addr, data)

    def copy_from(self, addr, bytecount):
        res = self.rb.copyFrom(addr, bytecount)
        res = res.wait()
        return res.data
