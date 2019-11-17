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

class RemoteCUDAGPU(CUDAGPU):
    def __init__(self, ordinal):
        super().__init__(ordinal)

        self.client = capnp.TwoPartyClient('localhost:55555')

        ref = rt_to_gpu.GetInterface.new_message(iface = 'cudaGPU', ordinal = ordinal)

        self.rg = self.client.restore(ref)
        self.rg = self.rg.cast_as(rt_to_gpu.CUDAGPU)

    def init_memory(self):
        assert self.total_memory is not None
        assert self.mem is None
        self.rg.initMemory().wait()
        self.mem = RemoteRebaseableMemory(self.total_memory, self.gpu_ordinal)

    @property
    def name(self):
        return super().name

    @name.setter
    def name(self, name):
        super(RemoteCUDAGPU, RemoteCUDAGPU).name.fset(self, name)
        self.rg.setName(name).wait()

    @property
    def total_memory(self):
        return super().total_memory

    @total_memory.setter
    def total_memory(self, size_in_bytes):
        super(RemoteCUDAGPU, RemoteCUDAGPU).total_memory.fset(self, size_in_bytes)
        self.rg.setTotalMemory(size_in_bytes).wait()

    @property
    def uuid(self):
        return super().uuid

    @uuid.setter
    def uuid(self, uuid):
        super(RemoteCUDAGPU, RemoteCUDAGPU).uuid.fset(self, uuid)
        self.rg.setUuid(uuid).wait()

    def set_attribute(self, attribute, value):
        super().set_attribute(attribute, value)
        self.rg.setAttribute(attribute, value).wait()

# essentially, proxy
class CUDAGPUProxy(rt_to_gpu.CUDAGPU.Server):
    def __init__(self, local_impl):
        self.local_impl = local_impl

    def initMemory_context(self, context):
        self.local_impl.init_memory()

    def initialize_context(self, context):
        self.local_impl = self.local_impl_class(context.params.ordinal)

    def setName_context(self, context):
        self.local_impl.name = context.params.name

    def setTotalMemory_context(self, context):
        self.local_impl.total_memory = context.params.sizeInBytes

    def setAttribute_context(self, context):
        self.local_impl.set_attribute(context.params.attribute, context.params.value)

    def setUuid_context(self, context):
        self.local_impl.uuid = context.params.uuid

    def launchKernel_context(self, context):
        self.local_impl.launch_kernel(context.params.f,
                                      dim(context.params.gridDimX,
                                          context.params.gridDimY,
                                          context.params.gridDimZ),
                                      dim(context.params.blockDimX,
                                          context.params.blockDimY,
                                          context.params.blockDimZ),
                                      context.params.sharedMemBytes,
                                      context.params.stream,
                                      context.params.kernelParams)

# essentially, proxies
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
        elif ref_id.iface == 'cudaGPU':
            if ref_id.ordinal not in self.devices:
                _logger.info("Creating new GPU proxy for ordinal {ref_id.ordinal}")
                self.devices[ref_id.ordinal] = CUDAGPUProxy(CUDAGPU(ref_id.ordinal))

            return self.devices[ref_id.ordinal]
        else:
            assert False

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
