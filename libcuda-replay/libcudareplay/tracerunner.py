#!/usr/bin/env python3
#
# tracerunner.py
#
# Utility functions to make it easier to construct programs that replay traces using libcuda_replay
#
#
# Author: Sreepathi Pai
#
# Copyright (c) 2019, University of Rochester

import logging
from libcudareplay import libcuda_replay
import configparser
from collections import namedtuple
from libcudareplay.cuda_device_runtime import CUDADeviceAPIHandler, CUDADefaultFactory, CUDARemoteFactory
import os

_logger = logging.getLogger(__name__)

FACTORIES = {'default': CUDADefaultFactory,
             'remote': CUDARemoteFactory}

TraceInfo = namedtuple('TraceInfo', 'name trace trace_dir blobstore binary args_binary args_yaml')

class ReplayConfig(object):
    debug = False
    logformat = '%(name)s: %(levelname)s: %(message)s'
    factory = 'default'

class TraceRunner(object):
    def __init__(self, config):
        self.config = config

    def _load_cfg_trace(self, cfgpath, cfg, section):
        if cfg.has_option(section, 'name'):

            trace_name = cfg.get(section, 'name')
            trace = os.path.join(cfgpath, cfg.get(section, 'trace'))
            trace_dir = libcuda_replay.get_actual_tracedir(trace)
            assert len(trace_dir) == 1, trace_dir # do not support more than one tracedir yet ...
            trace_dir = trace_dir[0]
            blobstore = os.path.join(cfgpath, cfg.get(section, 'blobstore'))
            binary = os.path.join(cfgpath, cfg.get(section, 'binary'))
            args_binary = os.path.join(cfgpath, cfg.get(section, 'args_binary'))
            args_yaml = os.path.join(cfgpath, cfg.get(section, 'args_yaml'))

            ti = TraceInfo(name=trace_name, trace=trace, trace_dir=trace_dir,
                           blobstore=blobstore, binary=binary,
                           args_binary=args_binary, args_yaml=args_yaml)
            _logger.info(f'Loaded trace from {section}: {ti}')
            return ti
        else:
            return None

    def load_trace_from_cfg(self, cfg):
        """Read a trace configuration file"""
        c = configparser.ConfigParser()

        with open(cfg, 'r') as f:
            c.read_file(f)

        cfgpath = os.path.dirname(cfg)
        traces = []
        for s in c.sections():
            if c.has_option(s, 'name'):
                _logger.info(f"Loading trace section {s}")
                t = self._load_cfg_trace(cfgpath, c, s)
                if t is not None:
                    traces.append(t)
                else:
                    _logger.warning(f"Could not load trace configuration from trace section {s}")

        if len(traces) > 1:
            _logger.warning(f"Warning: Multiple trace sections in configuration file not supported. Using first trace")

        self.traces = traces
        self.current_trace = 0 # TODO

    def load_trace(self, name, trace, blobstore, binary, argfile):
        trace_dir = libcuda_replay.get_actual_tracedir(trace)
        assert len(td) == 1, td # do not support more than one tracedir yet ...

        t = TraceInfo(name = name, trace=trace, trace_dir=trace_dir,
                      blobstore=blobstore, binary=binary, argfile=argfile)

        _logger.info(f'Loaded trace: {ti}')

        self.traces = [t]
        self.current_trace = 0

    def configure_logger(self):
        rootLogger = logging.getLogger('')

        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(self.config.logformat))
        rootLogger.addHandler(ch)

        if self.config.debug:
            rootLogger.setLevel(logging.DEBUG)
        else:
            rootLogger.setLevel(logging.INFO)

    def setup_replay(self):
        trace = self.traces[self.current_trace]
        self.replayer = libcuda_replay.Replay(trace.trace_dir, trace.blobstore)

        argh = libcuda_replay.NVArgHandler(trace.args_yaml)
        factory = FACTORIES[self.config.factory]()
        apih = CUDADeviceAPIHandler(trace.binary, factory)

        self.trace_handler = libcuda_replay.NVTraceHandler(argh, apih)

    def replay(self):
        self.replayer.replay(self.trace_handler)
