#!/usr/bin/env python3
#
# parser.py
#
# PTX Parser, uses ANTLR4 to parse PTX files, and create an AST
#
#
# Author: Sreepathi Pai
# Author: Amr Elhelw
#
# Copyright (C) 2019, University of Rochester
#
# Note: ANTLR Grammar source is:  (used under Apache license)
# Modifications to ANTLR Grammar by Amr
# Other code from pycparse, by Eli Bendersky (used under BSD license)

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from PtxParser import PtxParser
from PtxLexer import PtxLexer
from PtxListener import PtxListener

import ptx_ast as pa

class Stack(object):
    stk = None
    def __init__(self):
        self.stk = []

    def push(self, o):
        self.stk.append(o)

    def pop(self):
        return self.stk.pop()

    @property
    def top(self):
        return self.stk[-1]

    def is_empty(self):
        return len(self.stk) == 0

# would've preferred visitor, but using Listener for now.
class ASTBuilderListener(PtxListener):
    ptx = None
    stmt_stack = None

    def __init__(self, *args, **kwargs):
        # super init?
        self.stmt_stack = Stack()
        pass

    def enterProg(self, ctx:PtxParser.ProgContext):
        self.ptx = pa.Ptx(None, None, None, None)
        self.stmt_stack.push(self.ptx)

    def exitProg(self, ctx:PtxParser.ProgContext):
        assert self.stmt_stack.top == self.ptx
        self.stmt_stack.pop()

    def enterVersion(self, ctx:PtxParser.VersionContext):
        v = ctx.float_().T_FLT_LITERAL() #TODO: this is not really a float

        v = int(float(v.getText()) * 10)
        self.ptx.version = (v // 10, v % 10)

    def enterTarget(self, ctx:PtxParser.ProgContext):
        self.ptx.target = []

        for x in ctx.target_list().T_WORD():
            # TODO: change this to integer 35, 52, etc.
            self.ptx.target.append(x.getText())

    def enterAddress_size(self, ctx:PtxParser.Address_sizeContext):
        self.ptx.address_size = int(ctx.integer().getText())

def parse_buffer(data):
    input_stream = InputStream(data)

    lexer = PtxLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    parser = PtxParser(tokens)
    tree = parser.prog()

    walker = ParseTreeWalker()
    ab = ASTBuilderListener()

    walker.walk(ab, tree)

    return ab.ptx

def parse_file(filename):
    with open(filename, "rb") as f:
        data = f.read().decode('ascii') # 4.1: Source modules are ASCII text

        return parse_buffer(data)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Parse a PTX file")

    p.add_argument("ptx")

    args = p.parse_args()

    ast = parse_file(args.ptx)
    print(ast)
