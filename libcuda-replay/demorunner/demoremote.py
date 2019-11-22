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
import libcudareplay.cuda_devices

class MyGPUEmulator(libcudareplay.cuda_devices.NVEmulator):
    pass

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Sample remote client")

    p.add_argument('address', help='address:port to listen on', default='localhost:5555')

    args = p.parse_args()

    server = libcudareplay.remote_servers.create_remote_server(args.address, MyGPUEmulator)

    server.run_forever()
