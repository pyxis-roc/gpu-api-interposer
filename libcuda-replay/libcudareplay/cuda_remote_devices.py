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

class CUDARemoteGPU(CUDAGPU):
    def init_memory(self):
        assert self.total_memory is not None
        assert self.mem is None
        self.mem = RemoteRebaseableMemory(self.total_memory)

class RebaseableMemoryImpl(rt_to_gpu.RebaseableMemory.Server):
    def __init__(self, local_impl_class):
        self.local_impl_class = local_impl_class

    def initialize_context(self, context):
        self.local_impl = self.local_impl_class(context.params.byteSize)

    def allocMemory_context(self, context):
        self.local_impl.alloc_memory()

    def rebase_context(self, context):
        self.local_impl.rebase(context.params.newBase)

    def copyTo_context(self, context):
        self.local_impl.copy_to(context.params.addr, context.params.data)

    def copyFrom(self, addr, byteCount, _context, **kwargs):
        return self.local_impl.copy_from(addr, byteCount)

class RemoteRestorer(rt_to_gpu.GetInterface.Restorer):
    def restore(self, ref_id):
        if ref_id.iface == 'rebaseableMemory':
            return RebaseableMemoryImpl(RebaseableMemory)
        else:
            assert False

# this is a very thin layer and does not have the same semantics as RebaseableMemory
class RemoteRebaseableMemory(RebaseableMemory):
    def __init__(self, bytesize):
        super(RemoteRebaseableMemory, self).__init__(bytesize)
        self.client = capnp.TwoPartyClient('localhost:55555')

        ref = rt_to_gpu.GetInterface.new_message(iface = 'rebaseableMemory')

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
