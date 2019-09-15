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
from collections import namedtuple

if __name__ == "__main__":
    from PtxParser import PtxParser
    from PtxLexer import PtxLexer
    from PtxListener import PtxListener

    import ptx_ast as pa
else:
    from .PtxParser import PtxParser
    from .PtxLexer import PtxLexer
    from .PtxListener import PtxListener

    from . import ptx_ast as pa

ObjStmts = namedtuple('ObjStmts', 'obj stmts')

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
        self.stmts = Stack()
        self._stmt = Stack()

    def enterProg(self, ctx:PtxParser.ProgContext):
        self.ptx = pa.Ptx(None, None, None, None)
        self.stmts.push(ObjStmts(self.ptx, []))

    def exitProg(self, ctx:PtxParser.ProgContext):
        o, stmts = self.stmts.pop()
        assert o is self.ptx

        self.ptx.statements = stmts

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

    # Enter a parse tree produced by PtxParser#label_decl.
    def enterLabel_decl(self, ctx:PtxParser.Label_declContext):
        self._label = ctx.T_WORD().getText()

    def enterStatement(self, ctx:PtxParser.StatementContext):
        self._label = None
        self._stmt.push(None)

    def exitStatement(self, ctx:PtxParser.StatementContext):
        if self._stmt.top:
            if not self._label.is_empty and self._label.top():
                n = pa.Label(self._label, self._stmt)
        else:
            n = self._stmt

        self.stmts.top.stmts.append(n)

        self._stmt = None
        self._label = None

    def enterEntry(self, ctx:PtxParser.EntryContext):
        self._entry = pa.Entry(None, None, None, None, None)

    def enterEntry_aux(self, ctx:PtxParser.Entry_auxContext):
        ld = ctx.K_VISIBLE() or ctx.K_EXTERN()
        if ld:
            self._entry.linking = pa.LinkingDirective(ld.getText())

        self._entry.kernel_name = ctx.kernel_name().getText()
        self.stmts.push(ObjStmts(self._entry, []))

    def exitEntry_aux(self, ctx:PtxParser.Entry_auxContext):
        o, s = self.stmts.pop()
        assert o is self._entry
        o.kernel_body = s

    def exitEntry(self, ctx:PtxParser.EntryContext):
        self._stmt = self._entry

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
