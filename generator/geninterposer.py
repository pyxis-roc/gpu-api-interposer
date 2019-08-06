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

TEMPLATE_INIT_ORIG_HANDLE = """static __attribute__((constructor)) void init_orig_handle() {{
    char *original_library_path = getenv("{env_variable}");

    if(original_library_path == NULL) {{
        fprintf(stderr, "ERROR: Environment variable '{env_variable}' must contain path to original library\\n");
        exit(1);
    }}

    orig_handle = dlopen(original_library_path, RTLD_NOW);

    if(!orig_handle) {{
        fprintf(stderr, "ERROR: Could not load original library (%s)\\n", dlerror());
        exit(1);
    }}
}}

static __attribute__((destructor)) void deinit_orig_handle() {{
  if(orig_handle) {{
    dlclose(orig_handle);
  }}
}}
"""

TEMPLATE_INIT_TRACE_HANDLE = """static __attribute__((constructor)) void init_trace_output() {{
    char *trace_output_path = getenv("{env_variable}");

    if(trace_output_path == NULL) {{
        fprintf(stderr, "ERROR: Environment variable '{env_variable}' must contain output filename for trace\\n");
        exit(1);
    }}

    trace_handle = fopen(trace_output_path, "w");

    if(!trace_handle) {{
        int sverr = errno;
        fprintf(stderr, "ERROR: Could not open trace output '%s' (%d: %s)\\n", trace_output_path, sverr, strerror(sverr));
        exit(1);
    }}
}}

static __attribute__((destructor)) void deinit_trace_handle() {{
  if(trace_handle) {{
    fclose(trace_handle);
  }}
}}
"""


class FuncDeclVisitor(pycparser.c_ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        super(FuncDeclVisitor, self).__init__(*args, **kwargs)

        self.func_decl_nodes = []

    def erase_name(self, decl, level = 0):
        ty = type(decl)

        if ty is c_ast.TypeDecl:
            return ty(None, decl.quals, self.erase_name(decl.type, level + 1))
        elif ty is c_ast.PtrDecl:
            en = ty(decl.quals, self.erase_name(decl.type, level + 1))
            if level == 0:
                return c_ast.Typename(None, [], en)
            else:
                return en
        elif ty is c_ast.IdentifierType:
            return ty(decl.names)
        else:
            assert False, ty

    def decl_to_fnptr(self, func_decl_node):

        # strip names from paramlist
        params = []
        for a in func_decl_node.args:
            ent = self.erase_name(a.type)
            params.append(ent)

        new_type = copy.deepcopy(func_decl_node.type)
        old_name = self.get_declname(new_type)
        self.set_declname(new_type, old_name, old_name + "_orig")

        new_decl = c_ast.FuncDecl(c_ast.ParamList(params), new_type)

        new_fnptr = c_ast.PtrDecl([], new_decl)
        d = c_ast.Decl(old_name + "_orig", [], ['static'], [], new_fnptr, c_ast.ID("NULL"), None)

        return d

    def decl_to_fncall(self, func_decl_node):
        fn = c_ast.ID(self.get_declname(func_decl_node.type) + "_orig")

        #print(func_decl_node.args)

        # warning: func_decl_nodes do not need to have names!
        # typename indicates void
        # TODO: varargs?
        args = [x.name for x in func_decl_node.args if not (type(x) is c_ast.Typename)]

        #assert all(args), args

        return c_ast.FuncCall(fn, c_ast.ExprList([c_ast.ID(a) for a in args]))

    def set_declname(self, ty, old_declname, new_declname):
        if type(ty) is c_ast.PtrDecl:
            return self.set_declname(ty.type, old_declname, new_declname)
        else:
            if ty.declname == old_declname:
                ty.declname = new_declname
                return
            else:
                self.set_declname(ty.type, old_declname, new_declname)
    
    def get_declname(self, ty):
        if type(ty) is c_ast.PtrDecl:
            return self.get_declname(ty.type)
        else:
            return ty.declname

    def get_retval(self, fnptr): 
        retval_type = copy.deepcopy(fnptr.type.type.type)
        retval_decl = c_ast.Decl("_retval", [], [], [], retval_type, None, None)
        self.set_declname(retval_decl.type, fnptr.name, "_retval")

        return retval_decl
        
    def visit_FuncDecl(self, node):
        #print(f'{node.type.declname} at {node.coord}')

        out = {}

        out['origname'] = self.get_declname(node.type)
        out['decl'] = node
        out['fnptr'] = self.decl_to_fnptr(node)
        out['fncall'] = self.decl_to_fncall(node)

        out['retval_decl'] = self.get_retval(out['fnptr'])
        
        self.func_decl_nodes.append(out)

    def visit_Typedef(self, node):
        #print(node)
        return

class InterposerPlugin(object):
    def __init__(self, generator):
        self.generator = generator

    def generate_includes(self):
        """Generate code to be placed at top of generated file, must be list of strings"""
        return []

    def generate_pre_code(self):
        """Generate code before all API functions generated, must be list of strings"""
        return []

    def generate_post_code(self):
        """Generate code after all API functions generated, must be list of strings"""
        return []
        
    def generate(self, decl_node, context):
        raise NotImplementedError

class ReturnPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        if 'retval' in context:
            return [c_ast.Return(c_ast.ID(context['retval']))]
        else:
            return [c_ast.Return(decl_node['fncall'])]

class ReturnValuePlugin(InterposerPlugin):
    def generate(self, decl_node, context):

        # get the fnptr node
        # PtrDecl -> FuncDecl ->type
        context['retval'] = decl_node['retval_decl'].name
        return [decl_node['retval_decl'],
                c_ast.Assignment("=", c_ast.ID(context['retval']),
                                 decl_node['fncall'])]

class DefaultHeadersPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        # this doesn't generate anything.
        return []

    def generate_includes(self):
        return ["#include <stddef.h>"]

class StdDLPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        # this doesn't generate anything.
        return []

    def generate_includes(self):
        return ["#define _GNU_SOURCE", # for RTLD_NEXT
                "#include <dlfcn.h>"]
    
class DLOpenPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        # this doesn't generate anything.
        return []

    def generate_includes(self):
        return ["#include <dlfcn.h>",
                "#include <stdio.h>",
                "#include <stdlib.h>"]
    
    def generate_pre_code(self):
        """Generate code before all API functions generated, must be list of strings"""
        return ["static void * orig_handle;\n"]

    def generate_post_code(self):
        """Generate code before all API functions generated, must be list of strings"""
        return [TEMPLATE_INIT_ORIG_HANDLE.format(env_variable = 'DLOPEN_LIBRARY')]
    
    
class TracePlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        return [c_ast.FuncCall(c_ast.ID("fprintf"),
                               c_ast.ExprList([c_ast.ID("trace_handle"), 
                                               c_ast.Constant("string",
                                                              '"%s\\n"' % (decl_node['origname'],))]
                               ))]

    def generate_includes(self):
        return ["#include <stdio.h>",
                "#include <stdlib.h>",
                "#include <errno.h>"]

    def generate_pre_code(self):
        """Generate code before all API functions generated, must be list of strings"""
        return ["static FILE * trace_handle;\n"]

    def generate_post_code(self):
        """Generate code before all API functions generated, must be list of strings"""
        return [TEMPLATE_INIT_TRACE_HANDLE.format(env_variable = 'TRACE_OUTPUT')]

    
class InterposerGenerator(object):
    def __init__(self, hfile, ast):
        self.hfile = hfile
        self.hinclude = os.path.basename(hfile)
        self.ast = ast

        self.fdv = FuncDeclVisitor()
        self.fdv.visit(self.ast)
        self.dlopen = False
        self.plugins = []
        self.add_plugin(DefaultHeadersPlugin)
        
    def add_plugin(self, plugin):
        # TODO: automate ordering later...
        self.plugins.append(plugin(self))
        
    def generate_shells(self):
        def next_func_code(node_data):
            varname = c_ast.ID(node_data['fnptr'].name)

            if args.dlopen:
                handle = c_ast.ID("orig_handle")
            else:
                handle = c_ast.ID("RTLD_NEXT")

            a = c_ast.Assignment("=", varname, 
                             c_ast.FuncCall(c_ast.ID("dlsym"), 
                                            c_ast.ExprList([
                                                handle,
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

    def generate_plugins(self, decl_node):
        context = {}

        for p in self.plugins:
            l = p.generate(decl_node, context)
            assert isinstance(l, list) # should be iterable, actually...

            for ll in l:
                yield ll

    def generate_plugin_includes(self):
        already_generated = set()
        
        for p in self.plugins:
            l = p.generate_includes()
            for ll in l:
                if ll not in already_generated:
                    already_generated.add(ll)
                    yield ll + '\n'
                
    def generate_plugin_pre_code(self):
        for p in self.plugins:
            l = p.generate_pre_code()
            for ll in l:
                yield ll
                
    def generate_plugin_post_code(self):
        for p in self.plugins:
            l = p.generate_post_code()
            for ll in l:
                yield ll
                
    def generate_passthru(self, outputfile):
        with open(outputfile, "w") as f:
            f.write("/* automatically generated */\n")

            for l in self.generate_plugin_includes():
                f.write(l)

            f.write(f"#include <{self.hinclude}>\n")
            f.write("\n")

            for l in self.generate_plugin_pre_code():
                f.write(l)

            f.write("\n")
            
            generator = c_generator.CGenerator()

            for n in self.fdv.func_decl_nodes:
                passthru = copy.deepcopy(n['shell'])

                for l in self.generate_plugins(n):
                    passthru.body.block_items.append(l)
                    
                f.write(generator.visit(passthru) + "\n")

            for l in self.generate_plugin_post_code():
                f.write(l)
    
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
    p.add_argument("--dlopen", action="store_true",
                   help="Original library is dlopen-ed")
    p.add_argument("--trace", action="store_true",
                   help="Generate tracer")

    p.add_argument("-o", dest="output", help="Output file")

    args = p.parse_args()

    preprocessed = preprocess(args.hfile, args.cppargsfile, args.fake_c_headers)
    ast = get_ast(preprocessed)
    
    ig = InterposerGenerator(args.hfile, ast)

    ig.dlopen = args.dlopen    
    if args.dlopen:
        ig.add_plugin(DLOpenPlugin)
    else:
        ig.add_plugin(StdDLPlugin)

    if args.trace:
        ig.add_plugin(TracePlugin)

    ig.add_plugin(ReturnValuePlugin)

    ig.add_plugin(ReturnPlugin)

    ig.generate_shells()

    if not args.output:
        args.output = "/dev/stdout"

    ig.generate_passthru(args.output)
