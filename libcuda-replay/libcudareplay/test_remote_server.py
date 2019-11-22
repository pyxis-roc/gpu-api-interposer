#!/usr/bin/env pypy3

import capnp
from libcudareplay import remote_servers

if __name__ == "__main__":
    restorer = remote_servers.RemoteRestorer()
    server = capnp.TwoPartyServer('localhost:55555', restorer)
    server.run_forever()
