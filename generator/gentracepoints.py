#!/usr/bin/env python3

import argparse
import sys
import yaml
from collections import namedtuple

TP_Arg = namedtuple('tp_arg', ['type', 'name'])
TP_Field = namedtuple('tp_field', ['type', 'fieldname', 'type_args'])

FIELD_FMTS = {
    "ctf_integer": "ctf_integer({int_type}, {fieldname}, {expr})",
    "ctf_integer_hex": "ctf_integer_hex({int_type}, {fieldname}, {expr})"
}

def generate_tracepoint_template(recipe, output):
    provider = recipe['main']['provider']

    with open(output, "w") as outf:
        if 'includes' in recipe:            
            for i in recipe['includes'].get('system', []):
                outf.write(f"#include <{i}>\n")

            for i in recipe['includes'].get('local', []):
                outf.write(f'#include "{i}"\n')

        for e in recipe['tracepoint_events']:
            tpe = recipe['tracepoint_events'][e]
            args = []

            #TODO: allow reading arguments from function and not from recipe
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

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a tracepoint template for a header file")
    p.add_argument("header", help="C header file")
    p.add_argument("tp_recipe_yaml", help="Tracepoint recipe")
    p.add_argument("-o", "--output", help="Output template file")

    args = p.parse_args()

    with open(args.tp_recipe_yaml, "r") as f:
        recipe = yaml.safe_load(f)
        generate_tracepoint_template(recipe, args.output)
