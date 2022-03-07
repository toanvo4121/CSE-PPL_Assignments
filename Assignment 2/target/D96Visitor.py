# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#code_declares.
    def visitCode_declares(self, ctx:D96Parser.Code_declaresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_attribute_declare.
    def visitClass_attribute_declare(self, ctx:D96Parser.Class_attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#special_init_method_declare.
    def visitSpecial_init_method_declare(self, ctx:D96Parser.Special_init_method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declare.
    def visitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl.
    def visitAttr_decl(self, ctx:D96Parser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#full_ids.
    def visitFull_ids(self, ctx:D96Parser.Full_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mid2.
    def visitMid2(self, ctx:D96Parser.Mid2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mid1.
    def visitMid1(self, ctx:D96Parser.Mid1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param_list.
    def visitParam_list(self, ctx:D96Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression1.
    def visitExpression1(self, ctx:D96Parser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression2.
    def visitExpression2(self, ctx:D96Parser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression3.
    def visitExpression3(self, ctx:D96Parser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression4.
    def visitExpression4(self, ctx:D96Parser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression5.
    def visitExpression5(self, ctx:D96Parser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression6.
    def visitExpression6(self, ctx:D96Parser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression7.
    def visitExpression7(self, ctx:D96Parser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression8.
    def visitExpression8(self, ctx:D96Parser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression9.
    def visitExpression9(self, ctx:D96Parser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression10.
    def visitExpression10(self, ctx:D96Parser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_list.
    def visitExpression_list(self, ctx:D96Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_declare_stmt.
    def visitVar_declare_stmt(self, ctx:D96Parser.Var_declare_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_attr_stmt.
    def visitVar_attr_stmt(self, ctx:D96Parser.Var_attr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#val_attr_stmt.
    def visitVal_attr_stmt(self, ctx:D96Parser.Val_attr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_stmt.
    def visitAttr_stmt(self, ctx:D96Parser.Attr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_stmt_no_init.
    def visitAttr_stmt_no_init(self, ctx:D96Parser.Attr_stmt_no_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list_without_static.
    def visitId_list_without_static(self, ctx:D96Parser.Id_list_without_staticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_stmt_full.
    def visitAttr_stmt_full(self, ctx:D96Parser.Attr_stmt_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt3.
    def visitStmt3(self, ctx:D96Parser.Stmt3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_stmt.
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#invoca_stmt.
    def visitInvoca_stmt(self, ctx:D96Parser.Invoca_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#all_type.
    def visitAll_type(self, ctx:D96Parser.All_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#prim_type.
    def visitPrim_type(self, ctx:D96Parser.Prim_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_type.
    def visitArr_type(self, ctx:D96Parser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_type.
    def visitInt_type(self, ctx:D96Parser.Int_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_type.
    def visitFloat_type(self, ctx:D96Parser.Float_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_type.
    def visitString_type(self, ctx:D96Parser.String_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_type.
    def visitBoolean_type(self, ctx:D96Parser.Boolean_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_member_type.
    def visitArray_member_type(self, ctx:D96Parser.Array_member_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_member.
    def visitArray_member(self, ctx:D96Parser.Array_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_array.
    def visitMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_in_multi.
    def visitMulti_in_multi(self, ctx:D96Parser.Multi_in_multiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_in_multi.
    def visitIndex_in_multi(self, ctx:D96Parser.Index_in_multiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#empty_multi.
    def visitEmpty_multi(self, ctx:D96Parser.Empty_multiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_arrays.
    def visitMulti_arrays(self, ctx:D96Parser.Multi_arraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_array_mem.
    def visitMulti_array_mem(self, ctx:D96Parser.Multi_array_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)



del D96Parser