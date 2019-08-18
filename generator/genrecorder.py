#!/usr/bin/env python3

import argparse
import yaml
import os
from pycparser import c_ast, c_generator
from geninterposer import FuncDeclVisitor, get_ast, preprocess
import sys

BLOBSTORE_XTORS = """
static  __attribute__((constructor)) void init_blobstore() {
   char *blobstore_path = getenv("BLOBSTORE_PATH");

    if(blobstore_path == NULL) {
        fprintf(stderr, "ERROR: Environment variable BLOBSTORE_PATH must be set to point to blobstore file to store blobs.\\n");
        return; // not exiting because trace will still succeed
    }

    if(!bs_create(blobstore_path, &_bs)) {
        fprintf(stderr, "ERROR: Failed to create blobstore '%s'\\n", blobstore_path);
        exit(1);
    }
}

static __attribute__((destructor)) void deinit_blobstore() {
   if(_bs) bs_close(_bs);
}
"""

class PassthruStmt(c_ast.Node):
    __slots__ = ('code', 'coord')

    def __init__(self, code, coord=None):
        self.code = code
        self.coord = coord

class MyCGenerator(c_generator.CGenerator):
    def visit_PassthruStmt(self, n):
        return n.code

def load_yaml(f):
    with open(f, "r") as yf:
        return yaml.safe_load(yf)

def get_func_decls(hfile, cpp_args_file = None, fake_c_headers = None, addl_headers_path = None):
    fn = preprocess(hfile, cpp_args_file, fake_c_headers, addl_headers_path)
    ast = get_ast(fn)

    fdv = FuncDeclVisitor()
    fdv.visit(ast)
    os.unlink(fn)

    return fdv.func_decl_nodes

def get_instr_func_decls(decls, instr_hfiles):
    instr_hfiles = set(instr_hfiles)
    # ignore decls not in instrumentation header files
    out = [fn for fn in decls if fn['decl'].coord.file in instr_hfiles]
    return out

def generate_shells(fdvs, probes, blobstore):
    # only generate recorder for functions that have probes

    def get_bs_store_code(blobstore):
        bscalls = []

        for a in blobstore:
            bsvar = list(a.keys())[0]
            bsargs = a[bsvar]

            callargs = []
            callargs.append(c_ast.ID("_bs"))

            # *(int *)
            ty = c_ast.Typename(None, [], c_ast.PtrDecl([], c_ast.TypeDecl(None, [], c_ast.IdentifierType(['int']))))

            callargs.append(c_ast.UnaryOp("*", c_ast.Cast(ty, c_ast.ID(bsargs[0]))))
            callargs.append(c_ast.Constant("string", '"' + bsvar + '"'))
            callargs.append(c_ast.ID(bsargs[1])) #TODO: this is an expr ....
            callargs.append(c_ast.ID(bsargs[2])) #TODO: this is also an expr ...

            bscalls.append(c_ast.FuncCall(c_ast.ID("bs_store"), c_ast.ExprList(callargs)))

        return [c_ast.If(c_ast.ID("_bs"), c_ast.Compound(bscalls), None)]

    def get_instr_code(f, ev):
        code = []
        args = [c_ast.ID(a) for a in ev['args']]

        if 'pre_tp_code' in ev:
            code.append(PassthruStmt(ev['pre_tp_code']))

        code.append(c_ast.FuncCall(c_ast.ID("tracepoint"), c_ast.ExprList(args)))

        if 'blobstore' in ev:
            if not blobstore:
                print(f"WARNING: {f['origname']} has blobstore, but --blobstore is not present, so no blobstore calls will be generated.")
            else:
                code.extend(get_bs_store_code(ev['blobstore']))

        if f['origname'][-4:] == "_pre":
            code.append(c_ast.Return(c_ast.Constant("int", "0")))
        else:
            if 'post_tp_code' in ev:
                code.append(PassthruStmt(ev['post_tp_code']))

        return code

    fnd = dict([(fn['origname'], fn) for fn in fdvs])
    events = probes['events']
    for ev in events:
        f = fnd[ev]
        #print(f['decl'], events[ev])
        f['shell'] = c_ast.FuncDef(f['decl'], None,
                                   c_ast.Compound(get_instr_code(f, events[ev])))

def generate_output(fdvs, probes, outputfile, instr_headers, blobstore, local_headers, system_headers):
    with open(outputfile, "w") as ofile:
        # write headers

        for ih in instr_headers:
            ofile.write(f'#include "{ih}"\n')

        for h in system_headers:
            ofile.write(f"#include <{h}>\n");

        for h in local_headers:
            ofile.write(f'#include "{h}"\n')

        if blobstore:
            ofile.write("#include <blobstore.h>\n")
            ofile.write("static blobstore _bs = NULL;\n")

        tpheader = probes['output']
        try:
            p = tpheader.rindex(".")
            tpheader = tpheader[:p] + ".h"
        except ValueError:
            tpheader = tpheader + ".h"

        ofile.write(f'#include "{tpheader}"\n')
        cgen = MyCGenerator()

        for f in fdvs:
            if 'shell' not in f:
                # error?
                print(f"WARNING: '{f['origname']}' does not have tracepoints defined.",file=sys.stderr)
            else:
                ofile.write(cgen.visit(f['shell']))

        if blobstore:
            ofile.write(BLOBSTORE_XTORS)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a API recorder given filter file and a probe file")

    p.add_argument("--fake-c-headers", help="Path to pycparser's fake C headers")
    p.add_argument("--cppargsfile", help="File that contains C preprocessor arguments, one per line")
    p.add_argument("--blobstore", action="store_true", help="Support blobstore")
    p.add_argument("-I", dest="include_dirs", action="append", help="Include directories for CPP")
    p.add_argument("-o", dest="output", help="Output C file")
    p.add_argument("--include-local", dest="local_headers", action="append", metavar="HFILE", help="Add HFILE as a local header to output", default=[])
    p.add_argument("--include-system", dest="system_headers", action="append",metavar="HFILE", help="Add HFILE as a system header to output", default=[])
    p.add_argument("tpinfo", help="tpinfo file generated by gentracepoints.py")
    p.add_argument("instr_headers", nargs="+", help="Instrumentation headers generated by --pre and/or --post")

    args = p.parse_args()

    tpinfo = load_yaml(args.tpinfo)

    fdvs = []
    for hfile in args.instr_headers:
        fdecls = get_func_decls(hfile, args.cppargsfile,
                                args.fake_c_headers, args.include_dirs)
        fdvs.extend(get_instr_func_decls(fdecls, args.instr_headers))

    generate_shells(fdvs, tpinfo, args.blobstore)

    if not args.output:
        args.output = "/dev/stdout"

    generate_output(fdvs, tpinfo, args.output, args.instr_headers, args.blobstore, args.local_headers, args.system_headers)
