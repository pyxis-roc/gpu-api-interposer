#!/usr/bin/env pypy3

# SPDX-FileCopyrightText: 2019 University of Rochester
# SPDX-FileCopyrightText: 2019,2023 University of Rochester
#
# SPDX-License-Identifier: MIT

import capnp
from libcudareplay import remote_servers

if __name__ == "__main__":
    restorer = remote_servers.RemoteRestorer()
    server = capnp.TwoPartyServer('localhost:55555', restorer)
    server.run_forever()
