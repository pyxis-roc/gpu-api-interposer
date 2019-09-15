#-----------------------------------------------------------------
# ** ATTENTION **
# This code was automatically generated from the file:
# _ptx_ast.cfg
#
# Do not modify it directly. Modify the configuration file and
# run the generator again.
# ** ** *** ** **
#
# ptxparser: ptx_ast.py
#
# AST Node classes for CUDA PTX.
#
# (Originally based on c_ast.py by Eli Bendersky [https://eli.thegreenplace.net/])
# License: BSD
#
# Sreepathi Pai
#-----------------------------------------------------------------


import sys

def _repr(obj):
    """
    Get the representation of an object, with dedicated pprint-like format for lists.
    """
    if isinstance(obj, list):
        return '[' + (',\n '.join((_repr(e).replace('\n', '\n ') for e in obj))) + '\n]'
    else:
        return repr(obj) 

class Node(object):
    __slots__ = ()
    """ Abstract base class for AST nodes.
    """
    def __repr__(self):
        """ Generates a python representation of the current node
        """
        result = self.__class__.__name__ + '('
        
        indent = ''
        separator = ''
        for name in self.__slots__[:-2]:
            result += separator
            result += indent
            result += name + '=' + (_repr(getattr(self, name)).replace('\n', '\n  ' + (' ' * (len(name) + len(self.__class__.__name__)))))
            
            separator = ','
            indent = '\n ' + (' ' * len(self.__class__.__name__))
        
        result += indent + ')'
        
        return result

    def children(self):
        """ A sequence of all children that are Nodes
        """
        pass

    def show(self, buf=sys.stdout, offset=0, attrnames=False, nodenames=False, showcoord=False, _my_node_name=None):
        """ Pretty print the Node and all its attributes and
            children (recursively) to a buffer.

            buf:
                Open IO buffer into which the Node is printed.

            offset:
                Initial offset (amount of leading spaces)

            attrnames:
                True if you want to see the attribute names in
                name=value pairs. False to only see the values.

            nodenames:
                True if you want to see the actual node names
                within their parents.

            showcoord:
                Do you want the coordinates of each Node to be
                displayed.
        """
        lead = ' ' * offset
        if nodenames and _my_node_name is not None:
            buf.write(lead + self.__class__.__name__+ ' <' + _my_node_name + '>: ')
        else:
            buf.write(lead + self.__class__.__name__+ ': ')

        if self.attr_names:
            if attrnames:
                nvlist = [(n, getattr(self,n)) for n in self.attr_names]
                attrstr = ', '.join('%s=%s' % nv for nv in nvlist)
            else:
                vlist = [getattr(self, n) for n in self.attr_names]
                attrstr = ', '.join('%s' % v for v in vlist)
            buf.write(attrstr)

        if showcoord:
            buf.write(' (at %s)' % self.coord)
        buf.write('\n')

        for (child_name, child) in self.children():
            child.show(
                buf,
                offset=offset + 2,
                attrnames=attrnames,
                nodenames=nodenames,
                showcoord=showcoord,
                _my_node_name=child_name)


class NodeVisitor(object):
    """ A base NodeVisitor class for visiting ptx_ast nodes.
        Subclass it and define your own visit_XXX methods, where
        XXX is the class name you want to visit with these
        methods.

        For example:

        class ConstantVisitor(NodeVisitor):
            def __init__(self):
                self.values = []

            def visit_Constant(self, node):
                self.values.append(node.value)

        Creates a list of values of all the constant nodes
        encountered below the given node. To use it:

        cv = ConstantVisitor()
        cv.visit(node)

        Notes:

        *   generic_visit() will be called for AST nodes for which
            no visit_XXX method was defined.
        *   The children of nodes for which a visit_XXX was
            defined will not be visited - if you need this, call
            generic_visit() on the node.
            You can use:
                NodeVisitor.generic_visit(self, node)
        *   Modeled after Python's own AST visiting facilities
            (the ast module of Python 3.0)
    """

    _method_cache = None

    def visit(self, node):
        """ Visit a node.
        """

        if self._method_cache is None:
            self._method_cache = {}

        visitor = self._method_cache.get(node.__class__.__name__, None)
        if visitor is None:
            method = 'visit_' + node.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            self._method_cache[node.__class__.__name__] = visitor

        return visitor(node)

    def generic_visit(self, node):
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """
        for c in node:
            self.visit(c)

class Ptx(Node):
    __slots__ = ('version', 'target', 'address_size', 'statements', 'coord', '__weakref__')
    def __init__(self, version, target, address_size, statements, coord=None):
        self.version = version
        self.target = target
        self.address_size = address_size
        self.statements = statements
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.statements or []):
            nodelist.append(("statements[%d]" % i, child))
        return tuple(nodelist)

    def __iter__(self):
        for child in (self.statements or []):
            yield child

    attr_names = ('version', 'target', 'address_size', )

class Label(Node):
    __slots__ = ('name', 'stmt', 'coord', '__weakref__')
    def __init__(self, name, stmt, coord=None):
        self.name = name
        self.stmt = stmt
        self.coord = coord

    def children(self):
        nodelist = []
        if self.stmt is not None: nodelist.append(("stmt", self.stmt))
        return tuple(nodelist)

    def __iter__(self):
        if self.stmt is not None:
            yield self.stmt

    attr_names = ('name', )

class LinkingDirective(Node):
    __slots__ = ('directive', 'coord', '__weakref__')
    def __init__(self, directive, coord=None):
        self.directive = directive
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    def __iter__(self):
        return
        yield

    attr_names = ('directive', )

class Entry(Node):
    __slots__ = ('linking', 'kernel_name', 'param_list', 'performance_tuning', 'kernel_body', 'coord', '__weakref__')
    def __init__(self, linking, kernel_name, param_list, performance_tuning, kernel_body, coord=None):
        self.linking = linking
        self.kernel_name = kernel_name
        self.param_list = param_list
        self.performance_tuning = performance_tuning
        self.kernel_body = kernel_body
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.param_list or []):
            nodelist.append(("param_list[%d]" % i, child))
        for i, child in enumerate(self.kernel_body or []):
            nodelist.append(("kernel_body[%d]" % i, child))
        return tuple(nodelist)

    def __iter__(self):
        for child in (self.param_list or []):
            yield child
        for child in (self.kernel_body or []):
            yield child

    attr_names = ('linking', 'kernel_name', 'performance_tuning', )

class EntryParam(Node):
    __slots__ = ('space', 'align', 'param_type', 'name', 'array_spec', 'name2', 'param_type2', 'align2', 'array_spec2', 'coord', '__weakref__')
    def __init__(self, space, align, param_type, name, array_spec, name2, param_type2, align2, array_spec2, coord=None):
        self.space = space
        self.align = align
        self.param_type = param_type
        self.name = name
        self.array_spec = array_spec
        self.name2 = name2
        self.param_type2 = param_type2
        self.align2 = align2
        self.array_spec2 = array_spec2
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    def __iter__(self):
        return
        yield

    attr_names = ('space', 'align', 'param_type', 'name', 'array_spec', 'name2', 'param_type2', 'align2', 'array_spec2', )

class IdentifierDecl(Node):
    __slots__ = ('space', 'align', 'variable_declarator', 'coord', '__weakref__')
    def __init__(self, space, align, variable_declarator, coord=None):
        self.space = space
        self.align = align
        self.variable_declarator = variable_declarator
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.variable_declarator or []):
            nodelist.append(("variable_declarator[%d]" % i, child))
        return tuple(nodelist)

    def __iter__(self):
        for child in (self.variable_declarator or []):
            yield child

    attr_names = ('space', 'align', )

