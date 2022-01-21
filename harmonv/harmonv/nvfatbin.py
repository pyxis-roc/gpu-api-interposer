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
import re

try:
    from nvinfo import *
except ImportError:
    from .nvinfo import *

import warnings

KPARAM = namedtuple("KPARAM", "ordinal offset size")
GLOBALINFO = namedtuple("GLOBALINFO", "name info size value other_raw")

FATBIN_MAGIC = 0xBA55ED50
OLD_STYLE_FATBIN_MAGIC = 0x1EE55A01  # not supported

# these are FATBIN_KIND_* in fatbinary.h, but this naming convention
# predates that file.

CUBIN_PTX = 1
CUBIN_ELF = 2
CUBIN_OLDCUBIN = 4
CUBIN_IR = 8  # NVVM

HOSTS = {1: "linux", 2: "mac", 3: "windows"}

DEBUG_MODE = 0
LIBRARY_MODE = 1

CONSTANT_RE = re.compile(r"\.nv\.constant(?P<bank>[0-9]+)(\.(?P<symbol>.*))?")
SHAREDMEM_RE = re.compile(r"\.nv\.shared\.(?P<symbol>.+)")
TEXTINFO_RE = re.compile(r"\.text\.(?P<symbol>.+)")

# relocation types, lots more...
R_CUDA_ABS32_20 = 42
R_CUDA_ABS32_HI_20 = 44
R_CUDA_ABS32_LO_20 = 43

R_NV_64 = 2
R_CUDA_FUNC_DESC_64 = 35

# STO_CUDA
STO_CUDA_ENTRY = 0x10

NVFATBIN_SECTION_NAME = ".nv_fatbin"
NVFATBIN_REL_SECTION_NAME = "__nv_relfatbin" # when compiled with -rdc, the PTX only stays in this section

class NVCubinPart(object):
    def __init__(self, part_type, header, data, cubin):
        self.type = part_type
        self.header = header
        self.data = data
        self.cubin = cubin
        self.decompressor = cubin.decompressor

    def get_data(self):
        # this will fail if decompress has not been called
        if self.compressed:
            return self.uncompressed_data
        else:
            return self.data

    def decompress(self):
        if hasattr(self, "uncompressed_data"):
            return

        if self.decompressor is None:
            return

        self.uncompressed_data = self.decompressor.decompress(self)
        assert self.uncompressed_data is not None, "ERROR: Failed to decompress data!"

    def get_filename(self, stem_fn=None):
        # as shown by -lelf and -lptx

        def prefix(i):
            p = i.rfind(b".")
            if p != -1:
                return i[:p]

            return i

        if stem_fn == None:
            stem_fn = prefix

        if self.identifier is not None and len(self.identifier):
            identifiers = [prefix(i) for i in self.identifier.split(b" ")]
            fullname = b"-".join(identifiers).decode("utf-8")
        else:
            if self.cubin.filename:
                # TODO: this is not the same as cuobjdump

                # generates unique names, but still not the same as
                # cuobjdump, which indexes ptx and elf files separately

                part_index = self.cubin.parts.index(self)
                index = self.cubin.index + part_index + 1
                fullname = stem_fn(
                    os.path.basename(self.cubin.filename).encode("utf-8")
                ) + b".%d" % (index,)
                fullname = fullname.decode("utf-8")
            else:
                raise NotImplementedError

        if self.type == CUBIN_PTX:
            ext = "ptx"
        elif self.type == CUBIN_ELF:
            ext = "cubin"
        else:
            assert False, "Unknown type!"

        f = f"{fullname}.sm_{self.arch}.{ext}"
        return f

    def parse_header(self):
        if self.header:
            # print([hex(a) for a in self.header])
            self.arch = struct.unpack_from("H", self.header, 0x1C)[0]
            self.cv = struct.unpack_from("I", self.header, 0x18)[0]

            self.cv = (self.cv >> 16, self.cv & 0xFFFF)

            # platform, host, compressed
            phc = struct.unpack_from("I", self.header, 0x28)[0]  # unknown if it is 32-

            self.compressed = (phc & 0x2000) == 0x2000
            self.compile_size = 64 if (phc & 1) else 32

            # unknown number of bits ...
            self.producer_id = (phc >> 2) & 1
            self.host_id = (phc >> 4) & 7

            # essentially ffs
            for b in range(3):
                if self.host_id & 1:
                    self.host_id = b + 1
                    break

                self.host_id >>= 1

            self.producer = "cuda" if self.producer_id == 1 else "unknown"
            self.host = HOSTS[self.host_id] if self.host_id in HOSTS else "unknown"

            if self.compressed:
                self.compressed_size = struct.unpack_from("I", self.header, 0x10)[0]
                self.uncompressed_size = struct.unpack_from("I", self.header, 0x38)[0]

            if len(self.header) > 0x40:
                identifierOffset = struct.unpack_from("H", self.header, 0x20)[0]
                identifierLen = struct.unpack_from("H", self.header, 0x24)[0]
                self.raw_identifier = self.header[
                    identifierOffset : identifierOffset + identifierLen
                ]
                self.identifier = self.raw_identifier[
                    : (self.raw_identifier.find(b"\0"))
                ]
            else:
                self.identifier = None

            if self.type == CUBIN_PTX and len(self.header) > 0x40:
                ptxasOptionsOffset = struct.unpack_from("H", self.header, 0x40)[0]
                ptxasOptionsLen = struct.unpack_from("H", self.header, 0x44)[0]
                self.ptxasOptions = self.header[
                    ptxasOptionsOffset : ptxasOptionsOffset + ptxasOptionsLen
                ]
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

                if self.identifier:
                    print(f" \t identifier: {self.identifier}")

                print("\n")

    def parse(self):
        raise NotImplementedError


class NVCubinPartPTX(NVCubinPart):
    def parse(self):
        if self.compressed:
            if DEBUG_MODE:
                # TODO: need elf-specific name
                with open("/tmp/fatbin_compressed", "wb") as f:
                    f.write(self.data)

            self.decompress()

            if hasattr(self, "uncompressed_data"):
                return self.uncompressed_data
        else:
            return self.data


class NVCubinPartELF(NVCubinPart):
    def get_globals(self):
        return self.nvglobals

    def get_args(self):
        return self.args

    def get_fn_info(self):
        return self.fn_info

    def parse_symtab(self, elf):
        # TODO: note that fatbin checks for sh_type == SHT_SYMTAB
        symtab = elf.get_section_by_name(".symtab")
        global_syms = []
        if symtab:
            for i, sym in enumerate(symtab.iter_symbols()):
                n = sym.name

                if sym.entry["st_info"]["bind"] == "STB_GLOBAL":
                    symtab.stream.seek(symtab["sh_offset"] + i * symtab["sh_entsize"])
                    raw_entry = symtab.stream.read(symtab["sh_entsize"])
                    other_raw = raw_entry[4 + 1]
                    gi = GLOBALINFO(
                        name=n,
                        info=sym.entry["st_info"],
                        size=sym.entry["st_size"],
                        value=sym.entry["st_value"],  # also add st_other?
                        other_raw=other_raw,
                    )

                    global_syms.append(gi)

        return global_syms

    # NOTE: mimic parse symbtab's raw reading if parse_sharedmem mimic does not work

    def get_const_symbol_offsets(self, elf):
        global_constants = {}
        for x in self.constants:
            # print(f"sym: '{x}'")
            if x == "":
                for bnk in self.constants[x]:
                    if bnk["global"]:
                        global_constants[bnk["_index"]] = bnk
                        del bnk["_index"]

        symtab = elf.get_section_by_name(".symtab")
        local_syms = {}
        if symtab:
            for i, sym in enumerate(symtab.iter_symbols()):
                n = sym.name

                if sym.entry["st_info"]["bind"] == "STB_LOCAL":
                    # gi = GLOBALINFO(name=n,
                    #                info=sym.entry['st_info'],
                    #                size=sym.entry['st_size'],
                    #                value=sym.entry['st_value'], # also add st_other?
                    #                other_raw=other_raw)
                    bnk = sym.entry["st_shndx"]
                    if bnk in global_constants:
                        if "symbols" not in global_constants[bnk]:
                            global_constants[bnk]["symbols"] = {}

                        symbols = global_constants[bnk]["symbols"]
                        if sym.entry["st_size"] > 0:
                            symbols[n] = {
                                "size": sym.entry["st_size"],
                                "offset": sym.entry["st_value"],
                            }
                        else:
                            assert n.startswith(".nv.constant"), n

    def get_global_symbol_offsets(self, elf):
        symtab = elf.get_section_by_name(".symtab")
        glbl_shndx = 12
        if symtab:
            for _, sym in enumerate(symtab.iter_symbols()):
                if sym.name == ".nv.global.init":
                    glbl_shndx = sym.entry["st_shndx"]
                elif sym.entry["st_shndx"] == glbl_shndx:
                    # this is a global symbol
                    self.global_symbol_offset[sym.name] = dict(
                        size=sym.entry["st_size"], offset=sym.entry["st_value"]
                    )

    def parse_nv_info_section(self, s, data):
        ndx = 0
        section_size = len(data)
        out = []
        # print(s.name)
        while ndx < section_size:
            attr_fmt = struct.unpack_from("H", data, ndx)[0]
            attr_size = struct.unpack_from("H", data, ndx + 2)[0]
            # print(f"{attr_fmt:x} {attr_size}")
            ndx += 4

            # possibly use construct?

            out.append(ATTR_INFO(attr_fmt, attr_size, data[ndx : ndx + attr_size]))

            # TODO: refactor this using nvinfo

            if attr_fmt == 0x1704:  # EIATTR_KPARAM_INFO, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0xA04:  # EIATTR_PARAM_CBANK, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x0D04:  # EIATTR_SYNC_STACK, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x204:  # EIATTR_IMAGE_SLOT, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x1903:  # EIATTR_CBANK_PARAM_SIZE, EIFMT_HVAL
                pass
            elif attr_fmt == 0x2304:  # EIATTR_MAX_STACK_SIZE
                ndx += attr_size
            elif attr_fmt == 0x1204:  # EIATTR_MIN_STACK_SIZE_
                ndx += attr_size
            elif attr_fmt == 0x1104:  # EIATTR_FRAME_SIZE
                ndx += attr_size
            elif attr_fmt == 0x1B03:  # EIATTR_MAXREG_COUNT # uses 0x00ff as 'attr_size'
                pass
            elif attr_fmt == 0x1C04:  # EIATTR_EXIT_INSTR_OFFSETS
                ndx += attr_size
            elif attr_fmt == 0x1E04:  # EIATTR_CRS_STACK_SIZE
                ndx += attr_size
            elif attr_fmt == 0x504:  # EIATTR_MAX_THREADS
                ndx += attr_size
            elif attr_fmt == 0x1D04:  # EIATTR_S2RCTAID_INSTR_OFFSETS
                ndx += attr_size
            elif attr_fmt == 0xF04:  # EIATTR_EXTERNS
                ndx += attr_size
            elif attr_fmt == 0x1F01:  # EIATTR_NEED_CNP_WRAPPER
                ndx += attr_size
            elif attr_fmt == 0x2001:  # EIATTR_NEED_CNP_PATCH
                ndx += attr_size
            elif attr_fmt == 0x401:  # EIATTR_CTAIDZ_USED
                ndx += attr_size
            elif attr_fmt == 0x2A01:  # EIATTR_SW1850030_WAR
                ndx += attr_size
            elif attr_fmt == EIATTR_SW2393858_WAR:
                ndx += attr_size
            elif attr_fmt == 0x2804:  # EIATTR_COOP_GROUP_INSTR_OFFSETS
                ndx += attr_size
            elif attr_fmt == EIATTR_REGCOUNT:  # EIATTR_REGCOUNT
                ndx += attr_size
            elif attr_fmt == EIATTR_CUDA_API_VERSION:
                ndx += attr_size
            elif attr_fmt == EIATTR_SW_WAR:
                ndx += attr_size
            elif attr_fmt == EIATTR_INT_WARP_WIDE_INSTR_OFFSETS:
                ndx += attr_size
            elif attr_fmt == EIATTR_LD_CACHEMOD_INSTR_OFFSETS:
                ndx += attr_size
            elif attr_fmt == EIATTR_INDIRECT_BRANCH_TARGETS:
                ndx += attr_size
            elif attr_fmt == EIATTR_SW2861232_WAR:
                ndx += attr_size
            elif (
                attr_fmt == EIATTR_BINDLESS_TEXTURE_BANK
            ):  # EIATTR_BINDLESS_TEXTURE_BANK
                ndx += attr_size
            elif attr_fmt == EIATTR_EXPLICIT_CACHING:
                ndx += attr_size
            else:
                warnings.warn(
                    f"{self.get_filename()}: Unrecognized param info attribute  {attr_fmt:x} {attr_size}"
                )
                ndx += attr_size

        return out

    def parse_param_info(self, info):
        args = []
        for nfo in info:
            if nfo.attr_fmt == EIATTR_KPARAM_INFO:  # EIATTR_KPARAM_INFO, EIFMT_SVAL
                # W,S,S,B[4]
                ordinal = struct.unpack_from("H", nfo.data, 0 + 4)[0]
                offset = struct.unpack_from("H", nfo.data, 0 + 6)[0]
                size = struct.unpack_from("H", nfo.data, 0 + 10)[0] >> 2
                # Pointee's logAlignment : 0x0    Space : 0x0     cbank : 0x1f    Parameter Space : CBANK

                args.append(KPARAM(ordinal=ordinal, offset=offset, size=size))

        return args

    def parse_fn_info(self, info):
        out = {}
        for nfo in info:
            if nfo.attr_fmt == 0x1B03:
                out[
                    "EIATTR_MAXREG_COUNT"
                ] = nfo.attr_size  # unused, SHI_REGISTERS is used instead
            elif nfo.attr_fmt == EIATTR_CBANK_PARAM_SIZE:
                out["EIATTR_CBANK_PARAM_SIZE"] = nfo.attr_size
                # struct.unpack_from('H', nfo.data, 0)[0]
            elif nfo.attr_fmt == EIATTR_PARAM_CBANK:
                start, size = struct.unpack_from("HH", nfo.data, 4)  # skip word
                out["EIATTR_PARAM_CBANK"] = {"start": start, "size": size}
            elif nfo.attr_fmt == EIATTR_REGCOUNT:
                pass
            elif nfo.attr_fmt == EIATTR_CUDA_API_VERSION:
                version = struct.unpack_from("I", nfo.data, 0)[0]
                out[
                    "EIATTR_CUDA_API_VERSION"
                ] = version  # this is version * 10, so 111 for 11.1
            elif nfo.attr_fmt == EIATTR_FRAME_SIZE:
                # TODO: Get index, look up index in symbtab, write to the function with that index
                size = struct.unpack_from("I", nfo.data, 0)[0]
                out["EIATTR_FRAME_SIZE"] = size
            elif nfo.attr_fmt == EIATTR_MAX_STACK_SIZE:
                size = struct.unpack_from("I", nfo.data, 0)[0]
                out["EIATTR_MAX_STACK_SIZE"] = size
            elif nfo.attr_fmt == EIATTR_MIN_STACK_SIZE:
                size = struct.unpack_from("I", nfo.data, 0)[0]
                out["EIATTR_MIN_STACK_SIZE"] = size
            elif nfo.attr_fmt == EIATTR_MAX_THREADS:
                threads = struct.unpack_from("III", nfo.data, 0)
                out["EIATTR_MAX_THREADS"] = list(threads)
            elif nfo.attr_fmt == EIATTR_EXPLICIT_CACHING:
                out["EIATTR_EXPLICIT_CACHING"] = 1

        return out

    # deprecated, do not use
    def parse_nv_param_info_section(self, s, data):
        ndx = 0
        section_size = len(data)
        args = []
        # print(s.name)
        while ndx < section_size:
            attr_fmt = struct.unpack_from("H", data, ndx)[0]
            attr_size = struct.unpack_from("H", data, ndx + 2)[0]
            # print(f"{attr_fmt:x} {attr_size}")
            ndx += 4

            # possibly use construct?

            if attr_fmt == 0x1704:  # EIATTR_KPARAM_INFO, EIFMT_SVAL
                ordinal = struct.unpack_from("H", data, ndx + 4)[0]
                offset = struct.unpack_from("H", data, ndx + 6)[0]
                size = struct.unpack_from("H", data, ndx + 10)[0] >> 2

                args.append(KPARAM(ordinal=ordinal, offset=offset, size=size))
                # print(f"\t{ordinal} {offset} {size}")

                ndx += attr_size
            elif attr_fmt == 0xA04:  # EIATTR_PARAM_CBANK, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x0D04:  # EIATTR_SYNC_STACK, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x204:  # EIATTR_IMAGE_SLOT, EIFMT_SVAL
                ndx += attr_size
            elif attr_fmt == 0x1903:  # EIATTR_CBANK_PARAM_SIZE, EIFMT_HVAL
                pass
            elif attr_fmt == 0x2304:  # EIATTR_MAX_STACK_SIZE
                ndx += attr_size
            elif attr_fmt == 0x1204:  # EIATTR_MIN_STACK_SIZE_
                ndx += attr_size
            elif attr_fmt == 0x1104:  # EIATTR_FRAME_SIZE
                ndx += attr_size
            elif attr_fmt == 0x1B03:  # EIATTR_MAXREG_COUNT
                pass
            elif attr_fmt == 0x1C04:  # EIATTR_EXIT_INSTR_OFFSETS
                ndx += attr_size
            elif attr_fmt == 0x1E04:  # EIATTR_CRS_STACK_SIZE
                ndx += attr_size
            elif attr_fmt == 0x504:  # EIATTR_MAX_THREADS
                ndx += attr_size
            elif attr_fmt == 0x1D04:  # EIATTR_S2RCTAID_INSTR_OFFSETS
                ndx += attr_size
            elif attr_fmt == 0xF04:  # EIATTR_EXTERNS
                ndx += attr_size
            elif attr_fmt == 0x1F01:  # EIATTR_NEED_CNP_WRAPPER
                ndx += attr_size
            elif attr_fmt == 0x2001:  # EIATTR_NEED_CNP_PATCH
                ndx += attr_size
            elif attr_fmt == 0x401:  # EIATTR_CTAIDZ_USED
                ndx += attr_size
            elif attr_fmt == 0x2A01:  # EIATTR_SW1850030_WAR
                ndx += attr_size
            elif attr_fmt == 0x2804:  # EIATTR_COOP_GROUP_INSTR_OFFSETS
                ndx += attr_size
            else:
                print(
                    f"WARNING: unrecognized param info attribute  {attr_fmt:x} {attr_size}"
                )
                ndx += attr_size

        return args

    def parse_constant(self, index, section, data):
        m = CONSTANT_RE.match(section.name)

        assert m is not None, f"Couldn't parse constant section name: {section.name}"

        bank = int(m.group("bank"))
        symbol = m.group("symbol")
        out = {"bank": bank, "data": data}
        if symbol is None:
            if section.name in self.relocations:
                symbol = []
                for r in self.relocations[section.name]:
                    assert r[0]['r_info_type'] == R_CUDA_FUNC_DESC_64, r
                    symbol.append(r[1])
            else:
                symbol = [''] # possibly global

            out['global'] = True
            out['_index'] = index
        else:
            symbol = [symbol]

        return symbol, out

    def parse_sharedmem(self, section):
        m = SHAREDMEM_RE.match(section.name)
        assert (
            m is not None
        ), f"Couldn't parse shared memory section name: {section.name}"
        symbol = m.group("symbol")

        return symbol, section.data_size

    def parse_textinfo(self, section):
        m = TEXTINFO_RE.match(section.name)
        assert m is not None, f"Couldn't parse text info section name: {section.name}"
        symbol = m.group("symbol")
        nbars = (int(section.header["sh_flags"]) & 0x7F00000) >> 20
        nregs = (int(section.header["sh_info"]) & 0xFF000000) >> 24

        return symbol, nbars, nregs

    # parse_text print section.sh_info

    def parse_relocations(self, section):
        if section.name.startswith(".rel."):
            target = section.name[4:]
            symtab = self.cubin_elf.get_section(section["sh_link"])
            out = []
            for r in section.iter_relocations():
                out.append((r, symtab.get_symbol(r["r_info_sym"]).name))

            return target, out
        else:  # rela
            return None, None
            # raise NotImplementedError(f"Don't support rela-sections {section.name}")

    def parse(self):
        data = self.data
        if self.compressed:
            self.decompress()

            if hasattr(self, "uncompressed_data"):
                data = self.uncompressed_data
            else:
                warnings.warn("Don't know how to parse compressed ELFs")
                return

        self.cubin_elf = ELFFile(io.BytesIO(data))
        # # see Nervana's maxas cubin file for more details on properties
        self.elf_arch = self.cubin_elf.header["e_flags"] & 0xFF

        if (not LIBRARY_MODE) and DEBUG_MODE:
            print(f"elf: arch={self.elf_arch}")

        gs = self.parse_symtab(self.cubin_elf)
        self.nvglobals = gs
        self.args = {}
        self.fn_info = {}
        self.constants = {}
        self.relocations = {}
        self.sharedmem = {}
        self.numbar = {}
        self.numregs = {}
        self.global_init_data = {}
        self.global_symbol_offset = {}

        for index, s in enumerate(self.cubin_elf.iter_sections()):
            if s.name.startswith(".nv.info"):
                info = self.parse_nv_info_section(s, s.data())
                # args = self.parse_nv_param_info_section(s, s.data())
                args = self.parse_param_info(info)
                fninfo = self.parse_fn_info(info)

                self.args[s.name[9:]] = args
                self.fn_info[s.name[9:]] = fninfo
            elif s.name.startswith(".nv.constant"):
                fn_names, const = self.parse_constant(index, s, s.data())
                assert isinstance(fn_names, list), fn_names
                for fn_name in fn_names:
                    if fn_name not in self.constants:
                        self.constants[fn_name] = []
                    self.constants[fn_name].append(const)
            elif isinstance(s, elftools.elf.relocation.RelocationSection):
                tgt, relocs = self.parse_relocations(s)
                self.relocations[tgt] = relocs
            elif s.name.startswith(".nv.shared"):
                fn_name, shmem_size = self.parse_sharedmem(s)
                self.sharedmem[fn_name] = shmem_size
            elif s.name.startswith(".text"):
                fn_name, nbars, nregs = self.parse_textinfo(s)
                self.numbar[fn_name] = nbars
                self.numregs[fn_name] = nregs
            elif s.name.startswith(".nv.global.init"):
                self.global_init_data["size"] = s.data_size
                self.global_init_data["data"] = s.data()

            # elif s.name.startswith('text.') (write matcher for text sections)

        self.get_const_symbol_offsets(self.cubin_elf)

        self.get_global_symbol_offsets(self.cubin_elf)  # fill offsets from symbol table

        if (not LIBRARY_MODE) and DEBUG_MODE:
            print(self.nvglobals)
            print(self.args)


class NVCubin(object):
    def __init__(self, cubin_data, decompressor=None, filename=None, index=0):
        self.cubin_data = cubin_data
        self.decompressor = decompressor
        self.filename = filename
        self.index = index

    def parse_cubin(self):
        cubin_part_header = struct.Struct("IIQ")
        assert cubin_part_header.size == 16, len(cubin_part_header.size)

        # TODO: verify endian-ness assumptions from Power-generated cubins

        self.parts = []
        ndx = 0
        while ndx < len(self.cubin_data):
            magic, header_size, part_size = cubin_part_header.unpack_from(
                self.cubin_data, ndx
            )
            # print(f"header size: 0x{header_size:x}")

            header = self.cubin_data[ndx : ndx + header_size]
            ndx += header_size

            part_data = self.cubin_data[ndx : ndx + part_size]
            ndx += part_size

            part_type = magic & 0xFF
            if part_type == CUBIN_PTX:
                self.parts.append(NVCubinPartPTX(part_type, header, part_data, self))
            elif part_type == CUBIN_ELF:
                self.parts.append(NVCubinPartELF(part_type, header, part_data, self))
            else:
                assert False, f"Unknown part_type: {part_type}"

            self.parts[-1].parse_header()
            self.parts[-1].parse()

        if not LIBRARY_MODE:
            print(f"Cubin contains {len(self.parts)} parts")


class NVFatBinary(object):
    def __init__(self, elf, decompressor=None):
        self.elf = elf
        self.felf = open(elf, "rb")
        self.decompressor = decompressor

    def parse_fatbin(self, nv_fatbin_section = NVFATBIN_SECTION_NAME):
        self.elffile = ELFFile(self.felf)

        if self.elffile.elfclass != 64:
            print("ERROR: Only 64-bit binaries supported", file=sys.stderr)
            return 0

        nv_fatbin = self.elffile.get_section_by_name(nv_fatbin_section)
        if nv_fatbin:
            if DEBUG_MODE: print(f"Using section: {nv_fatbin_section}")

        if nv_fatbin:
            fatbin_header = struct.Struct("IHHQ")  # from fatbinary.h
            assert fatbin_header.size == 16, fatbin_header.size

            elfname = os.path.basename(self.elf)
            self.fatbin_data = nv_fatbin.data()

            if DEBUG_MODE:
                with open(f"/tmp/fatbin_complete_{elfname}", "wb") as f:
                    f.write(self.fatbin_data)

            # there are multiple cubins, one per object
            cubins = []
            ndx = 0
            while ndx + fatbin_header.size < len(
                self.fatbin_data
            ):  # clang sets weird next offset?
                magic, version, hdrSize, next_offset = fatbin_header.unpack_from(
                    self.fatbin_data, ndx
                )
                if magic != FATBIN_MAGIC:
                    raise NotImplementedError(
                        f"Don't support fat binary with magic={magic:x}"
                    )
                ndx += hdrSize  # fatbin_header.size

                # if next_offset == 0:
                #    continue

                cubin_data = self.fatbin_data[ndx : (ndx + next_offset)]
                cubins.append(
                    NVCubin(
                        cubin_data,
                        decompressor=self.decompressor,
                        filename=self.elf,
                        index=len(cubins),
                    )
                )

                if DEBUG_MODE:
                    with open(
                        f"/tmp/fatbin_part_{len(cubins):02d}_{elfname}", "wb"
                    ) as f:
                        print(f"WRITING /tmp/fatbin_part_{len(cubins):02d}_{elfname}")
                        f.write(
                            fatbin_header.pack(magic, version, hdrSize, next_offset)
                        )
                        f.write(cubin_data)

                    with open(
                        f"/tmp/fatbin_cubin_{len(cubins):02d}_{elfname}", "wb"
                    ) as f:
                        print(f"WRITING /tmp/fatbin_cubin_{len(cubins):02d}_{elfname}")
                        f.write(cubin_data)

                ndx += next_offset

            for c in cubins:
                c.parse_cubin()

            self.cubins = cubins


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Describe argument parameter formats for kernel arguments in a ELF file"
    )

    p.add_argument("elffile")
    p.add_argument("-d", dest="debug", action="store_true")
    p.add_argument("-r", dest="rel", help="Dump relocatable fatbin", action="store_true")

    args = p.parse_args()

    DEBUG_MODE = args.debug
    LIBRARY_MODE = 0

    fatbin = NVFatBinary(args.elffile)
    fatbin.parse_fatbin(NVFATBIN_REL_SECTION_NAME if args.rel else NVFATBIN_SECTION_NAME)
