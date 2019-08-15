#!/usr/bin/env python3

import argparse
import struct

# experimental code for decoding cubin structure

def roundup(v, d):
    if v % d:
        v += (v % d)

    return v

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Parse argument header")
    p.add_argument("fatbin")
    args = p.parse_args()

    with open(args.fatbin, "rb") as f:
        while True:
            cur_pos = f.tell()
            header = f.read(0x10)
            if len(header) == 0: break
            print([hex(a) for  a in header])

            next_offset = struct.unpack_from('Q', header, 8)[0]

            if next_offset > 0:
                next_offset = cur_pos + 16 + next_offset
                print(f">>> 0x{next_offset:x}")

                while f.tell() < next_offset:
                    cur_cubin_pos = f.tell()
                    print("cur_pos", hex(cur_cubin_pos))
                    cubin_header = f.read(0x40)
                    cubin_part_size = struct.unpack_from('Q', cubin_header, 0x8)[0]

                    if cubin_part_size == 0: break

                    # could be 32-bit or 16-bit?
                    cubin_header_size = struct.unpack_from('I', cubin_header, 0x4)[0]

                    if cubin_header[0] == 0x1: # PTX?
                        print("PTX")
                    elif cubin_header[0] == 0x2: # ELF?
                        print("ELF")

                    f.seek(cubin_header_size - 0x40, 1)

                    print([hex(a) for a in cubin_header[:4]])
                    print(hex(cubin_part_size))

                    arch = struct.unpack_from('H', cubin_header, 0x1c)[0]
                    code_version_1 = struct.unpack_from('H', cubin_header, 0x18)[0]
                    code_version_2 = struct.unpack_from('H', cubin_header, 0x1a)[0]
                    print(arch)
                    print(code_version_2, " ", code_version_1)

                    f.seek(cubin_part_size, 1)
            else:
                print("NO CUBIN FOUND")
