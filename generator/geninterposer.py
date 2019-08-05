#!/usr/bin/env python3

import sys
import argparse
import pycparser
from pycparser import c_ast, c_generator
import subprocess
import tempfile
import os
import logging
import copy

class FuncDeclVisitor(pycparser.c_ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        super(FuncDeclVisitor, self).__init__(*args, **kwargs)

        self.func_decl_nodes = []

    def erase_name(self, decl):
        ty = type(decl)

        if ty is c_ast.TypeDecl:
            return ty(None, decl.quals, self.erase_name(decl.type))
        elif ty is c_ast.PtrDecl:
            # not sure why typename is required ...
            return c_ast.Typename(None, [], ty(decl.quals, self.erase_name(decl.type)))
        elif ty is c_ast.IdentifierType:
            return ty(decl.names)
        else:
            assert False, ty

    def decl_to_fnptr(self, func_decl_node):

        # strip names from paramlist
        params = []
        for a in func_decl_node.args:
            params.append(self.erase_name(a.type))

        new_type = copy.deepcopy(func_decl_node.type)
        new_type.declname = new_type.declname + "_orig"

        new_decl = c_ast.FuncDecl(c_ast.ParamList(params), new_type)

        new_fnptr = c_ast.PtrDecl([], new_decl)
        d = c_ast.Decl(new_type.declname, [], ['static'], [], new_fnptr, c_ast.ID("NULL"), None)

        return d

    def decl_to_fncall(self, func_decl_node):
        fn = c_ast.ID(func_decl_node.type.declname + "_orig")

        print(func_decl_node.args)

        # warning: func_decl_nodes do not need to have names!
        # typename indicates void
        # TODO: varargs?
        args = [x.name for x in func_decl_node.args if not (type(x) is c_ast.Typename)]

        #assert all(args), args

        return c_ast.FuncCall(fn, c_ast.ExprList([c_ast.ID(a) for a in args]))

    def visit_FuncDecl(self, node):
        print(f'{node.type.declname} at {node.coord}')

        out = {}
        out['origname'] = node.type.declname
        out['decl'] = node
        out['fnptr'] = self.decl_to_fnptr(node)
        out['fncall'] = self.decl_to_fncall(node)
        self.func_decl_nodes.append(out)

class InterposerGenerator(object):
    def __init__(self, hfile, ast):
        self.hfile = hfile
        self.ast = ast

        self.fdv = FuncDeclVisitor()
        self.fdv.visit(self.ast)

    def generate_shells(self):
        def next_func_code(node_data):
            # PtrDecl -> FuncDecl -> actual type -> declname
            varname = c_ast.ID(node_data['fnptr'].type.type.type.declname)

            a = c_ast.Assignment("=", varname, 
                             c_ast.FuncCall(c_ast.ID("dlsym"), 
                                            c_ast.ExprList([
                                                c_ast.ID("RTLD_NEXT"),
                                                c_ast.Constant("string", 
                                                               '"' +f"{node_data['origname']}" + '"')]))
                         )

            return [node_data['fnptr'],
                    c_ast.If(c_ast.UnaryOp('!', varname), 
                             c_ast.Compound([a]),
                             None),]

        for nn in self.fdv.func_decl_nodes:
            n = nn['decl']
            nn['shell'] = pycparser.c_ast.FuncDef(n, None, 
                                                  c_ast.Compound(next_func_code(nn))
                                              )

    def generate_passthru(self):
        generator = c_generator.CGenerator()

        for n in self.fdv.func_decl_nodes:
            passthru = copy.deepcopy(n['shell'])
            passthru.body.block_items.append(c_ast.Return(n['fncall']))

            print(generator.visit(passthru))

    
def preprocess(infile, cpp_args_file = None, fake_c_headers_path = None):
    h, fn = tempfile.mkstemp(suffix = ".h")
    
    args = [infile, "-o", fn]

    if fake_c_headers_path is not None:
        args.insert(0, "-I")
        args.insert(1, fake_c_headers_path)
    
    if cpp_args_file is not None:
        with open(cpp_args_file, "r") as f:
            args = [s.strip() for s in f.readlines() if s[0] != "#"] + args
            args = [a for a in args if len(a)]

    cmd = ["cpp"] + args
    print(cmd)
    logging.info("Running " + " ".join(cmd))

    try:
        p = subprocess.run(cmd, check=True)
    except:
        raise

    os.close(h)
    return fn

def get_ast(preprocessed_file):
    ast = pycparser.parse_file(preprocessed_file)
    return ast

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a interceptor")
    p.add_argument("hfile", help="Include file")
    p.add_argument("--fake-c-headers", help="Path to pycparser's fake C headers")
    p.add_argument("--cppargsfile", help="File that contains C preprocessor arguments, one per line")

    args = p.parse_args()

    preprocessed = preprocess(args.hfile, args.cppargsfile, args.fake_c_headers)
    ast = get_ast(preprocessed)
    ig = InterposerGenerator(args.hfile, ast)
    ig.generate_shells()
    ig.generate_passthru()
