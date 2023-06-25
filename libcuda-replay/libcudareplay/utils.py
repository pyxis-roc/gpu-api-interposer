#
# utils.py
#
# Common utility functions and datastructures
#
# Author: Sreepathi Pai
#
# Copyright (c) 2019, University of Rochester
#
# SPDX-FileCopyrightText: 2019 University of Rochester
#
# SPDX-License-Identifier: MIT
class ReplayConfig(object):
    debug = False
    logformat = '%(name)s: %(levelname)s: %(message)s'
    factory = 'default'
    remote_cmd = None
    api_instr = None
    emu_class = None    # must be set only if factory is 'default'
