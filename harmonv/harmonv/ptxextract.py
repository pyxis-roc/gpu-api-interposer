#!/usr/bin/env python3

import argparse
from . import nvfatbin
import struct
import subprocess
import tempfile
import os

def extract_ptx_helper(ptx):
    if not ptx.compressed:
        return ptx.data

    # create a fake fat binary containing only the ptx
    # and use cuobjdump to decompress it
    #
    fatbin_header = struct.Struct('QQ')
    assert fatbin_header.size == 16, fatbin_header.size

    h, output = tempfile.mkstemp()
    os.close(h)

    with open(output, "wb") as f:
        f.write(fatbin_header.pack(0x00100001ba55ed50, len(ptx.header) + len(ptx.data)))
        f.write(ptx.header)
        f.write(ptx.data)

    # if we're using cuobjdump, why not just use -lptx and -xptx?
    # ... because one day we will write a decompressor ...
    p = subprocess.run(["cuobjdump", "-ptx", output],
                       stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE)

    os.unlink(output)

    if p.returncode == 0:
        assert len(p.stdout) > ptx.uncompressed_size, p.stdout
        return p.stdout[-ptx.uncompressed_size:]

    return None

def extract_ptx(fatbin):
    ptx_data = []
    for c in fatbin.cubins:
        for cc in c.parts:
            if isinstance(cc, nvfatbin.NVCubinPartPTX):
                ptx_data.append((cc, extract_ptx_helper(cc)))

    return ptx_data

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Cleanly extract PTX files from fat binaries")

    p.add_argument("elffile")
    p.add_argument("-d", dest="debug", action="store_true")

    args = p.parse_args()

    nvfatbin.DEBUG_MODE = args.debug

    fatbin = nvfatbin.NVFatBinary(args.elffile)
    fatbin.parse_fatbin()

    for ptx in extract_ptx(fatbin):
        print(ptx)
