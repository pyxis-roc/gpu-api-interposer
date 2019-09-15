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

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, ParseTreeVisitor
if __name__ == "__main__":
    from PtxParser import PtxParser
    from PtxLexer import PtxLexer
    from PtxListener import PtxListener
    from PtxVisitor import PtxVisitor

    import ptx_ast as pa
else:
    from .PtxParser import PtxParser
    from .PtxLexer import PtxLexer
    from .PtxListener import PtxListener
    from .PtxVisitor import PtxVisitor

    from . import ptx_ast as pa

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

class ASTBuilderVisitor(PtxVisitor):
    ptx = None

    def visitProg(self, ctx:PtxParser.ProgContext):
        v = self.visitVersion(ctx.version())
        t = self.visitTarget(ctx.target())
        a = self.visitAddress_size(ctx.address_size())
        stmts = [self.visitStatement(s) for s in ctx.statement()]

        self.ptx = pa.Ptx(v, t, a, stmts)

    def visitVersion(self, ctx:PtxParser.VersionContext):
        v = ctx.float_().T_FLT_LITERAL() #TODO: this is not really a float

        v = int(float(v.getText()) * 10)
        return (v // 10, v % 10)

    def visitAddress_size(self, ctx:PtxParser.Address_sizeContext):
        return int(ctx.integer().getText())

    def visitTarget(self, ctx:PtxParser.TargetContext):
        # TODO: change this to integer 35, 52, etc.
        return [x.getText() for x in ctx.target_list().T_WORD()]

    def visitStatement(self, ctx:PtxParser.StatementContext):
        return self.visitChildren(ctx)

    def visitLabel_decl(self, ctx:PtxParser.Label_declContext):
        return Label(ctx.T_WORD(), None) # patch up later

    def visitEntry_aux(self, ctx:PtxParser.Entry_auxContext):
        ld =  ctx.K_VISIBLE() or ctx.K_EXTERN()

        if ld:
            ld = pa.LinkingDirective(ld.getText())

        pl = self.visitEntry_param_list(ctx.entry_param_list())
        pt = None #ctx.performance_tuning_directives()
        eb = self.visitEntry_body(ctx.entry_body())

        return pa.Entry(ld, ctx.kernel_name().getText(), pl, pt, eb)

    def visitEntry_param_list(self, ctx:PtxParser.Entry_param_listContext):
        return [self.visitEntry_param(x) for x in ctx.entry_param()]

    def visitEntry_param(self, ctx:PtxParser.Entry_paramContext):
        assert len(ctx.T_WORD()) == 1 # TODO: what syntax is this?

        return pa.EntryParam(ctx.entry_space().getText(),
                             ctx.align()[0].getText() if ctx.align() else None,
                             ctx.entry_param_type()[0].getText(),
                             ctx.T_WORD()[0].getText(),
                             self.visitArray_spec(ctx.array_spec()[0]) if ctx.array_spec() else None,
                             None,
                             None,
                             None,
                             None)

    def visitEntry_body(self, ctx:PtxParser.Entry_bodyContext):
        return [self.visitStatement(s) for s in ctx.statement() if ctx.statement() is not None]

    def visitInstruction(self, ctx:PtxParser.InstructionContext):
        return self.visitChildren(ctx)

    def visitIdentifier_decl_aux(self, ctx:PtxParser.Identifier_declContext):
        space = self.visit(ctx.children[0])
        align = self.visitAlign(ctx.align()) if ctx.align() else None

        vd = ctx.variable_declarator_list() or ctx.variable_declarator_list_with_initializer()
        vdl = self.visit(vd)

        return pa.IdentifierDecl(space, align, vdl)

    # Visit a parse tree produced by PtxParser#variable_declarator.
    def visitVariable_declarator(self, ctx:PtxParser.Variable_declaratorContext):
        print(ctx.id_or_opcode().getText())
        return self.visitChildren(ctx)



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


    #walker = ParseTreeWalker()
    #ab = ASTBuilderListener()

    ab = ASTBuilderVisitor()

    ab.visit(tree)

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
