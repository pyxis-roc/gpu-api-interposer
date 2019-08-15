#!/usr/bin/env python3

import argparse
from elftools.elf.elffile import ELFFile
import elftools
import sys
import io
import struct
from collections import namedtuple

KPARAM = namedtuple('KPARAM', 'ordinal offset size')
GLOBALINFO = namedtuple('GLOBALINFO', 'info size value')

class NVFatBinary(object):
    def __init__(self, elf):
        self.elf = elf
        self.felf = open(elf, "rb")


    def parse_symtab(self, elf):
        # TODO: note that fatbin checks for sh_type == SHT_SYMTAB
        symtab = elf.get_section_by_name(".symtab")
        global_syms = []
        if symtab:
            for sym in symtab.iter_symbols():
                n = sym.name
                if sym.entry['st_info']['bind'] == 'STB_GLOBAL':
                    gi = GLOBALINFO(info=sym.entry['st_info'],
                                    size=sym.entry['st_size'],
                                    value=sym.entry['st_value'])

                    global_syms.append(gi)

        return gi

    def parse_fatbin(self):
        # TODO: some cubins apparently start with PTX, skip, see fatbin.cc

        self.elffile = ELFFile(self.felf)

        if self.elffile.elfclass != 64:
            #print("ERROR: Only 64-bit binaries supported", file=sys.stderr)
            return 0

        nv_fatbin = self.elffile.get_section_by_name('.nv_fatbin')

        if nv_fatbin:
            print(nv_fatbin.data_size)

            off = 0x50
            #off += 0x2b8

            with open("/tmp/fatbin_complete", "wb") as f:
                f.write(nv_fatbin.data())

            self.fatbin_data = io.BytesIO(nv_fatbin.data()[(off):])
            with open("/tmp/fatbin", "wb") as f:
                f.write(self.fatbin_data.getvalue())

            self.fatbin_elf = ELFFile(self.fatbin_data)

            assert self.fatbin_elf.elfclass == 64, self.fatbin_elf.elfclass

            gs = self.parse_symtab(self.fatbin_elf)
            #strtab = self.fatbin_elf.get_section_by_name('.strtab')

            for s in self.fatbin_elf.iter_sections():
                #print(s.name)
                if s.name[:8] == ".nv.info":
                    self.parse_nv_param_info_section(s, s.data())

    def parse_nv_param_info_section(self, s, data):
        ndx = 0
        section_size = len(data)
        args = []
        print(s.name)
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
            else:
                print(f"unrecognized {attr_fmt:x} {attr_size}")
                ndx += attr_size

        return args

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Describe argument parameter formats for kernel arguments in a ELF file")

    p.add_argument("elffile")

    args = p.parse_args()

    fatbin = NVFatBinary(args.elffile)
    fatbin.parse_fatbin()
