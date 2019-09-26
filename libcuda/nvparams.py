#!/usr/bin/env python3

#
# nvparams.py
#
# libcuda_record parameter helper.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, The University of Rochester

from harmonv import nvfatbin, compression
import argparse
import yaml
import array
import struct

def get_kernel_arguments(elffile):
    fatbin = nvfatbin.NVFatBinary(elffile, compression.DecompressorCuobjdump)
    fatbin.parse_fatbin()

    all_out = []
    for cubin in fatbin.cubins:
        for p in cubin.parts:
            if type(p) is nvfatbin.NVCubinPartELF:
                part = {'arch': p.elf_arch,
                        'globals': {},
                        'params': {}}

                for g in p.get_globals():
                    part['globals'][g.name] = {'size': g.size,
                                               'value': g.value}

                params = p.get_args()
                for f in params:
                    if f == '':
                        continue

                    out = []
                    for p in params[f]:
                        out.append(dict(p._asdict()))

                    out.sort(key=lambda x: x['ordinal'])

                    #print(bytes(f.encode('utf-8')))
                    part['params'][f] = out

                if len(part['globals']) or len(part['params']):
                    all_out.append(part)

    return all_out

# this creates a helper file -- ultimately we want this to read the section file in memory?
def create_arg_recorder_helper(param_data, outputfile, consolidate):
    # arches
    arch = []

    # is it possible to have multiple modules for same arch?
    out = {}
    for module in param_data:
        arch = module['arch']
        #arch.append()

        for f in module['params']:
            if f not in out:
                out[f] = []

            fp = module['params'][f]

            if fp: assert [i == x['ordinal'] for i, x in enumerate(fp)]

            out[f].append({'arch': arch,
                           'param_sizes': tuple([x['size'] for x in fp]),
                           'param_offsets': tuple([x['offset'] for x in fp])
            })

    for f in out:
        ps = all([out[f][0]['param_sizes'] == x['param_sizes'] for x in out[f]])
        po = all([out[f][0]['param_offsets'] == x['param_offsets'] for x in out[f]])

        assert all([len(out[f][0]['param_sizes']) == len(x['param_sizes']) for x in out[f]]), out[f]
        assert all([len(out[f][0]['param_offsets']) == len(x['param_offsets']) for x in out[f]]), out[f]
        assert len(out[f][0]['param_sizes']) == len(out[f][0]['param_offsets'])

        if ps and po and consolidate:
            # consolidate into a universal arch
            out[f] = [{'arch': 0,
                      'param_sizes': out[f][0]['param_sizes'],
                      'param_offsets': out[f][0]['param_offsets']}]

    # prepare a string table
    strtab = sorted(out.keys())
    bstrtab = bytes()

    for f in strtab:
        bstrtab += bytes(f.encode('ascii'))
        bstrtab += b'\0'

    # align to 4
    bstrtab += b'\0' * (4 - len(bstrtab) % 4)

    bparams = array.array('B')
    offsets = array.array('I') # overkill, but 64K might be too small

    for f in strtab:
        offsets.append(len(bparams))

        bparams.append(len(out[f])) # number of archs

        for apd in out[f]:
            bparams.append(apd['arch']) # arch
            bparams.append(len(apd['param_sizes'])) # size of params
            bparams += array.array('B', apd['param_sizes']) # assumes all param_size arrays are equal in length
            bparams += array.array('B', apd['param_offsets'])

    output = struct.pack('I', 1) # version
    output += struct.pack('I', len(strtab)) # number of entries 
    output += struct.pack('I', len(bstrtab)) # size of bstrtab
    output += bstrtab # binary strtab
    output += offsets.tobytes() # offsets into paramtab
    output += bparams # paramtab

    if outputfile:
        with open(outputfile, "wb") as f:
            f.write(output)

    return (out, output)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Obtain parameter offset and size information for kernels")
    p.add_argument("executable", help="ELF executable")
    p.add_argument("output", help="Output file")
    p.add_argument("--no-consolidate", help="Do not consolidate arguments for different arches into a single universal arch", action="store_true")
    args = p.parse_args()

    ka = get_kernel_arguments(args.executable)
    if len(ka) > 0:
        d, b = create_arg_recorder_helper(ka, args.output, not args.no_consolidate)

        with open(args.output + ".yaml", "w") as f:
            f.write(yaml.dump(d))
    else:
        print("ERROR: No kernel argument information found. Does the binary contain ELF sections?")
        sys.exit(1)
