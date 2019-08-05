#!/usr/bin/env python3

import sys
import argparse
import pycparser
import subprocess
import tempfile
import os
import logging

class FuncDeclVisitor(pycparser.c_ast.NodeVisitor):
    def visit_FuncDecl(self, node):
        print(f'{node.type.declname} at {node.coord}')
    

class InterposerGenerator(object):
    def __init__(self, hfile, ast):
        self.hfile = hfile
        self.ast = ast

        self.fdv = FuncDeclVisitor()
        self.fdv.visit(self.ast)
    
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
    
