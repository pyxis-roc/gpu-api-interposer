#!/usr/bin/env python3
#
# nvfatbin.py
#
# Parser for NVIDIA fatbin sections in ELF files
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, The University of Rochester
# Copyright (C) 2013, Sreepathi Pai

import argparse
from elftools.elf.elffile import ELFFile
import elftools
import sys
import io
import struct
from collections import namedtuple
import os
import zlib

KPARAM = namedtuple('KPARAM', 'ordinal offset size')
GLOBALINFO = namedtuple('GLOBALINFO', 'name info size value')

CUBIN_PTX = 1
CUBIN_ELF = 2

HOSTS = {1: "linux",
         2: "mac",
         3: "windows"}

DEBUG_MODE = 0
LIBRARY_MODE = 1

class NVCubinPart(object):
    def __init__(self, part_type, header, data):
        self.type = part_type
        self.header = header
        self.data = data

    def parse_header(self):
        if self.header:
            #print([hex(a) for a in self.header])
            self.arch = struct.unpack_from('H', self.header, 0x1c)[0]
            self.cv = struct.unpack_from('I', self.header, 0x18)[0]

            self.cv = (self.cv >> 16, self.cv & 0xffff)

            # platform, host, compressed
            phc = struct.unpack_from('I', self.header, 0x28)[0] # unknown if it is 32-

            self.compressed = (phc & 0x2000) == 0x2000
            self.compile_size = 64 if (phc & 1) else 32

            # unknown number of bits ...
            self.producer_id = (phc >> 2) & 1
            self.host_id = ((phc >> 4) & 7)

            # essentially ffs
            for b in range(3):
                if self.host_id & 1:
                    self.host_id = b + 1
                    break

                self.host_id >>= 1

            self.producer = "cuda" if self.producer_id == 1 else "unknown"
            self.host = HOSTS[self.host_id] if self.host_id in HOSTS else "unknown"

            if self.compressed:
                self.compressed_size = struct.unpack_from('I', self.header, 0x10)[0]
                self.uncompressed_size = struct.unpack_from('I', self.header, 0x38)[0]

            if self.type == CUBIN_PTX and len(self.header) > 0x40:
                ptxasOptionsOffset = struct.unpack_from('H', self.header, 0x40)[0]
                ptxasOptionsLen = struct.unpack_from('H', self.header, 0x44)[0]
                self.ptxasOptions = self.header[ptxasOptionsOffset:ptxasOptionsOffset+ptxasOptionsLen]
            else:
                self.ptxasOptions = None

            if not LIBRARY_MODE:
                if self.type == CUBIN_PTX:
                    print("ptx\n===")
                elif self.type == CUBIN_ELF:
                    print("elf\n===")
                else:
                    print("unknown\n===")

                print(f"arch: sm_{self.arch}")
                print(f"version: [{self.cv}]")
                print(f"phc: 0x{phc:x}")
                print(f"producer: {self.producer} [0x{self.producer_id:x}]")
                print(f"host: {self.host} [0x{self.host_id:x}]")
                print(f"compile_size: {self.compile_size}-bit")
                print(f"compressed: {self.compressed}")
                if self.compressed:
                    print(f" \t compressed size: {self.compressed_size}")
                    print(f" \t uncompressed size: {self.uncompressed_size}")

                if self.ptxasOptions:
                    print(f" \t ptxasOptions: {self.ptxasOptions}")

                print("\n")

    def parse(self):
        raise NotImplementedError

class NVCubinPartPTX(NVCubinPart):
    def parse(self):
        if self.compressed:
            if DEBUG_MODE:
                #TODO: need elf-specific name
                with open("/tmp/fatbin_compressed", "wb") as f:
                    f.write(self.data)

            if hasattr(self, 'uncompressed_data'):
                return self.uncompressed_data
        else:
            return self.data


class NVCubinPartELF(NVCubinPart):
    def get_globals(self):
        return self.nvglobals

    def get_args(self):
        return self.args

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

    def parse(self):
        if self.compressed:
            print("elf_parse: Don't know how to handle compressed ELFs")
            print(self.data[:16])
            #zlib.decompress(self.data)
            return

        self.cubin_elf = ELFFile(io.BytesIO(self.data))
        # # see Nervana's maxas cubin file for more details on properties
        self.elf_arch = self.cubin_elf.header['e_flags'] & 0xFF

        if not LIBRARY_MODE:
            print(f'elf: arch={self.elf_arch}')

        gs = self.parse_symtab(self.cubin_elf)
        self.nvglobals = gs
        self.args = {}
        for s in self.cubin_elf.iter_sections():
            #print(s.name)
            if s.name[:8] == ".nv.info":
                args = self.parse_nv_param_info_section(s, s.data())
                self.args[s.name[9:]] = args

        if not LIBRARY_MODE:
            print(self.nvglobals)
            print(self.args)

class NVCubin(object):
    def __init__(self, cubin_data):
        self.cubin_data = cubin_data

    def parse_cubin(self):
        cubin_part_header = struct.Struct('IIQ')
        assert cubin_part_header.size == 16, len(cubin_part_header.size)

        #TODO: verify endian-ness assumptions from Power-generated cubins

        self.parts = []
        ndx = 0
        while ndx < len(self.cubin_data):
            magic, header_size, part_size = cubin_part_header.unpack_from(self.cubin_data,
                                                                          ndx)
            #print(f"header size: 0x{header_size:x}")

            header = self.cubin_data[ndx:ndx+header_size]
            ndx += header_size

            part_data = self.cubin_data[ndx:ndx+part_size]
            ndx += part_size

            part_type = magic & 0xff
            if part_type == CUBIN_PTX:
                self.parts.append(NVCubinPartPTX(part_type, header, part_data))
            elif part_type == CUBIN_ELF:
                self.parts.append(NVCubinPartELF(part_type, header, part_data))
            else:
                assert False, f"Unknown part_type: {part_type}"

            self.parts[-1].parse_header()
            self.parts[-1].parse()

        if not  LIBRARY_MODE:
            print(f"Cubin contains {len(self.parts)} parts")

class NVFatBinary(object):
    def __init__(self, elf):
        self.elf = elf
        self.felf = open(elf, "rb")

    def parse_fatbin(self):
        self.elffile = ELFFile(self.felf)

        if self.elffile.elfclass != 64:
            print("ERROR: Only 64-bit binaries supported", file=sys.stderr)
            return 0

        for nv_fatbin_name in [".nv_fatbin", "__nv_relfatbin"]: # executables, .o: though the latter also exists in executables and contains ptx data (for example).
            nv_fatbin = self.elffile.get_section_by_name(nv_fatbin_name)
            if nv_fatbin:
                if DEBUG_MODE: print(f"Using section: {nv_fatbin_name}")
                break

        if nv_fatbin:
            fatbin_header = struct.Struct('QQ')
            assert fatbin_header.size == 16, fatbin_header.size

            elfname = os.path.basename(self.elf)
            self.fatbin_data = nv_fatbin.data()

            if DEBUG_MODE:
                with open(f"/tmp/fatbin_complete_{elfname}", "wb") as f:
                    f.write(self.fatbin_data)

            # there are multiple cubins, one per object
            cubins = []
            ndx = 0
            while ndx < len(self.fatbin_data):
                magic, next_offset = fatbin_header.unpack_from(self.fatbin_data, ndx)
                ndx += fatbin_header.size

                #if next_offset == 0:
                #    continue

                cubin_data = self.fatbin_data[ndx:(ndx + next_offset)]
                cubins.append(NVCubin(cubin_data))

                if DEBUG_MODE:
                    with open(f"/tmp/fatbin_part_{len(cubins):02d}_{elfname}", "wb") as f:
                        print(f"WRITING /tmp/fatbin_part_{len(cubins):02d}_{elfname}")
                        f.write(fatbin_header.pack(magic, next_offset))
                        f.write(cubin_data)

                    with open(f"/tmp/fatbin_cubin_{len(cubins):02d}_{elfname}", "wb") as f:
                        print(f"WRITING /tmp/fatbin_cubin_{len(cubins):02d}_{elfname}")
                        f.write(cubin_data)

                ndx += next_offset

            for c in cubins:
                c.parse_cubin()

            self.cubins = cubins

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Describe argument parameter formats for kernel arguments in a ELF file")

    p.add_argument("elffile")
    p.add_argument("-d", dest="debug", action="store_true")

    args = p.parse_args()

    DEBUG_MODE = args.debug
    LIBRARY_MODE = 0

    fatbin = NVFatBinary(args.elffile)
    fatbin.parse_fatbin()
