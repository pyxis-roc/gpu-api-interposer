#!/usr/bin/env python3
#
# compression.py
#
# Routines for handling NVIDIA's compressed PTX and ELF cubins
#
# Currently, uses cuobjdump (which must be in path) for decompression.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, University of Rochester

from harmonv import nvfatbin
import struct
import subprocess
import tempfile
import os

# if we're using cuobjdump, why not just use -lptx and -xptx?
# ... because one day we will write a decompressor ...

class DecompressorCuobjdump(object):
    @staticmethod
    def create_fatbin(output, cubin):
        # create a fat binary containing only the data
        fatbin_header = struct.Struct('QQ')
        assert fatbin_header.size == 16, fatbin_header.size

        with open(output, "wb") as f:
            f.write(fatbin_header.pack(0x00100001ba55ed50, len(cubin.header) + len(cubin.data)))
            f.write(cubin.header)
            f.write(cubin.data)

    @staticmethod
    def decompress_ptx(ptx, fatbin, _keep = False):
        # assumes fatbin contains only one PTX

        p = subprocess.run(["cuobjdump", "-ptx", fatbin],
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE)

        if p.returncode == 0:
            assert len(p.stdout) > ptx.uncompressed_size, f"Data size mismatch: header size {ptx.uncompressed_size} >= output size {len(p.stdout)}"
            return p.stdout[-ptx.uncompressed_size:]

        return None

    @staticmethod
    def decompress_elf(elf, fatbin, _keep = False):
        curdir = os.getcwd()
        tmpdir = tempfile.mkdtemp()
        os.chdir(tmpdir)

        fatbin = os.path.join(curdir, fatbin)

        p = subprocess.run(["cuobjdump", "-xelf", "all", fatbin],
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE)

        os.chdir(curdir)

        cuobjdump_output = os.path.join(tmpdir, elf.get_filename())

        data = None
        if p.returncode == 0:
            with open(cuobjdump_output, "rb") as f:
                data = f.read()
                assert len(data) == elf.uncompressed_size, f"Data size mismatch: {len(data)} != {elf.uncompressed_size}"

        if _keep:
            print(cuobjdump_output)
            print(tmpdir)
        else:
            os.unlink(cuobjdump_output) # remove cuobjdump output
            os.rmdir(tmpdir)            # remove tmpdir

        return data

    @staticmethod
    def decompress(cubin, _keep = False):
        if not cubin.compressed:
            return cubin.data

        h, output = tempfile.mkstemp()
        os.close(h)

        DecompressorCuobjdump.create_fatbin(output, cubin)

        if cubin.type == nvfatbin.CUBIN_PTX:
            data = DecompressorCuobjdump.decompress_ptx(cubin, output, _keep)
        elif cubin.type == nvfatbin.CUBIN_ELF:
            data = DecompressorCuobjdump.decompress_elf(cubin, output, _keep)

        if _keep:
            print(output)
        else:
            os.unlink(output)

        return data

def extract_elf_helper(elf, _keep = False):
    return DecompressorCuobjdump.decompress(elf, _keep)

def extract_ptx_helper(ptx, _keep=False):
    return DecompressorCuobjdump.decompress(ptx, _keep)

