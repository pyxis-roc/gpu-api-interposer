# Generated from Ptx.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PtxParser import PtxParser
else:
    from PtxParser import PtxParser

# This class defines a complete generic visitor for a parse tree produced by PtxParser.

class PtxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PtxParser#prog.
    def visitProg(self, ctx:PtxParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#version.
    def visitVersion(self, ctx:PtxParser.VersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#target.
    def visitTarget(self, ctx:PtxParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#address_size.
    def visitAddress_size(self, ctx:PtxParser.Address_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#target_list.
    def visitTarget_list(self, ctx:PtxParser.Target_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#statement.
    def visitStatement(self, ctx:PtxParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#label_decl.
    def visitLabel_decl(self, ctx:PtxParser.Label_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#semicolon_terminated_statement.
    def visitSemicolon_terminated_statement(self, ctx:PtxParser.Semicolon_terminated_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#unterminated_statement.
    def visitUnterminated_statement(self, ctx:PtxParser.Unterminated_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#semicolon_terminated_directive.
    def visitSemicolon_terminated_directive(self, ctx:PtxParser.Semicolon_terminated_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#unterminated_directive.
    def visitUnterminated_directive(self, ctx:PtxParser.Unterminated_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#entry.
    def visitEntry(self, ctx:PtxParser.EntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#entry_aux.
    def visitEntry_aux(self, ctx:PtxParser.Entry_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#kernel_name.
    def visitKernel_name(self, ctx:PtxParser.Kernel_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#entry_param_list.
    def visitEntry_param_list(self, ctx:PtxParser.Entry_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#entry_param.
    def visitEntry_param(self, ctx:PtxParser.Entry_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#entry_space.
    def visitEntry_space(self, ctx:PtxParser.Entry_spaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#align.
    def visitAlign(self, ctx:PtxParser.AlignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#byte_count.
    def visitByte_count(self, ctx:PtxParser.Byte_countContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#entry_param_type.
    def visitEntry_param_type(self, ctx:PtxParser.Entry_param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#entry_body.
    def visitEntry_body(self, ctx:PtxParser.Entry_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#fundamental_type.
    def visitFundamental_type(self, ctx:PtxParser.Fundamental_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#fundamental_type_aux.
    def visitFundamental_type_aux(self, ctx:PtxParser.Fundamental_type_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#vector_type.
    def visitVector_type(self, ctx:PtxParser.Vector_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#vector_type_aux.
    def visitVector_type_aux(self, ctx:PtxParser.Vector_type_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opaque_type.
    def visitOpaque_type(self, ctx:PtxParser.Opaque_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opaque_type_aux.
    def visitOpaque_type_aux(self, ctx:PtxParser.Opaque_type_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func.
    def visitFunc(self, ctx:PtxParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_aux.
    def visitFunc_aux(self, ctx:PtxParser.Func_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_name.
    def visitFunc_name(self, ctx:PtxParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_ret_list.
    def visitFunc_ret_list(self, ctx:PtxParser.Func_ret_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_ret.
    def visitFunc_ret(self, ctx:PtxParser.Func_retContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_ret_space.
    def visitFunc_ret_space(self, ctx:PtxParser.Func_ret_spaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_ret_type.
    def visitFunc_ret_type(self, ctx:PtxParser.Func_ret_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_param_list.
    def visitFunc_param_list(self, ctx:PtxParser.Func_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_param.
    def visitFunc_param(self, ctx:PtxParser.Func_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_param_space.
    def visitFunc_param_space(self, ctx:PtxParser.Func_param_spaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_param_type.
    def visitFunc_param_type(self, ctx:PtxParser.Func_param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#func_body.
    def visitFunc_body(self, ctx:PtxParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#control_flow_directive.
    def visitControl_flow_directive(self, ctx:PtxParser.Control_flow_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#branch_targets.
    def visitBranch_targets(self, ctx:PtxParser.Branch_targetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#list_of_labels.
    def visitList_of_labels(self, ctx:PtxParser.List_of_labelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#call_targets.
    def visitCall_targets(self, ctx:PtxParser.Call_targetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#call_prototype.
    def visitCall_prototype(self, ctx:PtxParser.Call_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#call_param_list.
    def visitCall_param_list(self, ctx:PtxParser.Call_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#call_param.
    def visitCall_param(self, ctx:PtxParser.Call_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#call_param_space.
    def visitCall_param_space(self, ctx:PtxParser.Call_param_spaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#call_param_type.
    def visitCall_param_type(self, ctx:PtxParser.Call_param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#performance_tuning_directives.
    def visitPerformance_tuning_directives(self, ctx:PtxParser.Performance_tuning_directivesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#performance_tuning_directive.
    def visitPerformance_tuning_directive(self, ctx:PtxParser.Performance_tuning_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#maxnreg.
    def visitMaxnreg(self, ctx:PtxParser.MaxnregContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#maxntid.
    def visitMaxntid(self, ctx:PtxParser.MaxntidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#reqntid.
    def visitReqntid(self, ctx:PtxParser.ReqntidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#minnctapersm.
    def visitMinnctapersm(self, ctx:PtxParser.MinnctapersmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#maxnctapersm.
    def visitMaxnctapersm(self, ctx:PtxParser.MaxnctapersmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#pragma.
    def visitPragma(self, ctx:PtxParser.PragmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#list_of_strings.
    def visitList_of_strings(self, ctx:PtxParser.List_of_stringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#debugging_directive.
    def visitDebugging_directive(self, ctx:PtxParser.Debugging_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#dwarf.
    def visitDwarf(self, ctx:PtxParser.DwarfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#filef.
    def visitFilef(self, ctx:PtxParser.FilefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#section.
    def visitSection(self, ctx:PtxParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#section_name.
    def visitSection_name(self, ctx:PtxParser.Section_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#data_declarator_list.
    def visitData_declarator_list(self, ctx:PtxParser.Data_declarator_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#loc.
    def visitLoc(self, ctx:PtxParser.LocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#linking_directive.
    def visitLinking_directive(self, ctx:PtxParser.Linking_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#extern_.
    def visitExtern_(self, ctx:PtxParser.Extern_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#visible.
    def visitVisible(self, ctx:PtxParser.VisibleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#identifier_decl.
    def visitIdentifier_decl(self, ctx:PtxParser.Identifier_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#identifier_decl_aux.
    def visitIdentifier_decl_aux(self, ctx:PtxParser.Identifier_decl_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#variable_declarator_list.
    def visitVariable_declarator_list(self, ctx:PtxParser.Variable_declarator_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#variable_declarator_list_with_initializer.
    def visitVariable_declarator_list_with_initializer(self, ctx:PtxParser.Variable_declarator_list_with_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#variable_declarator.
    def visitVariable_declarator(self, ctx:PtxParser.Variable_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#array_spec.
    def visitArray_spec(self, ctx:PtxParser.Array_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#array_spec_aux.
    def visitArray_spec_aux(self, ctx:PtxParser.Array_spec_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#parameterized_register_spec.
    def visitParameterized_register_spec(self, ctx:PtxParser.Parameterized_register_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#id_or_opcode.
    def visitId_or_opcode(self, ctx:PtxParser.Id_or_opcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opcode.
    def visitOpcode(self, ctx:PtxParser.OpcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#variable_declarator_with_initializer.
    def visitVariable_declarator_with_initializer(self, ctx:PtxParser.Variable_declarator_with_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#variable_equal_initializer.
    def visitVariable_equal_initializer(self, ctx:PtxParser.Variable_equal_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#variable_initializer.
    def visitVariable_initializer(self, ctx:PtxParser.Variable_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#aggregate_initializer.
    def visitAggregate_initializer(self, ctx:PtxParser.Aggregate_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#typet.
    def visitTypet(self, ctx:PtxParser.TypetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#idi.
    def visitIdi(self, ctx:PtxParser.IdiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#state_space_specifier.
    def visitState_space_specifier(self, ctx:PtxParser.State_space_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#state_space_specifier_aux.
    def visitState_space_specifier_aux(self, ctx:PtxParser.State_space_specifier_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#global_space_specifier.
    def visitGlobal_space_specifier(self, ctx:PtxParser.Global_space_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#const_space_specifier.
    def visitConst_space_specifier(self, ctx:PtxParser.Const_space_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#const_.
    def visitConst_(self, ctx:PtxParser.Const_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#globalg.
    def visitGlobalg(self, ctx:PtxParser.GlobalgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#local.
    def visitLocal(self, ctx:PtxParser.LocalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#param.
    def visitParam(self, ctx:PtxParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#reg.
    def visitReg(self, ctx:PtxParser.RegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#shared.
    def visitShared(self, ctx:PtxParser.SharedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#sreg.
    def visitSreg(self, ctx:PtxParser.SregContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#tex.
    def visitTex(self, ctx:PtxParser.TexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#instruction.
    def visitInstruction(self, ctx:PtxParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#instruction_aux.
    def visitInstruction_aux(self, ctx:PtxParser.Instruction_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#predicate.
    def visitPredicate(self, ctx:PtxParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_abs.
    def visitI_abs(self, ctx:PtxParser.I_absContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_abs_type.
    def visitI_abs_type(self, ctx:PtxParser.I_abs_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_abs_opr.
    def visitI_abs_opr(self, ctx:PtxParser.I_abs_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_add.
    def visitI_add(self, ctx:PtxParser.I_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_add_type.
    def visitI_add_type(self, ctx:PtxParser.I_add_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_add_opr.
    def visitI_add_opr(self, ctx:PtxParser.I_add_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_addc.
    def visitI_addc(self, ctx:PtxParser.I_addcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_addc_type.
    def visitI_addc_type(self, ctx:PtxParser.I_addc_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_addc_opr.
    def visitI_addc_opr(self, ctx:PtxParser.I_addc_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_and.
    def visitI_and(self, ctx:PtxParser.I_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_and_type.
    def visitI_and_type(self, ctx:PtxParser.I_and_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_and_opr.
    def visitI_and_opr(self, ctx:PtxParser.I_and_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_atom.
    def visitI_atom(self, ctx:PtxParser.I_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_atom_type.
    def visitI_atom_type(self, ctx:PtxParser.I_atom_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_atom_opr.
    def visitI_atom_opr(self, ctx:PtxParser.I_atom_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar.
    def visitI_bar(self, ctx:PtxParser.I_barContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar1.
    def visitI_bar1(self, ctx:PtxParser.I_bar1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar1_type.
    def visitI_bar1_type(self, ctx:PtxParser.I_bar1_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar1_opr.
    def visitI_bar1_opr(self, ctx:PtxParser.I_bar1_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar2.
    def visitI_bar2(self, ctx:PtxParser.I_bar2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar2_type.
    def visitI_bar2_type(self, ctx:PtxParser.I_bar2_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar2_opr.
    def visitI_bar2_opr(self, ctx:PtxParser.I_bar2_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar3.
    def visitI_bar3(self, ctx:PtxParser.I_bar3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar3_type.
    def visitI_bar3_type(self, ctx:PtxParser.I_bar3_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar3_opr.
    def visitI_bar3_opr(self, ctx:PtxParser.I_bar3_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar4.
    def visitI_bar4(self, ctx:PtxParser.I_bar4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar4_type.
    def visitI_bar4_type(self, ctx:PtxParser.I_bar4_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bar4_opr.
    def visitI_bar4_opr(self, ctx:PtxParser.I_bar4_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfe.
    def visitI_bfe(self, ctx:PtxParser.I_bfeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfe_type.
    def visitI_bfe_type(self, ctx:PtxParser.I_bfe_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfe_opr.
    def visitI_bfe_opr(self, ctx:PtxParser.I_bfe_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfi.
    def visitI_bfi(self, ctx:PtxParser.I_bfiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfi_type.
    def visitI_bfi_type(self, ctx:PtxParser.I_bfi_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfi_opr.
    def visitI_bfi_opr(self, ctx:PtxParser.I_bfi_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfind.
    def visitI_bfind(self, ctx:PtxParser.I_bfindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfind_type.
    def visitI_bfind_type(self, ctx:PtxParser.I_bfind_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bfind_opr.
    def visitI_bfind_opr(self, ctx:PtxParser.I_bfind_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bra.
    def visitI_bra(self, ctx:PtxParser.I_braContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bra_type.
    def visitI_bra_type(self, ctx:PtxParser.I_bra_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_bra_opr.
    def visitI_bra_opr(self, ctx:PtxParser.I_bra_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_brev.
    def visitI_brev(self, ctx:PtxParser.I_brevContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_brev_type.
    def visitI_brev_type(self, ctx:PtxParser.I_brev_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_brev_opr.
    def visitI_brev_opr(self, ctx:PtxParser.I_brev_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_brkpt.
    def visitI_brkpt(self, ctx:PtxParser.I_brkptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_call.
    def visitI_call(self, ctx:PtxParser.I_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_call_type.
    def visitI_call_type(self, ctx:PtxParser.I_call_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#flist.
    def visitFlist(self, ctx:PtxParser.FlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#fproto.
    def visitFproto(self, ctx:PtxParser.FprotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_clz.
    def visitI_clz(self, ctx:PtxParser.I_clzContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_clz_type.
    def visitI_clz_type(self, ctx:PtxParser.I_clz_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_clz_opr.
    def visitI_clz_opr(self, ctx:PtxParser.I_clz_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cnot.
    def visitI_cnot(self, ctx:PtxParser.I_cnotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cnot_type.
    def visitI_cnot_type(self, ctx:PtxParser.I_cnot_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cnot_opr.
    def visitI_cnot_opr(self, ctx:PtxParser.I_cnot_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_copysign.
    def visitI_copysign(self, ctx:PtxParser.I_copysignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_copysign_type.
    def visitI_copysign_type(self, ctx:PtxParser.I_copysign_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_copysign_opr.
    def visitI_copysign_opr(self, ctx:PtxParser.I_copysign_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cos.
    def visitI_cos(self, ctx:PtxParser.I_cosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cos_type.
    def visitI_cos_type(self, ctx:PtxParser.I_cos_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cos_opr.
    def visitI_cos_opr(self, ctx:PtxParser.I_cos_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvt.
    def visitI_cvt(self, ctx:PtxParser.I_cvtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvt_type.
    def visitI_cvt_type(self, ctx:PtxParser.I_cvt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvt_irnd.
    def visitI_cvt_irnd(self, ctx:PtxParser.I_cvt_irndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvt_irnd_aux.
    def visitI_cvt_irnd_aux(self, ctx:PtxParser.I_cvt_irnd_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvt_frnd.
    def visitI_cvt_frnd(self, ctx:PtxParser.I_cvt_frndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvt_frnd_aux.
    def visitI_cvt_frnd_aux(self, ctx:PtxParser.I_cvt_frnd_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvt_opr.
    def visitI_cvt_opr(self, ctx:PtxParser.I_cvt_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvta.
    def visitI_cvta(self, ctx:PtxParser.I_cvtaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvta_type.
    def visitI_cvta_type(self, ctx:PtxParser.I_cvta_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_cvta_opr.
    def visitI_cvta_opr(self, ctx:PtxParser.I_cvta_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_div.
    def visitI_div(self, ctx:PtxParser.I_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_div_type.
    def visitI_div_type(self, ctx:PtxParser.I_div_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_div_opr.
    def visitI_div_opr(self, ctx:PtxParser.I_div_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ex2.
    def visitI_ex2(self, ctx:PtxParser.I_ex2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ex2_type.
    def visitI_ex2_type(self, ctx:PtxParser.I_ex2_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ex2_opr.
    def visitI_ex2_opr(self, ctx:PtxParser.I_ex2_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_exit.
    def visitI_exit(self, ctx:PtxParser.I_exitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_fma.
    def visitI_fma(self, ctx:PtxParser.I_fmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_fma_type.
    def visitI_fma_type(self, ctx:PtxParser.I_fma_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_fma_opr.
    def visitI_fma_opr(self, ctx:PtxParser.I_fma_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_isspacep.
    def visitI_isspacep(self, ctx:PtxParser.I_isspacepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_isspacep_type.
    def visitI_isspacep_type(self, ctx:PtxParser.I_isspacep_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_isspacep_opr.
    def visitI_isspacep_opr(self, ctx:PtxParser.I_isspacep_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ld.
    def visitI_ld(self, ctx:PtxParser.I_ldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ld_type.
    def visitI_ld_type(self, ctx:PtxParser.I_ld_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ld_opr.
    def visitI_ld_opr(self, ctx:PtxParser.I_ld_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ldu.
    def visitI_ldu(self, ctx:PtxParser.I_lduContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ldu_type.
    def visitI_ldu_type(self, ctx:PtxParser.I_ldu_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ldu_opr.
    def visitI_ldu_opr(self, ctx:PtxParser.I_ldu_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_lg2.
    def visitI_lg2(self, ctx:PtxParser.I_lg2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_lg2_type.
    def visitI_lg2_type(self, ctx:PtxParser.I_lg2_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_lg2_opr.
    def visitI_lg2_opr(self, ctx:PtxParser.I_lg2_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mad.
    def visitI_mad(self, ctx:PtxParser.I_madContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mad_type.
    def visitI_mad_type(self, ctx:PtxParser.I_mad_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mad_opr.
    def visitI_mad_opr(self, ctx:PtxParser.I_mad_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_madc.
    def visitI_madc(self, ctx:PtxParser.I_madcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_madc_type.
    def visitI_madc_type(self, ctx:PtxParser.I_madc_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_madc_opr.
    def visitI_madc_opr(self, ctx:PtxParser.I_madc_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mad24.
    def visitI_mad24(self, ctx:PtxParser.I_mad24Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mad24_type.
    def visitI_mad24_type(self, ctx:PtxParser.I_mad24_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mad24_opr.
    def visitI_mad24_opr(self, ctx:PtxParser.I_mad24_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_max.
    def visitI_max(self, ctx:PtxParser.I_maxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_max_type.
    def visitI_max_type(self, ctx:PtxParser.I_max_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_max_opr.
    def visitI_max_opr(self, ctx:PtxParser.I_max_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_membar.
    def visitI_membar(self, ctx:PtxParser.I_membarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_membar_type.
    def visitI_membar_type(self, ctx:PtxParser.I_membar_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_min.
    def visitI_min(self, ctx:PtxParser.I_minContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_min_type.
    def visitI_min_type(self, ctx:PtxParser.I_min_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_min_opr.
    def visitI_min_opr(self, ctx:PtxParser.I_min_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mov.
    def visitI_mov(self, ctx:PtxParser.I_movContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mov_type.
    def visitI_mov_type(self, ctx:PtxParser.I_mov_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mov_opr.
    def visitI_mov_opr(self, ctx:PtxParser.I_mov_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mul.
    def visitI_mul(self, ctx:PtxParser.I_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mul_type.
    def visitI_mul_type(self, ctx:PtxParser.I_mul_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mul_opr.
    def visitI_mul_opr(self, ctx:PtxParser.I_mul_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mul24.
    def visitI_mul24(self, ctx:PtxParser.I_mul24Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mul24_type.
    def visitI_mul24_type(self, ctx:PtxParser.I_mul24_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_mul24_opr.
    def visitI_mul24_opr(self, ctx:PtxParser.I_mul24_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_neg.
    def visitI_neg(self, ctx:PtxParser.I_negContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_neg_type.
    def visitI_neg_type(self, ctx:PtxParser.I_neg_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_neg_opr.
    def visitI_neg_opr(self, ctx:PtxParser.I_neg_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_not.
    def visitI_not(self, ctx:PtxParser.I_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_not_type.
    def visitI_not_type(self, ctx:PtxParser.I_not_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_not_opr.
    def visitI_not_opr(self, ctx:PtxParser.I_not_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_or.
    def visitI_or(self, ctx:PtxParser.I_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_or_type.
    def visitI_or_type(self, ctx:PtxParser.I_or_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_or_opr.
    def visitI_or_opr(self, ctx:PtxParser.I_or_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_pmevent.
    def visitI_pmevent(self, ctx:PtxParser.I_pmeventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_pmevent_opr.
    def visitI_pmevent_opr(self, ctx:PtxParser.I_pmevent_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_popc.
    def visitI_popc(self, ctx:PtxParser.I_popcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_popc_type.
    def visitI_popc_type(self, ctx:PtxParser.I_popc_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_popc_opr.
    def visitI_popc_opr(self, ctx:PtxParser.I_popc_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prefetch.
    def visitI_prefetch(self, ctx:PtxParser.I_prefetchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prefetch_type.
    def visitI_prefetch_type(self, ctx:PtxParser.I_prefetch_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prefetch_opr.
    def visitI_prefetch_opr(self, ctx:PtxParser.I_prefetch_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prefetchu.
    def visitI_prefetchu(self, ctx:PtxParser.I_prefetchuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prefetchu_type.
    def visitI_prefetchu_type(self, ctx:PtxParser.I_prefetchu_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prefetchu_opr.
    def visitI_prefetchu_opr(self, ctx:PtxParser.I_prefetchu_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prmt.
    def visitI_prmt(self, ctx:PtxParser.I_prmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prmt_type.
    def visitI_prmt_type(self, ctx:PtxParser.I_prmt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_prmt_opr.
    def visitI_prmt_opr(self, ctx:PtxParser.I_prmt_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rcp.
    def visitI_rcp(self, ctx:PtxParser.I_rcpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rcp_type.
    def visitI_rcp_type(self, ctx:PtxParser.I_rcp_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rcp_opr.
    def visitI_rcp_opr(self, ctx:PtxParser.I_rcp_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_red.
    def visitI_red(self, ctx:PtxParser.I_redContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_red_type.
    def visitI_red_type(self, ctx:PtxParser.I_red_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_red_opr.
    def visitI_red_opr(self, ctx:PtxParser.I_red_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rem.
    def visitI_rem(self, ctx:PtxParser.I_remContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rem_type.
    def visitI_rem_type(self, ctx:PtxParser.I_rem_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rem_opr.
    def visitI_rem_opr(self, ctx:PtxParser.I_rem_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ret.
    def visitI_ret(self, ctx:PtxParser.I_retContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_ret_type.
    def visitI_ret_type(self, ctx:PtxParser.I_ret_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rsqrt.
    def visitI_rsqrt(self, ctx:PtxParser.I_rsqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rsqrt_type.
    def visitI_rsqrt_type(self, ctx:PtxParser.I_rsqrt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_rsqrt_opr.
    def visitI_rsqrt_opr(self, ctx:PtxParser.I_rsqrt_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sad.
    def visitI_sad(self, ctx:PtxParser.I_sadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sad_type.
    def visitI_sad_type(self, ctx:PtxParser.I_sad_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sad_opr.
    def visitI_sad_opr(self, ctx:PtxParser.I_sad_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_selp.
    def visitI_selp(self, ctx:PtxParser.I_selpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_selp_type.
    def visitI_selp_type(self, ctx:PtxParser.I_selp_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_selp_opr.
    def visitI_selp_opr(self, ctx:PtxParser.I_selp_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_set.
    def visitI_set(self, ctx:PtxParser.I_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_set1.
    def visitI_set1(self, ctx:PtxParser.I_set1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_set1_type.
    def visitI_set1_type(self, ctx:PtxParser.I_set1_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_set1_opr.
    def visitI_set1_opr(self, ctx:PtxParser.I_set1_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_set2.
    def visitI_set2(self, ctx:PtxParser.I_set2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_set2_type.
    def visitI_set2_type(self, ctx:PtxParser.I_set2_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_set2_opr.
    def visitI_set2_opr(self, ctx:PtxParser.I_set2_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_setp.
    def visitI_setp(self, ctx:PtxParser.I_setpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_setp1.
    def visitI_setp1(self, ctx:PtxParser.I_setp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_setp1_type.
    def visitI_setp1_type(self, ctx:PtxParser.I_setp1_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_setp1_opr.
    def visitI_setp1_opr(self, ctx:PtxParser.I_setp1_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_setp2.
    def visitI_setp2(self, ctx:PtxParser.I_setp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_setp2_type.
    def visitI_setp2_type(self, ctx:PtxParser.I_setp2_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_setp2_opr.
    def visitI_setp2_opr(self, ctx:PtxParser.I_setp2_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_shl.
    def visitI_shl(self, ctx:PtxParser.I_shlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_shl_type.
    def visitI_shl_type(self, ctx:PtxParser.I_shl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_shl_opr.
    def visitI_shl_opr(self, ctx:PtxParser.I_shl_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_shr.
    def visitI_shr(self, ctx:PtxParser.I_shrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_shr_type.
    def visitI_shr_type(self, ctx:PtxParser.I_shr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_shr_opr.
    def visitI_shr_opr(self, ctx:PtxParser.I_shr_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sin.
    def visitI_sin(self, ctx:PtxParser.I_sinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sin_type.
    def visitI_sin_type(self, ctx:PtxParser.I_sin_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sin_opr.
    def visitI_sin_opr(self, ctx:PtxParser.I_sin_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_slct.
    def visitI_slct(self, ctx:PtxParser.I_slctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_slct_type.
    def visitI_slct_type(self, ctx:PtxParser.I_slct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_slct_opr.
    def visitI_slct_opr(self, ctx:PtxParser.I_slct_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sqrt.
    def visitI_sqrt(self, ctx:PtxParser.I_sqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sqrt_type.
    def visitI_sqrt_type(self, ctx:PtxParser.I_sqrt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sqrt_opr.
    def visitI_sqrt_opr(self, ctx:PtxParser.I_sqrt_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_st.
    def visitI_st(self, ctx:PtxParser.I_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_st_type.
    def visitI_st_type(self, ctx:PtxParser.I_st_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_st_opr.
    def visitI_st_opr(self, ctx:PtxParser.I_st_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sub.
    def visitI_sub(self, ctx:PtxParser.I_subContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sub_type.
    def visitI_sub_type(self, ctx:PtxParser.I_sub_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sub_opr.
    def visitI_sub_opr(self, ctx:PtxParser.I_sub_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_subc.
    def visitI_subc(self, ctx:PtxParser.I_subcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_subc_type.
    def visitI_subc_type(self, ctx:PtxParser.I_subc_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_subc_opr.
    def visitI_subc_opr(self, ctx:PtxParser.I_subc_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_suld.
    def visitI_suld(self, ctx:PtxParser.I_suldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_suld_type.
    def visitI_suld_type(self, ctx:PtxParser.I_suld_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_suld_opr.
    def visitI_suld_opr(self, ctx:PtxParser.I_suld_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sured.
    def visitI_sured(self, ctx:PtxParser.I_suredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sured_type.
    def visitI_sured_type(self, ctx:PtxParser.I_sured_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sured_opr.
    def visitI_sured_opr(self, ctx:PtxParser.I_sured_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sust.
    def visitI_sust(self, ctx:PtxParser.I_sustContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sust_type.
    def visitI_sust_type(self, ctx:PtxParser.I_sust_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_sust_opr.
    def visitI_sust_opr(self, ctx:PtxParser.I_sust_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_suq.
    def visitI_suq(self, ctx:PtxParser.I_suqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_suq_type.
    def visitI_suq_type(self, ctx:PtxParser.I_suq_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_suq_opr.
    def visitI_suq_opr(self, ctx:PtxParser.I_suq_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_testp.
    def visitI_testp(self, ctx:PtxParser.I_testpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_testp_type.
    def visitI_testp_type(self, ctx:PtxParser.I_testp_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_testp_opr.
    def visitI_testp_opr(self, ctx:PtxParser.I_testp_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_tex.
    def visitI_tex(self, ctx:PtxParser.I_texContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_tex_type.
    def visitI_tex_type(self, ctx:PtxParser.I_tex_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_tex_opr.
    def visitI_tex_opr(self, ctx:PtxParser.I_tex_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_txq.
    def visitI_txq(self, ctx:PtxParser.I_txqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_txq_type.
    def visitI_txq_type(self, ctx:PtxParser.I_txq_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_txq_opr.
    def visitI_txq_opr(self, ctx:PtxParser.I_txq_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_trap.
    def visitI_trap(self, ctx:PtxParser.I_trapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vabsdiff.
    def visitI_vabsdiff(self, ctx:PtxParser.I_vabsdiffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vadd.
    def visitI_vadd(self, ctx:PtxParser.I_vaddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vmad.
    def visitI_vmad(self, ctx:PtxParser.I_vmadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vmax.
    def visitI_vmax(self, ctx:PtxParser.I_vmaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vmin.
    def visitI_vmin(self, ctx:PtxParser.I_vminContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vset.
    def visitI_vset(self, ctx:PtxParser.I_vsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vshl.
    def visitI_vshl(self, ctx:PtxParser.I_vshlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vshr.
    def visitI_vshr(self, ctx:PtxParser.I_vshrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vsub.
    def visitI_vsub(self, ctx:PtxParser.I_vsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vote.
    def visitI_vote(self, ctx:PtxParser.I_voteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vote_type.
    def visitI_vote_type(self, ctx:PtxParser.I_vote_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_vote_opr.
    def visitI_vote_opr(self, ctx:PtxParser.I_vote_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_xor.
    def visitI_xor(self, ctx:PtxParser.I_xorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_xor_type.
    def visitI_xor_type(self, ctx:PtxParser.I_xor_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#i_xor_opr.
    def visitI_xor_opr(self, ctx:PtxParser.I_xor_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_register.
    def visitOpr_register(self, ctx:PtxParser.Opr_registerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_register_or_constant.
    def visitOpr_register_or_constant(self, ctx:PtxParser.Opr_register_or_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_register_or_constant2.
    def visitOpr_register_or_constant2(self, ctx:PtxParser.Opr_register_or_constant2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_register_or_constant3.
    def visitOpr_register_or_constant3(self, ctx:PtxParser.Opr_register_or_constant3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_register_or_constant4.
    def visitOpr_register_or_constant4(self, ctx:PtxParser.Opr_register_or_constant4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_register_or_constant5.
    def visitOpr_register_or_constant5(self, ctx:PtxParser.Opr_register_or_constant5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_label.
    def visitOpr_label(self, ctx:PtxParser.Opr_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr.
    def visitOpr(self, ctx:PtxParser.OprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr_aux.
    def visitOpr_aux(self, ctx:PtxParser.Opr_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr2.
    def visitOpr2(self, ctx:PtxParser.Opr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr3.
    def visitOpr3(self, ctx:PtxParser.Opr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr4.
    def visitOpr4(self, ctx:PtxParser.Opr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#opr5.
    def visitOpr5(self, ctx:PtxParser.Opr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#constant_expression.
    def visitConstant_expression(self, ctx:PtxParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#constant_expression_aux.
    def visitConstant_expression_aux(self, ctx:PtxParser.Constant_expression_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#conditional_expression.
    def visitConditional_expression(self, ctx:PtxParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#conditional_or_expression.
    def visitConditional_or_expression(self, ctx:PtxParser.Conditional_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#conditional_and_expression.
    def visitConditional_and_expression(self, ctx:PtxParser.Conditional_and_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#inclusive_or_expression.
    def visitInclusive_or_expression(self, ctx:PtxParser.Inclusive_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#exclusive_or_expression.
    def visitExclusive_or_expression(self, ctx:PtxParser.Exclusive_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#and_expression.
    def visitAnd_expression(self, ctx:PtxParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#equality_expression.
    def visitEquality_expression(self, ctx:PtxParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#relational_expression.
    def visitRelational_expression(self, ctx:PtxParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#relational_op.
    def visitRelational_op(self, ctx:PtxParser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#shift_expression.
    def visitShift_expression(self, ctx:PtxParser.Shift_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#shift_op.
    def visitShift_op(self, ctx:PtxParser.Shift_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#additive_expression.
    def visitAdditive_expression(self, ctx:PtxParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:PtxParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#unary_expression.
    def visitUnary_expression(self, ctx:PtxParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#unary_expression_not_plus_minus.
    def visitUnary_expression_not_plus_minus(self, ctx:PtxParser.Unary_expression_not_plus_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#cast_expression.
    def visitCast_expression(self, ctx:PtxParser.Cast_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#cast_expression_aux.
    def visitCast_expression_aux(self, ctx:PtxParser.Cast_expression_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#primary.
    def visitPrimary(self, ctx:PtxParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#par_expression.
    def visitPar_expression(self, ctx:PtxParser.Par_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#integer.
    def visitInteger(self, ctx:PtxParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#float_.
    def visitFloat_(self, ctx:PtxParser.Float_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#base_10_integer.
    def visitBase_10_integer(self, ctx:PtxParser.Base_10_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#base_8_integer.
    def visitBase_8_integer(self, ctx:PtxParser.Base_8_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PtxParser#base_16_integer.
    def visitBase_16_integer(self, ctx:PtxParser.Base_16_integerContext):
        return self.visitChildren(ctx)



del PtxParser