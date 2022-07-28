#!/usr/bin/env python3
#
# cuda_api_objects.py
#
# Python implementations of CUDA API objects
#
# Author: Sreepathi Pai
# Author: Benjamin Valpey
#
# Copyright (C) 2019, University of Rochester

# fmt: off

import logging
from typing import List, Optional
from .cuda_api_constants import *

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

class CUDAContextThreadStack(object):
    def __init__(self):
        self.stack = []

    def push(self, ctx):
        self.stack.append(ctx)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    @property
    def top(self):
        return self.stack[-1]

class CUDAFunction(object):
    """Represents a CUDA Function"""
    def __init__(self, name, elf = None, ptx = None, hmod=None):
        self.name = name
        self.elf = elf # binary image
        self.ptx = ptx # text image
        self.hmod = hmod # module identifier

class CUDAModule(object):
    """Represents a CUDA Module"""
    def __init__(self, cc, elf, ptx, compat_ptx):
        self.cc = cc
        self.elf = elf
        self.ptx = ptx
        self.compat_ptx = compat_ptx

class CUDAMemoryRegion(object):
    """Represents a CUDA Memory Region. This is not an API object per se."""
    def __init__(self, dev, dptr, bytesize):
        self.dev = dev
        self.dptr = dptr
        self.bytesize = bytesize

class CUDAStream(object):
    """Represents a CUDA Stream"""
    def __init__(self):
        # TODO
        self.dev = None
        self.queue = None

class CUDAContext(object):
    usage_count = 0

    def __init__(self, addr = None):
        self.addr = addr

class CUDAChannelFormatDesc(object):
    def __init__(self, x, y, z, w, f):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.w: int = w
        self.f: int = f

class CUDAArray(object):
    def __init__(
        self,
        dev,
        pHandle: int,
        Width: int,
        Height: int,
        Depth: int,
        Format: int,
        NumChannels: int,
        Flags: int,
    ):
        self.pHandle: int = pHandle
        self.dev = dev
        self.Width: int = Width
        self.Height: int = Height
        self.Depth: int = Depth
        self.NumChannels: int = NumChannels
        self.Format: int = Format
        self.Flags: int = Flags

class CUDATexRef(object):
    def __init__(self, dev, hmod, pTexRef, name):
        self.dev = dev
        self.hmod: int = hmod
        self.name: str = name
        self.pTexRef: int = pTexRef

        self.normalized: int = 0
        self.filterMode: int = 0
        self.channelDesc: CUDAChannelFormatDesc = CUDAChannelFormatDesc(0,0,0,0,0)
        self.addressMode: List[int] = [0,0,0]

        self.sRGB: int = 0
        self.maxAnisotropy: int = 0
        self.mipmapFilterMode: int = 0

        # Should we use floats for these? Will python mess with rounding?
        self.mipmapLevelBias: float = 0.0
        self.minMipmapLevelClamp: float = 0.0
        self.maxMipmapLevelClamp: float = 0.0
        
        # Exists in texture_types.h, but not in online documentation.

        self.read_as_integer: int = 0
        self.disableTrilinearOptimization: int = 0

        # Not a part of the api object, but track information we need 

        self.array_address: int = 0
        self.device_address: int = 0
        self.address_byte_offset: int = 0
        self.bound_size: int = 0
        self.bound_type: str = "Not Bound"
        self.bound_flags: int = 0
        self.array_handle: Optional[CUDAArray] = None

    def set_format(self, fmt: int, NumPackedComponents: int):
        if NumPackedComponents not in {1,2,4}:
            raise ValueError("NumPackedComponents must be one of 1, 2, 4")

        self.channelDesc.f = fmt
        num_bytes = CUDA_ARRAY_FORMAT_SIZE_MAP[fmt]

        self.channelDesc.x = num_bytes
        if NumPackedComponents >= 2:
            self.channelDesc.y = num_bytes
        if NumPackedComponents == 4:
            self.channelDesc.z = num_bytes
            self.channelDesc.w = num_bytes

    def set_address(self, ByteOffset: int, dptr: int, bytes: int):
        self.address_byte_offset = ByteOffset
        self.device_address = dptr
        self.bound_size = bytes
        self.bound_type = "dptr"

    def set_array(self, hArray: int, Flags: int, handle: CUDAArray):
        self.array_address = hArray
        self.array_handle = handle
        self.bound_flags = Flags
        self.bound_type = "array"

    def set_addressMode(self, dim: int, am: int):
        self.addressMode[dim] = am

    def set_flags(self, flags: int):
        self.read_as_integer = 1 if (flags & 1) == 1 else 0
        self.normalized = 1 if (flags & 2) == 2 else 0
        self.sRGB = 1 if (flags & 16) == 16 else 0
        self.disableTrilinearOptimization = 1 if (flags & 32) == 32 else 0

    def set_filterMode(self, fm: int):
        self.filterMode = fm

    def set_maxAnisotropy(self, maxAniso: int):
        self.maxAnisotropy = maxAniso

    def set_mipmapLevelBias(self, bias: int):
        self.mipmapLevelBias = bias

    def set_mipmapFilterMode(self, fm: int):
        self.mipmapFilterMode = fm

    def set_mipmapLevelClamp(self, minMipmapLevelClamp: int, maxMipmapLevelClamp: int):
        self.minMipmapLevelClamp = minMipmapLevelClamp
        self.maxMipmapLevelClamp = maxMipmapLevelClamp
