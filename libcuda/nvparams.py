#!/usr/bin/env python3

import argparse
from elftools.elf.elffile import ELFFile
import elftools
import sys
import io
import struct
from collections import namedtuple
import os

KPARAM = namedtuple('KPARAM', 'ordinal offset size')
GLOBALINFO = namedtuple('GLOBALINFO', 'name info size value')

class NVCubin(object):
    def __init__(self, cubin_data):
        self.cubin_data = cubin_data
        # possibly this is multiple files ELF + ELF, or ELF + PTX, etc.

    def parse_symtab(self, elf):
        # TODO: note that fatbin checks for sh_type == SHT_SYMTAB
        symtab = elf.get_section_by_name(".symtab")
        global_syms = []
        if symtab:
            for sym in symtab.iter_symbols():
                n = sym.name
                if sym.entry['st_info']['bind'] == 'STB_GLOBAL':
                    gi = GLOBALINFO(name=n,
                                    info=sym.entry['st_info'],
                                    size=sym.entry['st_size'],
                                    value=sym.entry['st_value'])

                    global_syms.append(gi)

        return global_syms

    def parse_nv_param_info_section(self, s, data):
        ndx = 0
        section_size = len(data)
        args = []
        #print(s.name)
        while(ndx < section_size):
            attr_fmt = struct.unpack_from('H', data, ndx)[0]
            attr_size = struct.unpack_from('H', data, ndx + 2)[0]
            #print(f"{attr_fmt:x} {attr_size}")
            ndx += 4

            # possibly use construct?

            if attr_fmt == 0x1704: # EIATTR_KPARAM_INFO, EIFMT_SVAL
                ordinal = struct.unpack_from('H', data, ndx + 4)[0]
                offset = struct.unpack_from('H', data, ndx + 6)[0]
                size = struct.unpack_from('H', data, ndx + 10)[0] >> 2

                args.append(KPARAM(ordinal = ordinal, offset=offset, size=size))
                #print(f"\t{ordinal} {offset} {size}")

                ndx += attr_size
            elif attr_fmt == 0xa04:   # EIATTR_PARAM_CBANK, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x0d04:  # EIATTR_SYNC_STACK, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x204:   # EIATTR_IMAGE_SLOT, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x1903:  # EIATTR_CBANK_PARAM_SIZE, EIFMT_HVAL
                pass
            elif attr_fmt == 0x2304  : #EIATTR_MAX_STACK_SIZE
                ndx += attr_size
            elif attr_fmt == 0x1204  : #EIATTR_MIN_STACK_SIZE_
                ndx += attr_size
            elif attr_fmt == 0x1104  : #EIATTR_FRAME_SIZE
                ndx += attr_size
            elif attr_fmt == 0x1b03 : #EIATTR_MAXREG_COUNT
                pass
            elif attr_fmt == 0x1c04 : #EIATTR_EXIT_INSTR_OFFSETS
                ndx += attr_size
            elif attr_fmt == 0x1e04 : #EIATTR_CRS_STACK_SIZE
                ndx += attr_size
            elif attr_fmt == 0x504 : #EIATTR_MAX_THREADS
                ndx += attr_size
            elif attr_fmt == 0x1d04 : #EIATTR_S2RCTAID_INSTR_OFFSETS
                ndx += attr_size
            elif attr_fmt == 0xf04 : #EIATTR_EXTERNS
                ndx += attr_size
            elif attr_fmt == 0x1f01 : # EIATTR_NEED_CNP_WRAPPER
                ndx += attr_size
            elif attr_fmt == 0x2001 : #EIATTR_NEED_CNP_PATCH
                ndx += attr_size
            elif attr_fmt == 0x401 : # EIATTR_CTAIDZ_USED
                ndx += attr_size
            elif attr_fmt == 0x2a01: #EIATTR_SW1850030_WAR
                ndx += attr_size
            else:
                print(f"unrecognized {attr_fmt:x} {attr_size}")
                ndx += attr_size

        return args

    def parse_cubin(self):
        self.cubin_elf = ELFFile(io.BytesIO(self.cubin_data))
        # # see Nervana's maxas cubin file for more details on properties
        arch = self.cubin_elf.header['e_flags'] & 0xFF
        print(f'elf: arch={arch}')

        gs = self.parse_symtab(self.cubin_elf)

        for s in self.cubin_elf.iter_sections():
            #print(s.name)
            if s.name[:8] == ".nv.info":
                args = self.parse_nv_param_info_section(s, s.data())
                print(s.name)
                print(args)

        print(gs)

class NVFatBinary(object):
    def __init__(self, elf):
        self.elf = elf
        self.felf = open(elf, "rb")

    def parse_fatbin(self):
        # TODO: some cubins apparently start with PTX, skip, see fatbin.cc

        self.elffile = ELFFile(self.felf)

        if self.elffile.elfclass != 64:
            #print("ERROR: Only 64-bit binaries supported", file=sys.stderr)
            return 0

        nv_fatbin = self.elffile.get_section_by_name('.nv_fatbin')

        elfname = os.path.basename(self.elf)

        if nv_fatbin:
            self.fatbin_data = nv_fatbin.data()

            with open(f"/tmp/fatbin_complete_{elfname}", "wb") as f:
                f.write(self.fatbin_data)

            cubins = []
            ndx = 0
            while ndx < len(self.fatbin_data):
                header = self.fatbin_data[ndx:ndx+0x50]

                next_offset = struct.unpack_from('Q', header, 8)[0]
                arch = struct.unpack_from('H', header, 0x2c)[0]
                code_version_1 = struct.unpack_from('H', header, 0x28)[0]
                code_version_2 = struct.unpack_from('H', header, 0x2a)[0]

                # producer, platform, 64bit?

                print(f"arch: sm_{arch}")
                print(f"version: [{code_version_1, code_version_2}]")
                print(f"offset: {next_offset}")
                print("")

                cubin_data = self.fatbin_data[ndx+0x50:(ndx + 16 + next_offset)]
                cubins.append(NVCubin(cubin_data))

                with open(f"/tmp/fatbin_cubin_{len(cubins):02d}_{elfname}", "wb") as f:
                    print(f"WRITING /tmp/fatbin_cubin_{len(cubins):02d}_{elfname}")
                    f.write(cubin_data)

                ndx += 16 + next_offset # 16: 8 bytes for header, 8 bytes for offset
                #print("***", ndx)

            for c in cubins:
                c.parse_cubin()

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Describe argument parameter formats for kernel arguments in a ELF file")

    p.add_argument("elffile")

    args = p.parse_args()

    fatbin = NVFatBinary(args.elffile)
    fatbin.parse_fatbin()
