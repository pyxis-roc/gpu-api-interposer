#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 University of Rochester
#
# SPDX-License-Identifier: MIT

from harmonv import nvfatbin
from harmonv.compression import extract_ptx_helper, extract_elf_helper
import struct
import subprocess
import tempfile
import os
from pathlib import Path

def extract_ptx(fatbin, _keep_fatbin = False):
    ptx_data = []
    for c in fatbin.cubins:
        for cc in c.parts:
            if isinstance(cc, nvfatbin.NVCubinPartPTX):
                ptx_data.append((cc, extract_ptx_helper(cc, _keep_fatbin)))

    return ptx_data

def extract_elf(fatbin):
    elf_data = []
    for c in fatbin.cubins:
        for cc in c.parts:
            if isinstance(cc, nvfatbin.NVCubinPartELF):
                elf_data.append((cc, extract_elf_helper(cc)))

    return elf_data

if __name__ == "__main__":
    import sys
    import argparse

    p = argparse.ArgumentParser(description="Cleanly extract compressed PTX and ELF cubins from fat binaries")

    p.add_argument("elffile")
    p.add_argument("-x", "--extract", dest="extract", action="append", choices=["ptx", "elf"],
                   default=[], help="What to extract" )
    p.add_argument("-k", "--keep", dest="keep", action="store_true", help="Keep temporary files")
    p.add_argument("-d", dest="debug", help="Debug", action="store_true")
    p.add_argument("-p", dest="file_prefix", help="Filename prefix")
    p.add_argument("-s", dest="stem", help="Stem for extracted files, default is cuobjdump-style stemming (upto last .)")
    p.add_argument("-r", dest="rel", action="store_true", help="Use __nv_relfatbin to extract from instead of .nv_fatbin")

    args = p.parse_args()

    if args.stem:
        stem_fn = lambda x: args.stem.encode('utf-8')
    else:
        stem_fn = None

    nvfatbin.DEBUG_MODE = args.debug

    fatbin = nvfatbin.NVFatBinary(args.elffile)
    fatbin.parse_fatbin(nvfatbin.NVFATBIN_SECTION_NAME if not args.rel else nvfatbin.NVFATBIN_REL_SECTION_NAME)

    if len(args.extract) == 0:
        print("Nothing to extract, use -x to specify what to extract (-x ptx or -x elf)")

        for c in fatbin.cubins:
            for cc in c.parts:
                print(cc.get_filename(stem_fn=stem_fn))

        sys.exit(1)

    if "ptx" in args.extract:
        for ptx in extract_ptx(fatbin, args.keep):
            fn = Path(ptx[0].get_filename(stem_fn=stem_fn))
            if args.file_prefix:
                fn = fn.parent / (args.file_prefix + fn.name)
            print(fn)
            with open(fn, "wb") as f:
                if ptx[1][-1] == 0:
                    # CUDA versions >= 11.0 store a 0 byte at the end
                    f.write(ptx[1][:-1])
                else:
                    f.write(ptx[1])

    if "elf" in args.extract:
        for elf in extract_elf(fatbin):
            fn = Path(elf[0].get_filename(stem_fn=stem_fn))
            if args.file_prefix:
                fn.name = fn.parent / (args.file_prefix + fn.name)

            print(fn)
            with open(fn, "wb") as f:
                f.write(elf[1])
