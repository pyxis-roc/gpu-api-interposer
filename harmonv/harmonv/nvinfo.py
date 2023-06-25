#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2020,2021 University of Rochester
#
# SPDX-License-Identifier: MIT

#
# Constants for the nvinfo sections
#
from collections import namedtuple

ATTR_INFO = namedtuple('ATTR_INFO', 'attr_fmt attr_size data')

EIATTR_KPARAM_INFO = 0x1704
EIATTR_REGCOUNT = 0x2f04
EIATTR_MAXREG_COUNT = 0x1b03
EIATTR_CBANK_PARAM_SIZE = 0x1903
EIATTR_PARAM_CBANK = 0x0a04
EIATTR_CUDA_API_VERSION = 0x3704
EIATTR_SW2393858_WAR = 0x3001
EIATTR_INT_WARP_WIDE_INSTR_OFFSETS = 0x3104 # data is an array of offset words with length prefix?
EIATTR_SW_WAR = 0x3604 # data is word
EIATTR_LD_CACHEMOD_INSTR_OFFSETS = 0x2504 # data is array of words
EIATTR_INDIRECT_BRANCH_TARGETS = 0x3404 # data is array of word, shortx2, word, word
EIATTR_SW2861232_WAR = 0x3501
EIATTR_MIN_STACK_SIZE = 0x1204
EIATTR_MAX_STACK_SIZE = 0x2304
EIATTR_FRAME_SIZE = 0x1104
EIATTR_BINDLESS_TEXTURE_BANK = 0x1502
EIATTR_MAX_THREADS = 0x504
EIATTR_EXPLICIT_CACHING = 0x2101 # -dlcm=ca
