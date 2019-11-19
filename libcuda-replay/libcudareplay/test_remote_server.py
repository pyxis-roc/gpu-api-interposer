#!/usr/bin/env pypy3

import capnp
import cuda_remote_devices

if __name__ == "__main__":
    restorer = cuda_remote_devices.RemoteRestorer()
    server = capnp.TwoPartyServer('localhost:55555', restorer)
    server.run_forever()
