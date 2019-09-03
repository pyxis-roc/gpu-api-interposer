#
# devspecs.py
#
# Specifications for CUDA devices that are useful when tracing.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester

from collections import namedtuple

CUDADeviceSpec = namedtuple('CUDADeviceSpec', 'name cc_major cc_minor')

QuadroM4000 = CUDADeviceSpec('Quadro M4000', 5, 2)

DEV_SPECS_BY_NAME = {QuadroM4000.name: QuadroM4000}
