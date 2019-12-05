#!/usr/bin/env python3
#
# cuda_devices.py
#
# Python implementations of CUDA Devices (GPU and GPU Memory)
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester

import mmap
import ctypes
import errno
from . import memregions
from harmonv.cuda.constants import *
from harmonv.cuda import devspecs
from .cuda_api_objects import *
import logging
from collections import namedtuple
import itertools

_logger = logging.getLogger(__name__)

dim = namedtuple('dim', 'x y z')

class NVGPUEmulator(object):
    """An emulator for an NVIDIA GPU device. This interface is kept as
       stateless as possible so it can be in a remote process"""

    def __init__(self, gpu_props):
        _logger.debug('Initializing NVGPUEmulator')
        self.images = {}
        self.mem = RebaseableMemory(gpu_props['total_memory'])

    def load_image(self, imageId, image):
        self.images[imageId] = image

    def launch_kernel(self, imageId, entry, gridDim, blockDim, sharedMemBytes, queue, kernelParams):
        paramTxt = ", ".join([f"{p}" for p in kernelParams])
        _logger.info(f'Running {entry}<<<{gridDim}, {blockDim}, {sharedMemBytes}, {queue}>>>({paramTxt})')

class CUDAGPU(object):
    """Represents a CUDA GPU"""
    def __init__(self, ordinal, emu_cls = NVGPUEmulator):
        self.gpu_ordinal = ordinal
        self._name = None
        self._total_memory = None
        self._attributes = {}
        self._uuid = None
        self.primary_ctx = None
        self.memory_regions = memregions.MemoryRegions()
        self.cc = None

        # represents an emulator and its memory
        self.emu_cls = emu_cls
        self.emu = None
        self.mem = None
        self._emu_inited = False
        self._img_id = 0

    def _lazy_emu_init(self):

        #TODO: it should be possible to do a non-lazy init, by scanning the trace or reading a configuration file, etc.
        # right now, we lazy init whenever an actual action needs to be performed on the GPU (mem allocs/transfers, launches)

        if self._emu_inited:
            return

        assert self.total_memory is not None
        assert self.mem is None

        # TODO: add more properties needed for emulation here ...
        props = {'total_memory': self.total_memory,
                 'max_shared_memory_per_mp': self.get_attribute(CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_MULTIPROCESSOR),
                 'gpu_ordinal': self.gpu_ordinal}

        self.emu = self.emu_cls(props)
        self.mem = self.emu.mem

        if self.mem.mem is None:
            self.mem.alloc_memory()

        self._emu_inited = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def total_memory(self):
        return self._total_memory

    @total_memory.setter
    def total_memory(self, size_in_bytes):
        self._total_memory = size_in_bytes

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        self._uuid = uuid

    def set_attribute(self, attribute, value):
        self._attributes[attribute] = value

    def get_attribute(self, attribute):
        return self._attributes[attribute]

    @property
    def compute_capability(self):
        if self.cc is not None: return self.cc

        major = None
        minor = None

        if CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR in self._attributes:
            major = self._attributes[CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR]

        if CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR in self._attributes:
            minor = self._attributes[CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR]

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

    def alloc_memory_region(self, cumemregion):
        self._lazy_emu_init()

        assert cumemregion.dev == self.gpu_ordinal

        if not self.memory_regions.add(memregions.MemoryRegion(cumemregion.dptr,
                                                               cumemregion.dptr + cumemregion.bytesize - 1)):
            _logger.error(f'alloc_memory_region: Failed to alloc memory region {cumemregion.dptr}')
            return False

        self.mem.rebase(cumemregion.dptr)

        return True

    def dealloc_memory_region(self, cumemregion):
        self._lazy_emu_init()

        assert cumemregion.dev == self.gpu_ordinal

        self.memory_regions.remove(memregions.MemoryRegion(cumemregion.dptr,
                                                           cumemregion.dptr + cumemregion.bytesize - 1))

        return True

    def set_memory(self, dptr, data):
        self._lazy_emu_init()
        _logger.debug(f'set_memory: {len(data)} bytes at 0x{dptr:x}')
        self.mem.copy_to(dptr, data)

    def get_memory(self, dptr, bytecount):
        self._lazy_emu_init()
        _logger.debug(f'get_memory: {bytecount} bytes from 0x{dptr:x}')
        return self.mem.copy_from(dptr, bytecount)

    def register_module(self, module):
        self._lazy_emu_init()

        for e in module.elf:
            self.emu.load_image(id(e), e.get_data())

        for p in itertools.chain(module.ptx, module.compat_ptx):
            self.emu.load_image(id(p), p.get_data())

    def launch_kernel(self, f, gridDim, blockDim, sharedMemBytes, stream, kernelParams):
        def _pp_dim(d):
            if d.z != 1 or d.y != 1:
                return f"({d.x}, {d.y}, {d.z})"
            else:
                return f"{d.x}"

        def _pp_param(p):
            return hex(int.from_bytes(p, 'little', signed=False))

        self._lazy_emu_init()

        # TODO: handle stream
        paramTxt = ", ".join([f"{_pp_param(p)}" for p in kernelParams])
        _logger.info(f'{self.name}({self.gpu_ordinal}): Launching {f.name}<<<{_pp_dim(gridDim)}, {_pp_dim(blockDim)}, {sharedMemBytes}>>>({paramTxt})')

        #TODO dispatch it to gpu device
        #TODO ultimately change executable format?
        self.emu.launch_kernel(id(f.ptx), f.name, gridDim, blockDim, sharedMemBytes, stream.queue, kernelParams)

class RebaseableMemory(object):
    """A memory object that can be rebased dynamically, and because it is
       using mmap can also be shared with child processes."""

    def __init__(self, bytesize):
        self.bytesize = bytesize
        self.mem = None
        self.baseaddr = None
        self._highest_write_addr = None

    def alloc_memory(self):
        assert self.mem is None

        alloc_size = self.bytesize
        while True:
            try:
                self.mem = mmap.mmap(-1, # anonymous
                                     alloc_size)
                break
            except OSError as e:
                if e.errno == errno.ENOMEM:
                    _logger.error(f'Failed to allocate memory of size {alloc_size} for GPU memory, trying again with smaller size')
                    alloc_size = alloc_size // 2
                else:
                    raise

        if alloc_size != self.bytesize:
            _logger.warning(f"mmap allocation size {alloc_size} for GPU memory is less than {self.bytesize}. This may cause errors.")

        self.alloc_size = self.bytesize

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
        if self._highest_write_addr is None or addr > self._highest_write_addr:
            self._highest_write_addr = addr

    def copy_to(self, addr, data):
        assert addr >= self.baseaddr

        offset = addr - self.baseaddr
        self.mem[offset:offset+len(data)] = data
        self.set_highest_write_addr(addr + len(data) - 1)

    def copy_from(self, addr, bytecount):
        assert addr >= self.baseaddr

        offset = addr - self.baseaddr
        return self.mem[offset:offset+bytecount]

    def set_memory(self, addr, data):
        assert addr >= self.baseaddr
        offset = addr - self.baseaddr
        _logger.debug(f'Setting {len(data)} bytes at 0x{addr:x} (actually {offset:x})')
        self.mem[offset:offset+len(data)] = data
        self.set_highest_write_addr(addr + len(data) - 1)

    def get_memory(self, addr, bytecount):
        assert addr >= self.baseaddr
        offset = addr - self.baseaddr
        _logger.debug(f'Reading {bytecount} bytes from 0x{addr:x} (actually {offset:x})')                
        return self.mem[offset:offset+bytecount]
        
