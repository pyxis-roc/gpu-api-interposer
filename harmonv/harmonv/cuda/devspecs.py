#
# devspecs.py
#
# Specifications for CUDA devices that are useful when tracing.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester
#
# SPDX-FileCopyrightText: 2019 University of Rochester
#
# SPDX-License-Identifier: MIT

from collections import namedtuple

CUDADeviceSpec = namedtuple('CUDADeviceSpec', 'name cc_major cc_minor')

QuadroM4000 = CUDADeviceSpec('Quadro M4000', 5, 2)

DEV_SPECS_BY_NAME = {QuadroM4000.name: QuadroM4000}

# from: https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#release-notes
# todo: make this more useful
MIN_CC_FOR_PTX = {(1,0): (1,0),
                  (2,0): (2,0),
                  (2,1): (2,None),  # None -> X
                  (2,2): (2,None),
                  (2,3): (2,None),
                  (3,0): (3,0),
                  (3,1): (3,5),
                  (3,2): (3,5),
                  (4,0): (5,0),   #note: 4.0 also supports sm_32
                  (4,1): (5,2),   #note: 4.1 also supports sm_37
                  (4,2): (5,3),
                  (4,3): (5,3),
                  (5,0): (6,0),  #note: 5.0 also supports 61 and 62
                  (6,0): (7,0),
                  (6,1): (7,2),
                  (6,3): (7,5),
                  (6,4): (7,5)
}

