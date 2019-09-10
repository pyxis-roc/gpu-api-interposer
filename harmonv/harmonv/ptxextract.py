#!/usr/bin/env python3

from harmonv import nvfatbin
import struct
import subprocess
import tempfile
import os

def create_fatbin(output, cubin):
    # create a fake fat binary containing only the data
    fatbin_header = struct.Struct('QQ')
    assert fatbin_header.size == 16, fatbin_header.size

    with open(output, "wb") as f:
        f.write(fatbin_header.pack(0x00100001ba55ed50, len(cubin.header) + len(cubin.data)))
        f.write(cubin.header)
        f.write(cubin.data)

def extract_elf_helper(elf, _keep = False):
    if not elf.compressed:
        return elf.data

    h, output = tempfile.mkstemp()
    os.close(h)

    create_fatbin(output, elf)

    curdir = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    p = subprocess.run(["cuobjdump", "-xelf", "all", os.path.join(curdir, output)],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE)

    os.chdir(curdir)
    cuobjdump_output = os.path.join(tmpdir, elf.get_filename())

    data = None
    if p.returncode == 0:
        with open(cuobjdump_output, "rb") as f:
            data = f.read()
            assert len(data) == elf.uncompressed_size, f"Data size mismatch: {len(data)} > {elf.uncompressed_size}"

    if _keep:
        print(tmpdir)
        print(elf.get_filename())
        print(output)
    else:
        os.unlink(output) # remove fatbin
        os.unlink(cuobjdump_output) # remove cuobjdump output
        os.rmdir(tmpdir) # remove tmpdir

    return data

def extract_ptx_helper(ptx, _keep=False):
    if not ptx.compressed:
        return ptx.data

    h, output = tempfile.mkstemp()
    os.close(h)

    create_fatbin(output, ptx)

    # if we're using cuobjdump, why not just use -lptx and -xptx?
    # ... because one day we will write a decompressor ...
    p = subprocess.run(["cuobjdump", "-ptx", output],
                       stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE)

    if _keep:
        print(output)
        os.unlink(output)

    if p.returncode == 0:
        assert len(p.stdout) > ptx.uncompressed_size, p.stdout
        return p.stdout[-ptx.uncompressed_size:]

    return None

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

    p = argparse.ArgumentParser(description="Cleanly extract compressed PTX and ELF files from fat binaries")

    p.add_argument("elffile")
    p.add_argument("-x", "--extract", dest="extract", action="append", choices=["ptx", "elf"],
                   default=[], help="What to extract" )
    p.add_argument("-k", "--keep", dest="keep", action="store_true", help="Keep temporary fatbins")
    p.add_argument("-d", dest="debug", action="store_true")

    args = p.parse_args()

    nvfatbin.DEBUG_MODE = args.debug

    fatbin = nvfatbin.NVFatBinary(args.elffile)
    fatbin.parse_fatbin()

    if len(args.extract) == 0:
        print("Nothing to extract, use -x to specify what to extract (-x ptx or -x elf)")

        for c in fatbin.cubins:
            for cc in c.parts:
                print(cc.get_filename())

        sys.exit(1)

    if "ptx" in args.extract:
        for ptx in extract_ptx(fatbin, args.keep):
            print(ptx[0].get_filename())
            with open(ptx[0].get_filename(), "wb") as f:
                f.write(ptx[1])

    if "elf" in args.extract:
        for elf in extract_elf(fatbin):
            print(elf[0].get_filename())
            with open(elf[0].get_filename(), "wb") as f:
                f.write(elf[1])


