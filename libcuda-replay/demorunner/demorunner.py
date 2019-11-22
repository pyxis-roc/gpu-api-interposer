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

import argparse
import libcudareplay
import libcudareplay.tracerunner as tracerunner

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Sample to demonstrate usage of tracerunner")
    p.add_argument("tracecfg", help="trace configuration file")
    p.add_argument("-d", dest="debug", action="store_true", help="Enable debugging mode", default=False)
    p.add_argument("--factory", choices=['default', 'remote'], help="Enable debugging mode")
    args = p.parse_args()

    cfg = tracerunner.ReplayConfig()
    cfg.debug = args.debug

    tr = tracerunner.TraceRunner(cfg)

    tr.load_trace_from_cfg(args.tracecfg)
    tr.configure_logger()
    tr.setup_replay()
    tr.replay()

