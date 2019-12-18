#!/usr/bin/env python3
#
# remote_servers.py
#
# Server-side implementations of remote CUDA Devices (GPU and GPU
# Memory) that are running in a different process.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester

from .cuda_devices import *
import logging
import capnp
import os

capnp.remove_import_hook()

rt_to_gpu = capnp.load(os.path.join(os.path.dirname(__file__), 'rt_to_gpu_protocol.capnp'))

_logger = logging.getLogger(__name__)

class NVGPUEmulatorProxy(rt_to_gpu.GPUEmulator.Server):
    emu_cls = NVGPUEmulator

    def initialize_context(self, context):
        props = {'total_memory': context.params.gpu_props.totalMemory,
                 'gpu_ordinal': context.params.gpu_props.ordinal}

        self.local_impl = self.emu_cls(props)

    def loadImage_context(self, context):
        self.local_impl.load_image(context.params.imgId, context.params.image)

    def launchKernel_context(self, context):
        self.local_impl.launch_kernel(context.params.imgId,
                                      context.params.entry.decode('ascii'),
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
        # this is no longer used ...
        pass

    def allocMemory_context(self, context):
        self.local_impl.alloc_memory()

    def rebase_context(self, context):
        self.local_impl.rebase(context.params.newBase)

    def copyTo_context(self, context):
        _logger.debug(f'copyTo {context.params.data} bytes from {context.params.addr:x}')
        self.local_impl.copy_to(context.params.addr, context.params.data)

    def copyFrom(self, addr, byteCount, _context, **kwargs):
        _logger.debug(f'{self.local_impl} copyFrom {byteCount} bytes from {addr:x}')
        data = self.local_impl.copy_from(addr, byteCount)
        return data

class RemoteRestorer(rt_to_gpu.GetInterface.Restorer):
    devices = None

    def __init__(self,
                 gpu_emulator_cls = NVGPUEmulator,
                 gpu_emulator_proxy_cls = NVGPUEmulatorProxy,
                 rebaseable_memory_proxy_cls = RebaseableMemoryProxy):
        self.devices = {}
        self.rmp_cls = rebaseable_memory_proxy_cls
        self.emp_cls = gpu_emulator_proxy_cls
        self.emu_cls = gpu_emulator_cls

    def restore(self, ref_id):
        if ref_id.iface == 'rebaseableMemory':
            assert ref_id.ordinal in self.devices
            return self.rmp_cls(self.devices[ref_id.ordinal].local_impl.mem)
        elif ref_id.iface == 'gpuEmulator':
            if ref_id.ordinal not in self.devices:
                _logger.info(f"Creating new GPU Emulator proxy for ordinal {ref_id.ordinal}")
                self.devices[ref_id.ordinal] = self.emp_cls()
                self.devices[ref_id.ordinal].emu_cls = self.emu_cls
            return self.devices[ref_id.ordinal]
        else:
            assert False

def create_remote_server(address, gpu_emulator_cls = NVGPUEmulator,
                         gpu_emulator_proxy_cls = NVGPUEmulatorProxy,
                         rebaseable_memory_proxy_cls = RebaseableMemoryProxy):
    restorer = RemoteRestorer(gpu_emulator_cls, gpu_emulator_proxy_cls, rebaseable_memory_proxy_cls)
    server = capnp.TwoPartyServer(address, restorer)
    return server
