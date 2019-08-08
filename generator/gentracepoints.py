#!/usr/bin/env python3

import argparse
import sys
import yaml
from collections import namedtuple
import geninterposer
from pycparser import c_generator

TP_Arg = namedtuple('tp_arg', ['type', 'name'])
TP_Field = namedtuple('tp_field', ['type', 'fieldname', 'type_args'])

FIELD_FMTS = {
    "ctf_integer": "ctf_integer({int_type}, {fieldname}, {expr})",
    "ctf_integer_hex": "ctf_integer_hex({int_type}, {fieldname}, {expr})",
    "ctf_string": "ctf_string({field_name}, {expr})"
}

def generate_tracepoint_template(recipe, output, ig):
    provider = recipe['main']['provider']

    tracepoint_probes = {}
    dn = dict([(x['origname'], x) for x in ig.get_decl_nodes()])

    with open(output, "w") as outf:
        outf.write("/* automatically generated, do not edit */\n")

        if 'includes' in recipe:            
            for i in recipe['includes'].get('system', []):
                outf.write(f"#include <{i}>\n")

            for i in recipe['includes'].get('local', []):
                outf.write(f'#include "{i}"\n')

        for e in recipe['tracepoint_events']:
            tpe = recipe['tracepoint_events'][e]
            args = []

            if tpe['fn'] not in dn:
                print(f"WARNING: Function {tpe['fn']} does not exist in header, ignoring.", file=sys.stderr)
                continue

            #TODO: allow reading arguments from function (dn above) and not from recipe
            for a in tpe['args']:
                if isinstance(a, dict):
                    assert len(a) == 1, f'Arg dictionary must contain only argname {a}'
                    argname = list(a.keys())[0] 

                    args.append(TP_Arg(type=a[argname]['type'], name=argname))
                else:
                    # string type, get arg type from function defn
                    pass

            fields = []
            for f in tpe['fields']:
                if isinstance(f, dict):
                    assert len(f) == 1, f'Field dictionary must contain only argname {f}'
                    fieldname = list(f.keys())[0]

                    # yeah, yeah ...
                    name = fieldname if 'fieldname' not in f[fieldname] else f[fieldname]['fieldname']

                    fields.append(TP_Field(type=f[fieldname]['type'], 
                                           fieldname=name, 
                                           type_args=f[fieldname]['type_args']))
                else:
                    # TODO: get field types from arg names
                    pass

            CALL_ARGS = ", ".join([a.name for a in args])
            if len(CALL_ARGS): CALL_ARGS = ", " + CALL_ARGS

            TP_ARGS = "TP_ARGS(" + ",\n".join([f"{a.type}, {a.name}" for a in args]) + ")"
            TP_FIELDS = "TP_FIELDS(" + "\n".join([FIELD_FMTS[f.type].format(fieldname=f.fieldname, 
                                                                        **f.type_args) for f in fields]) + ")"

            out = f"""
/* {tpe['fn']} */
TRACEPOINT_EVENT(
            {provider},
            {e},
            {TP_ARGS},
            {TP_FIELDS}
)
"""
            outf.write(out)

            tracepoint_probes[e] = f"tracepoint({provider}, {e}{CALL_ARGS})"

        return tracepoint_probes

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a tracepoint template for a header file")
    p.add_argument("hfile", help="C header file")
    p.add_argument("--fake-c-headers", help="Path to pycparser's fake C headers")
    p.add_argument("--cppargsfile", help="File that contains C preprocessor arguments, one per line")

    p.add_argument("tp_recipe_yaml", help="Tracepoint recipe")
    p.add_argument("-o", "--output", help="Output template file", default="/dev/stdout")
    p.add_argument("--oprobes", help="Output probes file")

    args = p.parse_args()

    ig = geninterposer.get_generator_for_header(args.hfile,
                                                args.cppargsfile,
                                                args.fake_c_headers)

    with open(args.tp_recipe_yaml, "r") as f:
        recipe = yaml.safe_load(f)
        tp = generate_tracepoint_template(recipe, args.output, ig)
        if args.oprobes:
            with open(args.oprobes, "w") as opf:
                yaml.dump(tp, opf)
