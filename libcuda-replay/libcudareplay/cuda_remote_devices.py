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

_logger = logging.getLogger(__name__)

class CUDARemoteGPU(CUDAGPU):
    pass

class RemoteRebaseableMemory(RebaseableMemory):
    pass

