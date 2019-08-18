#!/usr/bin/env python3

import argparse
import sys
import yaml
from collections import namedtuple
import geninterposer
from pycparser import c_generator

MAX_TP_ARGS = 10
TP_Arg = namedtuple('tp_arg', ['type', 'name'])
TP_Field = namedtuple('tp_field', ['type', 'fieldname', 'type_args'])

FIELD_FMTS = {
    "ctf_integer": "ctf_integer({int_type}, {fieldname}, {expr})",
    "ctf_integer_hex": "ctf_integer_hex({int_type}, {fieldname}, {expr})",
    "ctf_string": "ctf_string({fieldname}, {expr})",
    "ctf_array": "ctf_array({int_type}, {fieldname}, {expr}, {count})",
    "ctf_array_hex": "ctf_array_hex({int_type}, {fieldname}, {expr}, {count})"
}

def merge_tpargs(recipe, tpargs):
    tpe = recipe['tracepoint_events']
    for f in tpargs:
        if f not in tpe:
            continue

        tpfn = tpe[f]
        for k in tpargs[f]:
            if k not in tpfn:
                tpfn[k] = tpargs[f][k]
            else:
                if k == 'args':
                    tpfn[k] = tpfn[k] + tpargs[f][k] # prepend args
                elif k == 'fn':
                    tpfn[k] = tpargs[f][k]
                else:
                    assert False, "Duplicate key '%s' in recipe and tpargs, don't know how to handle" % (k,)

    for f in tpe:
        if "remove_args" in tpe[f]:
            remove_args = set(tpe[f]["remove_args"])
            tpe[f]['args'] = [x for x in tpe[f]['args'] if list(x.keys())[0] not in remove_args]

        if "subst_args" in tpe[f]:
            subst_args = tpe[f]['subst_args']

            out = []
            for a in tpe[f]['args']:
                aname = list(a.keys())[0]
                if aname in subst_args:
                    out.append({subst_args[aname]['with'] : subst_args[aname]})
                else:
                    out.append(a)

            tpe[f]['args'] = out

def generate_tracepoint_template(recipe, output, ig):
    provider = recipe['main']['provider']

    tracepoint_info = {"output": output,
                       "events": {},
                   }
    dn = dict([(x['origname'], x) for x in ig.get_decl_nodes()])
    ALIGN=13

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

            assert 'fields' in tpe, f"No 'fields' for {e}"

            fields = []
            for f in tpe['fields']:
                if isinstance(f, dict):
                    assert len(f) == 1, f'Field dictionary must contain only argname {f}'
                    fieldname = list(f.keys())[0]

                    # yeah, yeah ...
                    name = fieldname if 'fieldname' not in f[fieldname] else f[fieldname]['fieldname']

                    if 'expr' not in f[fieldname]['type_args']:
                        # and field type expects expr?
                        f[fieldname]['type_args']['expr'] = fieldname

                    fields.append(TP_Field(type=f[fieldname]['type'],
                                           fieldname=name,
                                           type_args=f[fieldname]['type_args']))


                else:
                    # TODO: get field types from arg names
                    pass


            if len(args) > MAX_TP_ARGS:
                print(f"WARNING: {e} has more than {MAX_TP_ARGS} arguments to tracepoint, trimming!")

                args = args[:MAX_TP_ARGS]

                # In general, fields has no relation to args, and we
                # will need to identify exprs in each field that
                # depend on a particular arg before removing it.  For
                # now, this will work.
                fields = fields[:MAX_TP_ARGS]

            try:
                sep = ",\n"+(" "*(ALIGN+len("TP_ARGS")))
                TP_ARGS = "TP_ARGS(" + sep.join([f"{a.type}, {a.name}" for a in args]) + ")"

                sep = "\n"+(" "*(ALIGN+len("TP_FIELDS")))
                TP_FIELDS = "TP_FIELDS(" + sep.join([FIELD_FMTS[f.type].format(fieldname=f.fieldname, **f.type_args) for f in fields]) + ")"
            except:
                print(f"ERROR: when processing {e}")
                raise

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

            tracepoint_info['events'][e] = {'args': [provider, e] + [a.name for a in args]}

            if 'blobstore' in tpe:
                bs_specs = []
                for bs_spec in tpe['blobstore']:
                    name = list(bs_spec.keys())[0]
                    expr = name if 'expr' not in bs_spec[name] else bs_spec[name]['expr']
                    length = bs_spec[name]['length']

                    bs_specs.append({name: ["_ctx", expr, length]})

                tracepoint_info['events'][e]['blobstore'] = bs_specs

            # TODO: consolidate all code before and after into "pre" and "post" so genrecorder
            # doesn't have to do much.
            if 'arg_constructors' in tpe:
                tracepoint_info['events'][e]['pre_tp_code'] = tpe['arg_constructors']

            if 'post_code' in tpe:
                tracepoint_info['events'][e]['post_tp_code'] = tpe['post_code']

        return tracepoint_info

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a tracepoint template for a header file")
    p.add_argument("hfile", help="C header file")
    p.add_argument("--fake-c-headers", help="Path to pycparser's fake C headers")
    p.add_argument("--cppargsfile", help="File that contains C preprocessor arguments, one per line")
    p.add_argument("--tpargs", help="File generated by --tpargs of geninterposer.py")
    p.add_argument("tp_recipe_yaml", help="Tracepoint recipe")
    p.add_argument("-o", "--output", help="Output template file", default="/dev/stdout")
    p.add_argument("--tpinfo", help="Output tracepoint info file")

    args = p.parse_args()

    ig = geninterposer.get_generator_for_header(args.hfile,
                                                args.cppargsfile,
                                                args.fake_c_headers)

    tpargs = None
    if args.tpargs:
        with open(args.tpargs, "r") as f:
            tpargs = yaml.safe_load(f)

    with open(args.tp_recipe_yaml, "r") as f:
        recipe = yaml.safe_load(f)
        if tpargs: merge_tpargs(recipe, tpargs)
        tp = generate_tracepoint_template(recipe, args.output, ig)
        if args.tpinfo:
            with open(args.tpinfo, "w") as tpinfo:
                yaml.dump(tp, tpinfo)
