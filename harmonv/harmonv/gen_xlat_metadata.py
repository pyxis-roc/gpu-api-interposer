#!/usr/bin/env python3
#
# gen_xlat_metadata.py
#
# Extract PTX and its corresponding SASS, along with other translation
# metadata.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2020 University of Rochester

from harmonv import nvfatbin
from harmonv.compression import extract_ptx_helper, extract_elf_helper, DefaultDecompressor
from harmonv.disassembler import DisassemblerCUObjdump
import struct
import subprocess
import tempfile
import os
import yaml
import re

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

def get_function_info(fatbin):
    out = []

    for c in fatbin.cubins:
        # each cubin is for a particular architecture

        ptx_data = []
        elf_data = []

        # each cubin contains parts, for PTX or for ELF
        for cc in c.parts:
            if isinstance(cc, nvfatbin.NVCubinPartPTX):
                ptx_data.append((cc, extract_ptx_helper(cc, _keep_fatbin)))
            elif isinstance(cc, nvfatbin.NVCubinPartELF):
                elf_data.append((cc, extract_elf_helper(cc)))

        # check that both PTX and ELF are present
        if len(ptx_data) and len(elf_data):
            ocubin = {'cubin': 'cubin', # TODO
                      'ptx': [{'data': pd[1].decode('ascii')} for pd in ptx_data], #TODO
                      }

            function_info = []

            for elfcubin, rawelf in elf_data:
                disfns = DisassemblerCUObjdump.disassemble(elfcubin)
                for fn, sassfn in disfns.items():
                    function_info.append(sassfn)
                    #print(yaml.dump(sassfn.to_dict()))

            ocubin['functions'] = function_info
            out.append(ocubin)
        else:
            if len(elf_data) and not len(ptx_data):
                print("WARNING: ELF data present, but no PTX data found")
            elif len(ptx_data) and not len(elf_data):
                print("WARNING: PTX data present, but no ELF/Binary data found")
            else:
                # this is common, not sure why
                pass


    return out

if __name__ == "__main__":
    import sys
    import argparse

    p = argparse.ArgumentParser(description="Extract PTX and corresponding SASS translations")

    p.add_argument("elffile", help="Fat binary to extract translations from")
    p.add_argument("output", help="Output YAML file")
    p.add_argument("-d", dest="debug", help="Debug", action="store_true")
    p.add_argument("--only", dest="only_re", action="append", help="Regular expressions to include functions", default=[])
    p.add_argument("--except", dest="except_re", action="append", help="Regular expressions to exclude functions", default=[])

    args = p.parse_args()

    nvfatbin.DEBUG_MODE = args.debug

    _keep_fatbin = False

    fatbin = nvfatbin.NVFatBinary(args.elffile, decompressor=DefaultDecompressor)
    fatbin.parse_fatbin()
    function_info = get_function_info(fatbin)

    only_re = re.compile("|".join(args.only_re))
    except_re = re.compile("|".join(args.except_re))

    for cubin in function_info:
        if args.only_re:
            cubin['functions'] = [x for x in cubin['functions'] if only_re.search(x.function)]

        if args.except_re:
            cubin['functions'] = [x for x in cubin['functions'] if not except_re.search(x.function)]

        cubin['functions'] = [x.to_dict() for x in cubin['functions']]

    with open(args.output, 'w') as f:
        print(yaml.dump(function_info), file=f)
