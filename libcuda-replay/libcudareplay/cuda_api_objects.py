#!/usr/bin/env python3
#
# cuda_api_objects.py
#
# Python implementations of CUDA API objects
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
    def __init__(self, name, elf = None, ptx = None):
        self.name = name
        self.elf = elf # binary image
        self.ptx = ptx # text image

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

