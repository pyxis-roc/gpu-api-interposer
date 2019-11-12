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
import memregions
from harmonv.cuda.constants import *
from harmonv.cuda import devspecs
from cuda_api_objects import *
import logging

_logger = logging.getLogger(__name__)

class CUDAGPU(object):
    """Represents a CUDA GPU"""
    def __init__(self, ordinal):
        self.gpu_ordinal = ordinal
        self.name = None
        self.total_memory = None
        self.attributes = {}
        self.uuid = None
        self.primary_ctx = None
        self.memory_regions = memregions.MemoryRegions()
        self.cc = None

    @property
    def compute_capability(self):
        if self.cc is not None: return self.cc

        major = None
        minor = None

        if CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR in self.attributes:
            major = self.attributes[CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR]

        if CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR in self.attributes:
            minor = self.attributes[CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR]

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

    def init_memory(self, memobj):
        self.mem = memobj

    def alloc_memory_region(self, cumemregion):
        assert cumemregion.dev == self.gpu_ordinal

        if not self.memory_regions.add(memregions.MemoryRegion(cumemregion.dptr,
                                                               cumemregion.dptr + cumemregion.bytesize - 1)):
            _logger.error(f'alloc_memory_region: Failed to alloc memory region {cumemregion.dptr}')
            return False

        if self.mem.mem is None:
            self.mem.alloc_memory()

        self.mem.rebase(cumemregion.dptr)

        return True

    def dealloc_memory_region(self, cumemregion):
        assert cumemregion.dev == self.gpu_ordinal

        self.memory_regions.remove(memregions.MemoryRegion(cumemregion.dptr,
                                                           cumemregion.dptr + cumemregion.bytesize - 1))

        return True

    def set_memory(self, dptr, data):
        self.mem.copy_to(dptr, data)

    def get_memory(self, dptr, bytecount):
        return self.mem.copy_from(dptr, bytecount)

class RebaseableMemory(object):
    """A memory object that can be rebased dynamically, and because it is
       using mmap can also be shared with child processes."""

    def __init__(self, bytesize):
        self.bytesize = bytesize
        self.mem = None
        self.baseaddr = None
        self._highest_write_addr = None

    def alloc_memory(self):
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
