from pycparser import c_ast, c_generator

class PassthruExpr(c_ast.Node):
    __slots__ = ('code', 'coord')

    def __init__(self, code, coord=None):
        self.code = code
        self.coord = coord

class PassthruStmt(c_ast.Node):
    __slots__ = ('code', 'coord')

    def __init__(self, code, coord=None):
        self.code = code
        self.coord = coord

class MyCGenerator(c_generator.CGenerator):
    def visit_PassthruStmt(self, n):
        return n.code

    def visit_PassthruExpr(self, n):
        return n.code
