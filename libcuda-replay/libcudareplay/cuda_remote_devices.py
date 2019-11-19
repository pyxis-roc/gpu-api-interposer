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

from cuda_devices import *
import logging
import capnp
import os

capnp.remove_import_hook()

rt_to_gpu = capnp.load(os.path.join(os.path.dirname(__file__), 'rt_to_gpu_protocol.capnp'))

_logger = logging.getLogger(__name__)


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

class RemoteCUDAGPU(CUDAGPU):
    emu_cls = RemoteNVGPUEmulator

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
