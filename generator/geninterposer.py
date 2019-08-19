#!/usr/bin/env python3
#
# geninterposer.py
#
# Generate a C file suitable for LD_PRELOAD for a given header file.
#
# Author: Sreepathi Pai
#
# Copyright (C) 2019, The University of Rochester
#

import sys
import argparse
import pycparser
from pycparser import c_ast, c_generator
import subprocess
import tempfile
import os
import logging
import copy
import yaml
import difflib
import itertools

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

def is_void_type(ty):
    return type(ty) is c_ast.TypeDecl and type(ty.type) is c_ast.IdentifierType \
        and (len(ty.type.names) == 1) and (ty.type.names[0] == 'void')

class FuncDeclVisitor(pycparser.c_ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        super(FuncDeclVisitor, self).__init__(*args, **kwargs)

        self.func_decl_nodes = []

    @staticmethod
    def erase_name(decl, level = 0):
        ty = type(decl)

        if ty is c_ast.TypeDecl:
            return ty(None, decl.quals, FuncDeclVisitor.erase_name(decl.type, level + 1))
        elif ty is c_ast.PtrDecl:
            en = ty(decl.quals, FuncDeclVisitor.erase_name(decl.type, level + 1))
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
        for a in func_decl_node.args.params:
            ent = FuncDeclVisitor.erase_name(a.type)
            params.append(ent)

        new_type = copy.deepcopy(func_decl_node.type)
        old_name = FuncDeclVisitor.get_declname(new_type)
        self.set_declname(new_type, old_name, old_name + "_orig")

        new_decl = c_ast.FuncDecl(c_ast.ParamList(params), new_type)

        new_fnptr = c_ast.PtrDecl([], new_decl)
        d = c_ast.Decl(old_name + "_orig", [], ['static'], [], new_fnptr, c_ast.ID("NULL"), None)

        return d

    def decl_to_fncall(self, func_decl_node):
        fn = c_ast.ID(FuncDeclVisitor.get_declname(func_decl_node.type) + "_orig")

        #print(func_decl_node.args)

        # warning: func_decl_nodes do not need to have names!
        # typename indicates void
        # TODO: varargs?
        args = [x.name for x in func_decl_node.args.params if not (type(x) is c_ast.Typename)]

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

    @staticmethod
    def get_declname(ty):
        if type(ty) is c_ast.PtrDecl:
            return FuncDeclVisitor.get_declname(ty.type)
        else:
            return ty.declname

    def get_retval(self, fnptr): 
        retval_type = copy.deepcopy(fnptr.type.type.type)

        if is_void_type(retval_type):
            return None
        
        retval_decl = c_ast.Decl("_retval", [], [], [], retval_type, None, None)
        self.set_declname(retval_decl.type, fnptr.name, "_retval")

        return retval_decl
        
    def visit_FuncDecl(self, node):
        #print(f'{node.type.declname} at {node.coord}')

        out = {}

        out['origname'] = FuncDeclVisitor.get_declname(node.type)
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

    def generate_includes(self, context):
        """Generate code to be placed at top of generated file, must be list of strings"""
        return []

    def generate_pre_code(self, context):
        """Generate code before all API functions generated, must be list of strings"""
        return []

    def generate_post_code(self, context):
        """Generate code after all API functions generated, must be list of strings"""
        return []
        
    def generate(self, decl_node, context):
        raise NotImplementedError

class ReturnPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        if decl_node['retval_decl']:
            if 'retval' in context:
                return [c_ast.Return(c_ast.ID(context['retval']))]
            else:
                assert 'called' not in context or not context['called'], "Can't have called function with no retval"
                return [c_ast.Return(decl_node['fncall'])]
        else:
            if 'called' not in context:
                # function with no return value, but may already have been called
                context['called'] = True
                return [decl_node['fncall']]

        return []

class ReturnValuePlugin(InterposerPlugin):
    def generate(self, decl_node, context):

        # get the fnptr node
        # PtrDecl -> FuncDecl ->type

        context['called'] = True

        if decl_node['retval_decl']:
            context['retval'] = decl_node['retval_decl'].name
            return [c_ast.Assignment("=", c_ast.ID(context['retval']),
                                     decl_node['fncall'])]
        else:
            return [decl_node['fncall']]

class DefaultHeadersPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        # this doesn't generate anything.
        return []

    def generate_includes(self, context):
        return ["#include <stddef.h>"]

class StdDLPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        # this doesn't generate anything.
        return []

    def generate_includes(self, context):
        return ["#define _GNU_SOURCE", # for RTLD_NEXT
                "#include <dlfcn.h>"]
    
class DLOpenPlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        # this doesn't generate anything.
        return []

    def generate_includes(self, context):
        return ["#include <dlfcn.h>",
                "#include <stdio.h>",
                "#include <stdlib.h>"]
    
    def generate_pre_code(self, context):
        """Generate code before all API functions generated, must be list of strings"""
        return ["static void * orig_handle;\n"]

    def generate_post_code(self, context):
        """Generate code before all API functions generated, must be list of strings"""
        return [TEMPLATE_INIT_ORIG_HANDLE.format(env_variable = 'DLOPEN_LIBRARY')]
    
    
class TracePlugin(InterposerPlugin):
    def generate(self, decl_node, context):
        return [c_ast.FuncCall(c_ast.ID("fprintf"),
                               c_ast.ExprList([c_ast.ID("trace_handle"), 
                                               c_ast.Constant("string",
                                                              '"%s\\n"' % (decl_node['origname'],))]
                               ))]

    def generate_includes(self, context):
        return ["#include <stdio.h>",
                "#include <stdlib.h>",
                "#include <errno.h>",
                "#include <string.h>"]

    def generate_pre_code(self, context):
        """Generate code before all API functions generated, must be list of strings"""
        return ["static FILE * trace_handle;\n"]

    def generate_post_code(self, context):
        """Generate code before all API functions generated, must be list of strings"""
        return [TEMPLATE_INIT_TRACE_HANDLE.format(env_variable = 'TRACE_OUTPUT')]

class CommonInstrumentMixin(object):
    def get_ctx_arg_type(self):
        return c_ast.Decl('_ctx', [], [], [],
                          c_ast.PtrDecl([],
                                        c_ast.TypeDecl("_ctx", [],
                                                       c_ast.IdentifierType(['void']))), None, None)

    def _generate_instr_decl(self, decl_node, new_ret_type):
        new_decl_node = copy.deepcopy(decl_node['decl'])
        ret_ty = c_ast.TypeDecl(decl_node['origname'] + self.fn_suffix, [],
                                c_ast.IdentifierType([new_ret_type]))

        new_decl_node.type = ret_ty

        if len(new_decl_node.args.params) == 1 and is_void_type(new_decl_node.args.params[0].type):
            new_decl_node.args.params = []

        if decl_node['retval_decl']:
            retval_arg_type = c_ast.Decl('_retval', [], [], [],
                                         c_ast.PtrDecl([],
                                                       copy.deepcopy(decl_node['retval_decl'].type)),
                                         None, None)

            new_decl_node.args.params.append(retval_arg_type)

        
        new_decl_node.args.params.append(self.get_ctx_arg_type())
        return new_decl_node

    def generate_includes(self, context):
        return ['#include "%s"' % (self.hfile,)]

    def generate_post_code(self, context):
        with open(self.hfile, "w") as f:
            f.write("/* automatically generated, do not edit */\n")
            f.write(f"#include <{self.generator.hinclude}>\n")

            f.write("#ifdef __cplusplus\n")
            f.write('extern "C" {\n')
            f.write("#endif\n")                    
            
            cgen = c_generator.CGenerator()
            f.write(cgen.visit(self.ast))

            f.write("#ifdef __cplusplus\n")
            f.write('}\n')
            f.write("#endif\n")                    
            
        return []

    def _add_to_context(self, context, section, hookfn, origname, instr_decl):
        if section not in context:
            context[section] = {}

        context[section][hookfn] = {'origname': origname,
                                    'instr_decl': instr_decl}

class CtxPlugin(InterposerPlugin):
    filter_section_name = ["pre", "pre_and_post", "post"]
    ctx_global_variable = "_ctx_order"
    ctx_local_variable = "_ctx"

    def generate_pre_code(self, context):
        """Generate code before all API functions generated, must be list of strings"""
        return [f"static unsigned int {self.ctx_global_variable};\n"]

    def generate(self, decl_node, context):
        ctx_init = c_ast.FuncCall(c_ast.ID("__sync_fetch_and_add"),
                                  c_ast.ExprList([c_ast.UnaryOp("&", 
                                                                c_ast.ID(self.ctx_global_variable)), 
                                                  c_ast.Constant("int", "1")]))

        ctx_type = c_ast.TypeDecl(self.ctx_local_variable,
                                  [], c_ast.IdentifierType(['unsigned', 'int']))

        x = c_ast.Decl(self.ctx_local_variable, [], [], [], ctx_type, ctx_init, None)
        context['ctx_expr'] = c_ast.UnaryOp("&", c_ast.ID(self.ctx_local_variable))

        #print(c_generator.CGenerator().visit(x))        
        return [x]
    
class PreInstrumentPlugin(CommonInstrumentMixin, InterposerPlugin):
    fn_suffix = "_pre"
    filter_section_name = ["pre", "pre_and_post"]
    
    def __init__(self, *args, **kwargs):
        super(PreInstrumentPlugin, self).__init__(*args, **kwargs)

        self.hfile = (self.generator.oprefix or self.generator.hinclude[:-2]) + "_pre_instr.h"
        self.ast = c_ast.FileAST([])

    def generate(self, decl_node, context):
        prehookfn = decl_node['origname'] + self.fn_suffix
        args = copy.deepcopy(decl_node['fncall'].args)

        if decl_node['retval_decl']:
            args.exprs.append(c_ast.UnaryOp("&", c_ast.ID(decl_node['retval_decl'].name)))
            return_stmt = c_ast.Return(c_ast.ID(decl_node['retval_decl'].name))
        else:
            return_stmt = c_ast.Return(None)

        args.exprs.append(context['ctx_expr'])
        #else:
        #    args.exprs.append(c_ast.ID("NULL")) # TODO: add support for context type

        idecl = self._generate_instr_decl(decl_node, 'int')

        self.ast.ext.append(idecl)
        self._add_to_context(self.generator.global_ctx, "pre", prehookfn,
                             decl_node['origname'], idecl)
                             
        # TODO: post- and pre- context variable
        return [c_ast.If(c_ast.FuncCall(c_ast.ID(prehookfn), args),
                         c_ast.Compound([return_stmt]),
                         None)]
    

class PostInstrumentPlugin(CommonInstrumentMixin, InterposerPlugin):
    fn_suffix = "_post"
    filter_section_name = ["post", "pre_and_post"]

    def __init__(self, *args, **kwargs):
        super(PostInstrumentPlugin, self).__init__(*args, **kwargs)

        self.hfile = (self.generator.oprefix or self.generator.hinclude[:-2]) + "_post_instr.h"
        self.ast = c_ast.FileAST([])
        
    def generate(self, decl_node, context):
        posthookfn = decl_node['origname'] + self.fn_suffix
        args = copy.deepcopy(decl_node['fncall'].args)

        if decl_node['retval_decl']:
            assert 'retval' in context, "PostInstrumentPlugin requires return value"
            args.exprs.append(c_ast.UnaryOp("&", c_ast.ID(context['retval'])))

        args.exprs.append(context['ctx_expr'])
        #args.exprs.append(c_ast.ID("NULL")) # TODO: add support for context type

        idecl = self._generate_instr_decl(decl_node, 'void')        
        self.ast.ext.append(idecl)
        self._add_to_context(self.generator.global_ctx, "post",
                             posthookfn, decl_node['origname'], idecl)
        
        # TODO: post- and pre- context variable
        return [c_ast.FuncCall(c_ast.ID(posthookfn), 
                             args)]

class TpEventArgGeneratorPlugin(InterposerPlugin):
    def __init__(self, *args, **kwargs):
        super(TpEventArgGeneratorPlugin, self).__init__(*args, **kwargs)

        self.tpargfile = (self.generator.oprefix or self.generator.hinclude[:-2]) + "_tpargs.yaml"

    def generate(self, decl_node, context):
        return []

    def generate_post_code(self, context):
        fns = itertools.chain(self.generator.global_ctx['pre'].keys(),
                              self.generator.global_ctx['post'].keys())
        
        decls = dict([(d['origname'], d) for d in self.generator.get_decl_nodes()])

        out = {}
        cgen = c_generator.CGenerator()
        for f in fns:
            fd = self.generator.global_ctx['pre'].get(f, None) or self.generator.global_ctx['post'][f]

            out[f] = {'fn': fd['origname'],
                      'args': []}

            origdecl = decls[fd['origname']]

            if not (len(origdecl['decl'].args.params) == 1 and is_void_type(origdecl['decl'].args.params[0].type)):
                for noname, withname in zip(origdecl['fnptr'].type.type.args.params,
                             fd['instr_decl'].args.params):

                    argtype = cgen.visit(noname)
                    argname = FuncDeclVisitor.get_declname(withname.type)
                    x = {argname: {'type': argtype}}
                    out[f]['args'].append(x)

            # add _retval and _ctx
            if len(origdecl['decl'].args.params) == 1 and is_void_type(origdecl['decl'].args.params[0].type):
                instr_args = fd['instr_decl'].args.params[:]
            else:
                instr_args = fd['instr_decl'].args.params[len(origdecl['decl'].args.params):]

            if f not in self.generator.global_ctx['post']:
                instr_args = instr_args[1:] # skip _retval

            for arg in instr_args:
                argtype = cgen.visit(FuncDeclVisitor.erase_name(arg.type))
                argname = FuncDeclVisitor.get_declname(arg.type)
                x = {argname: {'type': argtype}}
                out[f]['args'].append(x)
            
        with open(self.tpargfile, "w") as f:
            yaml.dump(out, f)
        
        return []

class InterposerGenerator(object):
    def __init__(self, hfile, ast, oprefix):
        self.hfile = hfile
        self.hinclude = os.path.basename(hfile)
        self.oprefix = oprefix
        self.ast = ast

        self.fdv = FuncDeclVisitor()
        self.fdv.visit(self.ast)
        self.dlopen = False
        self.plugins = []
        self.add_plugin(DefaultHeadersPlugin)
        self.filter_data = None
        self.global_ctx = {}
        
    def get_decl_nodes(self):
        return self.fdv.func_decl_nodes

    def check_filter(self, plugin, function):
        if self.filter_data is not None:
            if hasattr(plugin, "filter_section_name"):
                fsn = plugin.filter_section_name
                if isinstance(fsn, str): fsn = [fsn]

                checks = [function in self.filter_data[s] for s in fsn if s in self.filter_data]
                if len(checks): return any(checks)

        # no section or no filter data means everything gets through ...
        return True

    def add_filter(self, filter_file):
        okay = True

        with open(filter_file, "r") as f:
            self.filter_data = yaml.safe_load(f)

            header_functions = set([x['origname'] for x in self.fdv.func_decl_nodes])

            if 'optional_functions' in self.filter_data:
                optional_functions = set(self.filter_data['optional_functions'])
            else:
                optional_functions = set()
                
            # make it 
            for x in ['pre', 'post', 'pre_and_post']:
                if x not in self.filter_data: 
                    self.filter_data[x] = []
                else:
                    assert isinstance(self.filter_data[x], list), f"Data for {x} is not a list"
                                      
                # TODO: add support for "*"/wildcards
                for fn in self.filter_data[x]:
                    if fn not in header_functions and fn not in optional_functions:
                        closest = " ".join(difflib.get_close_matches(fn, header_functions))

                        print(f"ERROR: Function '{fn}' in {x} filter list does not exist in header [closest: {closest}]", file=sys.stderr)
                        okay = False

        return okay

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
                             None),
                    node_data['retval_decl']]

        for nn in self.fdv.func_decl_nodes:
            n = nn['decl']
            nn['shell'] = pycparser.c_ast.FuncDef(n, None, 
                                                  c_ast.Compound(next_func_code(nn))
                                              )

    def generate_plugins(self, decl_node):
        context = {'called': False, 'ctx_expr': c_ast.ID("NULL")}

        for p in self.plugins:
            if self.check_filter(p, decl_node['origname']):
                l = p.generate(decl_node, context)
                assert isinstance(l, list) # should be iterable, actually...

                for ll in l:
                    yield ll

    def generate_plugin_includes(self):
        already_generated = set()
        context = {}
        
        for p in self.plugins:
            l = p.generate_includes(context)
            for ll in l:
                if ll not in already_generated:
                    already_generated.add(ll)
                    yield ll + '\n'
                
    def generate_plugin_pre_code(self):
        context = {}
        for p in self.plugins:
            l = p.generate_pre_code(context)
            for ll in l:
                yield ll
                
    def generate_plugin_post_code(self):
        context = {}
        for p in self.plugins:
            l = p.generate_post_code(context)
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
    
def preprocess(infile, cpp_args_file = None, fake_c_headers_path = None, addl_headers_path = None):
    h, fn = tempfile.mkstemp(suffix = ".h")
    
    args = [infile, "-o", fn]

    if fake_c_headers_path is not None:
        args.insert(0, "-nostdinc")
        args.insert(0, "-I")
        args.insert(1, fake_c_headers_path)

    if addl_headers_path is not None:
        for x in addl_headers_path:
            args.insert(0, "-I")
            args.insert(1, x)
        
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

def get_generator_for_header(hfile, cppargsfile, fake_c_headers, oprefix = None):
    preprocessed = preprocess(hfile, cppargsfile, fake_c_headers)
    ast = get_ast(preprocessed)
    os.unlink(preprocessed)
    ig = InterposerGenerator(hfile, ast, oprefix)

    return ig

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a interceptor")
    p.add_argument("hfile", help="Include file")
    p.add_argument("--fake-c-headers", help="Path to pycparser's fake C headers")
    p.add_argument("--cppargsfile", help="File that contains C preprocessor arguments, one per line")
    p.add_argument("--dlopen", action="store_true", help="Original library is dlopen-ed")
    p.add_argument("--filter", help="Filter file (YAML)")
    p.add_argument("--ctx", dest="context", action="store_true",
                   help="Generate ordered context variable")
    p.add_argument("--pre-instrument", action="store_true",
                   help="Instrument functions before they've been called, generate a header file for post-call instrumentation functions")
    p.add_argument("--post-instrument", action="store_true",
                   help="Instrument functions after they've been called, generate a header file for post-call instrumentation functions")
    p.add_argument("--trace", action="store_true", help="Generate tracer")
    p.add_argument("--tpargs", action="store_true", help="Generate tracepoint arguments for pre/post functions")    
    p.add_argument("--oprefix", dest="output_prefix", help="Output prefix for supplementary output files")
    p.add_argument("-o", dest="output", help="Output file")

    args = p.parse_args()

    ig = get_generator_for_header(args.hfile, args.cppargsfile, args.fake_c_headers, args.output_prefix)
    if args.filter:
        if not ig.add_filter(args.filter):
            sys.exit(1)
        
    ig.dlopen = args.dlopen    
    if args.dlopen:
        ig.add_plugin(DLOpenPlugin)
    else:
        ig.add_plugin(StdDLPlugin)

    if args.trace:
        ig.add_plugin(TracePlugin)

    if args.context:
        ig.add_plugin(CtxPlugin)

    if args.pre_instrument:
        ig.add_plugin(PreInstrumentPlugin)

    ig.add_plugin(ReturnValuePlugin)
    
    if args.post_instrument:
        ig.add_plugin(PostInstrumentPlugin)

    if args.tpargs:
        if (args.pre_instrument or args.post_instrument):
            ig.add_plugin(TpEventArgGeneratorPlugin)
        else:
            print("ERROR: --tpargs requires --pre and/or --post, ignoring", file=sys.stderr)
            sys.exit(1)
        
    ig.add_plugin(ReturnPlugin)

    ig.generate_shells()

    if not args.output:
        args.output = "/dev/stdout"

    ig.generate_passthru(args.output)
