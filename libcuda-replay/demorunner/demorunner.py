#!/usr/bin/env python3
#
# demorunner.py
#
# Provides a sample of how to load and run a trace
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester
#
# SPDX-FileCopyrightText: 2019,2023 University of Rochester
#
# SPDX-License-Identifier: MIT

import argparse
import libcudareplay
import libcudareplay.cuda_device_runtime
import libcudareplay.tracerunner as tracerunner
import logging
import os
from democommon import MyGPUEmulator

_logger = logging.getLogger(__name__)

class MyAPIInstr(libcudareplay.cuda_device_runtime.CUDADeviceAPIInstr):
    def __init__(self):
        self.instr_fns = set(['cuMemcpyDtoH'])

    def cuMemcpyDtoH(self, dstHost, srcDevice, ByteCount, _data, _gpudata):
        if _gpudata != _data:
            # legitimate reasons exist for data not to match (e.g. floating point data)
            _logger.warning(f'cuMemcpyDtoH: {ByteCount} bytes from 0x{srcDevice:x} did not match original trace!')

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Sample to demonstrate usage of tracerunner")
    p.add_argument("tracecfg", help="trace configuration file")
    p.add_argument("-d", dest="debug", action="store_true", help="Enable debugging mode", default=False)
    p.add_argument("--factory", choices=['default', 'remote'], help="Enable debugging mode", default='default')
    p.add_argument("--remote-cmd", help="Remote command to execute", default='./demoremote.py')
    p.add_argument("--remote-addr", help="Remote address", default='localhost:55555')

    args = p.parse_args()

    cfg = tracerunner.ReplayConfig()
    cfg.debug = args.debug
    cfg.factory = args.factory
    cfg.remote_cmd = args.remote_cmd
    cfg.api_instr = MyAPIInstr()

    if args.factory == 'default':
        cfg.emu_class = MyGPUEmulator

    if args.remote_addr:
        os.environ['REMOTE_EMULATOR_ADDR'] = args.remote_addr

    tr = tracerunner.TraceRunner(cfg)

    tr.load_trace_from_cfg(args.tracecfg)
    tr.configure_logger()
    if tr.setup_replay():
        tr.replay()
