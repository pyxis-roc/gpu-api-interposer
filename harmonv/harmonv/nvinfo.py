#!/usr/bin/env python3
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

