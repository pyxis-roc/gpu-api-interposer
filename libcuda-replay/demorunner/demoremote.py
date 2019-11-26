#!/usr/bin/env python3
#
# demoremote.py
#
# Provides a sample of how to create remote client
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester
#

import argparse
import libcudareplay.remote_servers
import logging
import sys
from democommon import MyGPUEmulator
import os

_logger = logging.getLogger()
logformat = 'remote %(name)s: %(levelname)s: %(message)s'

def setup_logging(debug = False):
    rootLogger = logging.getLogger('')

    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(logformat))
    rootLogger.addHandler(ch)

    if debug:
        rootLogger.setLevel(logging.DEBUG)
    else:
        rootLogger.setLevel(logging.INFO)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Sample remote client")

    p.add_argument('-d', '--debug', action='store_true', help='Enable debugging')

    args = p.parse_args()

    if 'REMOTE_EMULATOR_ADDR' in os.environ:
        addr = os.environ['REMOTE_EMULATOR_ADDR']
    else:
        _logger.error('No address to listen. Specify one using environment variable REMOTE_EMULATOR_ADDR')
        sys.exit(1)

    setup_logging(args.debug)
    _logger.info(f'Listening on {addr}. Press CTRL+\ to quit')
    server = libcudareplay.remote_servers.create_remote_server(addr, MyGPUEmulator)
    print("EMULATOR READY", file=sys.stdout)
    sys.stdout.flush()
    server.run_forever()
