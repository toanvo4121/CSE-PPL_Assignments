from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    # program: code_declares+ EOF;
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        classList = []
        classList = list(map(lambda x: self.visit(x), ctx.code_declares()))
        return Program(classList)
    # //////////////////////////////// declaration //////////////////////////////////
    # code_declares:
    # 	CLASS IDENTIFIERS (COLON IDENTIFIERS)? LP class_body* RP;
    def visitCode_declares(self, ctx:D96Parser.Code_declaresContext):
        if ctx.COLON():
            className = Id(ctx.IDENTIFIERS(0).getText())
            parentName = Id(ctx.IDENTIFIERS(1).getText())
        else:
            className = Id(ctx.IDENTIFIERS(0).getText())
            parentName = None
        flag = False
        if className.name == "Program":
            flag = True
        memList = []
        if ctx.class_body():
            for x in ctx.class_body():
                mem = self.visit(x)
                if isinstance(mem[0], MethodDecl):
                    if flag and mem[0].name.name == "main" and not mem[0].param:
                        mem[0].kind = Static()
                        flag = False
                memList += mem
        return ClassDecl(className, memList, parentName)
    # class_body:
    # 	method_declare
    # 	| class_attribute_declare
    # 	| special_init_method_declare;
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visit(ctx.getChild(0))
    # class_attribute_declare: (VAL | VAR) attr_decl SEMI;
    def visitClass_attribute_declare(self, ctx:D96Parser.Class_attribute_declareContext):
        attributes = self.visit(ctx.attr_decl())
        num_of_attr = len(attributes) // 2
        type = attributes[num_of_attr]
        result = []
        if len(attributes) == 2:
            for id in attributes[0]: # list_ids
                if ctx.VAL() and id.name[0] == '$':
                    result += [AttributeDecl(Static(), ConstDecl(id, type))]
                elif ctx.VAL() and id.name[0] != '$':
                    result += [AttributeDecl(Instance(), ConstDecl(id, type))]
                elif ctx.VAR() and id.name[0] == '$':
                    if isinstance(type, ClassType):
                        result += [AttributeDecl(Static(), VarDecl(id, type, NullLiteral()))]
                    else:
                        result += [AttributeDecl(Static(), VarDecl(id, type))]
                else:
                    if isinstance(type, ClassType):
                        result += [AttributeDecl(Instance(), VarDecl(id, type, NullLiteral()))]
                    else:
                        result += [AttributeDecl(Instance(), VarDecl(id, type))]
        else:
            attr_id_idx = 0
            attr_expr_idx = num_of_attr + 1
            for i in range(num_of_attr):
                id = attributes[attr_id_idx]
                expr = attributes[attr_expr_idx]
                if ctx.VAL() and id.name[0] == '$':
                    result += [AttributeDecl(Static(), ConstDecl(id, type, expr))]
                elif ctx.VAL() and id.name[0] != '$':
                    result += [AttributeDecl(Instance(), ConstDecl(id, type, expr))]
                elif ctx.VAR() and id.name[0] == '$':
                    result += [AttributeDecl(Static(), VarDecl(id, type, expr))]
                else:
                    result += [AttributeDecl(Instance(), VarDecl(id, type, expr))]
                attr_id_idx += 1
                attr_expr_idx += 1
        return result
    # Constructor & Destructor
    # special_init_method_declare:
    # 	(CONSTRUCTOR LB param_list? | DESTRUCTOR LB) RB block_stmt;
    def visitSpecial_init_method_declare(self, ctx:D96Parser.Special_init_method_declareContext):
        kind = Instance()
        param_list = self.visit(ctx.param_list()) if ctx.param_list() else []
        body = self.visit(ctx.block_stmt())
        if ctx.CONSTRUCTOR():
            name = Id(ctx.CONSTRUCTOR().getText())
        elif ctx.DESTRUCTOR():
            name = Id(ctx.DESTRUCTOR().getText())
        return [MethodDecl(kind, name, param_list, body)]
    # method_declare:
    # 	STATIC_MEM LB param_list? RB block_stmt
    # 	| IDENTIFIERS LB param_list? RB block_stmt;
    def visitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        param = self.visit(ctx.param_list()) if ctx.param_list() else []
        body = self.visit(ctx.block_stmt())
        if ctx.IDENTIFIERS():
            kind = Instance()
            name = Id(ctx.IDENTIFIERS().getText())
        elif ctx.STATIC_MEM():
            kind = Static()
            name = Id(ctx.STATIC_MEM().getText())
        return [MethodDecl(kind, name, param, body)]
    # attr_decl: (id_list COLON all_type) | mid2;
    def visitAttr_decl(self, ctx:D96Parser.Attr_declContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.mid2())
        else:
            list_ids = self.visit(ctx.id_list())
            all_type = self.visit(ctx.all_type())
            return (list_ids, all_type)
    # full_ids: IDENTIFIERS | STATIC_MEM;
    def visitFull_ids(self, ctx:D96Parser.Full_idsContext):
        return Id(ctx.getChild(0).getText())
    # id_list: full_ids (COMMA full_ids)*;
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        list_ids = []
        for i in ctx.full_ids():    
            list_ids += [self.visit(i)]
        return list_ids
    # mid2:
    # 	STATIC_MEM COMMA mid2 COMMA expression
    # 	| IDENTIFIERS COMMA mid2 COMMA expression
    # 	| STATIC_MEM mid1 expression
    # 	| IDENTIFIERS mid1 expression;
    def visitMid2(self, ctx:D96Parser.Mid2Context):
        id = Id(ctx.STATIC_MEM().getText()) if ctx.STATIC_MEM() else Id(ctx.IDENTIFIERS().getText())
        expr = self.visit(ctx.expression())
        type = [self.visit(ctx.mid1())] if ctx.mid1() else self.visit(ctx.mid2())
        return [id] + type + [expr]
    # mid1: COLON all_type ASSOP;
    def visitMid1(self, ctx:D96Parser.Mid1Context):
        return self.visit(ctx.all_type())
    # param_list: param (SEMI param)*;
    def visitParam_list(self, ctx:D96Parser.Param_listContext):
        result = [] 
        for x in ctx.param():
            result += self.visit(x)
        return result
    # param: IDENTIFIERS (COMMA IDENTIFIERS)* COLON all_type;
    def visitParam(self, ctx:D96Parser.ParamContext):
        paramList = list(map(lambda x: Id(x.getText()), ctx.IDENTIFIERS()))
        type = self.visit(ctx.all_type())
        return list(map(lambda x: VarDecl(x, type, NullLiteral()) if isinstance(type, ClassType) else VarDecl(x, type), paramList))
    # /////////////////////////// EXPRESSION //////////////////////////
    # expression:
    # 	expression1 (CONCAT | STRCMP) expression1
    # 	| expression1; // String expression
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        if ctx.CONCAT():
            return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)))
        elif ctx.STRCMP():
            return BinaryOp(ctx.STRCMP().getText(), self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)))
        else:
            return self.visit(ctx.expression1(0))
    # expression1:
    # 	expression2 (GRTOP | GTEOP | LSTOP | LTEOP | EQLOP | IEQOP) expression2
    # 	| expression2; // > >= < <= == != expression
    def visitExpression1(self, ctx:D96Parser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2(0))
        else:
            left = self.visit(ctx.expression2(0))
            right = self.visit(ctx.expression2(1))
            if ctx.GRTOP():
                op = ctx.GRTOP().getText()
            elif ctx.GTEOP():
                op = ctx.GTEOP().getText()
            elif ctx.LSTOP():
                op = ctx.LSTOP().getText()
            elif ctx.LTEOP():
                op = ctx.LTEOP().getText()
            elif ctx.EQLOP():
                op = ctx.EQLOP().getText()
            elif ctx.IEQOP():
                op = ctx.IEQOP().getText()
            return BinaryOp(op, left, right)
    # expression2:
    # 	expression2 (ANDOP | OROP) expression3
    # 	| expression3; // && || expression
    def visitExpression2(self, ctx:D96Parser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        else:
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            if ctx.ANDOP():
                op = ctx.ANDOP().getText()
            elif ctx.OROP():
                op = ctx.OROP().getText()
            return BinaryOp(op, left, right)
    # expression3:
    # 	expression3 (ADDOP | SUBOP) expression4
    # 	| expression4; // +- expression
    def visitExpression3(self, ctx:D96Parser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        else:
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            if ctx.ADDOP():
                op = ctx.ADDOP().getText()
            else: 
                op = ctx.SUBOP().getText()
            return BinaryOp(op, left, right)
    # expression4:
    # 	expression4 (MULOP | DIVOP | MODOP) expression5
    # 	| expression5; // */% expression
    def visitExpression4(self, ctx:D96Parser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        else:
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            if ctx.MULOP():
                op = ctx.MULOP().getText()
            elif ctx.DIVOP():
                op = ctx.DIVOP().getText()
            else:
                op = ctx.MODOP().getText()
            return BinaryOp(op, left, right)
    # expression5: NOTOP expression5 | expression6; // ! expression
    def visitExpression5(self, ctx:D96Parser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        else:
            return UnaryOp(ctx.NOTOP().getText(), self.visit(ctx.expression5()))
    # expression6: SUBOP expression6 | expression7; // - expression
    def visitExpression6(self, ctx:D96Parser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        else:
            return UnaryOp(ctx.SUBOP().getText(), self.visit(ctx.expression6()))
    # expression7:
    #   expression7 (LSB expression RSB)+
    # 	| expression8; // [] expression
    def visitExpression7(self, ctx:D96Parser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression8())
        else: 
            exprs = []
            for x in ctx.expression():
                exprs += [self.visit(x)]
            return ArrayCell(self.visit(ctx.expression7()), exprs)
    # expression8:
    # 	expression8 DOTOP IDENTIFIERS (LSB expression RSB)+
    #   | expression8 DOTOP IDENTIFIERS LB expression_list? RB (LSB expression RSB)+
    #   | expression8 DOTOP IDENTIFIERS
    # 	| expression8 DOTOP IDENTIFIERS LB expression_list? RB
    # 	| expression9;
    def visitExpression8(self, ctx:D96Parser.Expression8Context):
        if ctx.getChildCount() == 1: # line 5
            return self.visit(ctx.expression9())
        obj = self.visit(ctx.expression8())
        name = Id(ctx.IDENTIFIERS().getText())
        if ctx.LSB() and ctx.RSB():
            exprs = []
            for x in ctx.expression():
                exprs += [self.visit(x)]
            if ctx.LB() and ctx.RB(): # line 2
                param = self.visit(ctx.expression_list()) if ctx.expression_list() else []
                return ArrayCell(CallExpr(obj, name, param), exprs)
            else: # line 1
                return ArrayCell(FieldAccess(obj, name), exprs)
        elif ctx.LB() and ctx.RB(): # line 4
            paramList = self.visit(ctx.expression_list()) if ctx.expression_list() else []
            return CallExpr(obj, name, paramList)
        elif ctx.getChildCount() == 3: # line 3
            return FieldAccess(obj, name)
    # expression9:
	# IDENTIFIERS SCOOP STATIC_MEM (LSB expression RSB)+
	# | IDENTIFIERS SCOOP STATIC_MEM LB expression_list? RB (
	# 	LSB expression RSB
	# )+
	# | IDENTIFIERS SCOOP STATIC_MEM
	# | IDENTIFIERS SCOOP STATIC_MEM LB (expression_list)? RB
	# | expression10;
    def visitExpression9(self, ctx:D96Parser.Expression9Context):
        if ctx.getChildCount() == 1: # line 5
            return self.visit(ctx.expression10())
        obj = Id(ctx.IDENTIFIERS().getText())
        name = Id(ctx.STATIC_MEM().getText())
        if ctx.LSB() and ctx.RSB():
            exprs = []
            for x in ctx.expression():
                exprs += [self.visit(x)]
            if ctx.LB() and ctx.RB(): # line 2
                param = self.visit(ctx.expression_list()) if ctx.expression_list() else []
                return ArrayCell(CallExpr(obj, name, param), exprs)
            else: # line 1
                return ArrayCell(FieldAccess(obj, name), exprs)
        elif ctx.LB() and ctx.RB(): # line 4
            paramList = self.visit(ctx.expression_list()) if ctx.expression_list() else []
            return CallExpr(obj, name, paramList)
        elif ctx.getChildCount() == 3: # line 3
            return FieldAccess(obj, name)
    # expression10: NEW IDENTIFIERS LB expression_list? RB | operand;
    def visitExpression10(self, ctx:D96Parser.Expression10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        else:
            className = Id(ctx.IDENTIFIERS().getText())
            paramList = self.visit(ctx.expression_list()) if ctx.expression_list() != None else []
            return NewExpr(className, paramList)
    # operand:
    # 	IDENTIFIERS
    # 	| literals
    # 	| SELF
    # 	| NULL
    # 	| LB expression RB
    # 	| IDENTIFIERS (LSB expression RSB)*;
    def visitOperand(self, ctx:D96Parser.OperandContext):
        if ctx.getChildCount() == 1:
            if ctx.IDENTIFIERS():
                return Id(ctx.IDENTIFIERS().getText())
            elif ctx.literals():
                return self.visit(ctx.literals())
            elif ctx.SELF():
                return SelfLiteral()
            elif ctx.NULL():
                return NullLiteral()
        else:
            if ctx.LB() and ctx.RB():
                return self.visit(ctx.expression(0))
            else:
                arr = Id(ctx.IDENTIFIERS().getText())
                idx = []
                for x in ctx.expression():
                    idx += [self.visit(x)]
                return ArrayCell(arr, idx)
    # expression_list: expression (COMMA expression)*;
    def visitExpression_list(self, ctx:D96Parser.Expression_listContext):
        return list(map(lambda x: self.visit(x), ctx.expression()))
    # // //////////////////////// Statements ///////////////////////////////////
    # var_declare_stmt: var_attr_stmt | val_attr_stmt;
    def visitVar_declare_stmt(self, ctx:D96Parser.Var_declare_stmtContext):
        return self.visit(ctx.getChild(0))
    # var_attr_stmt: VAR attr_stmt SEMI;
    def visitVar_attr_stmt(self, ctx:D96Parser.Var_attr_stmtContext):
        attributes = self.visit(ctx.attr_stmt())
        num_of_attr = len(attributes) // 2
        type = attributes[num_of_attr]
        result = []
        if len(attributes) == 2:
            for id in attributes[0]: # list_ids
                if isinstance(type, ClassType):
                    result += [VarDecl(id, type, NullLiteral())]
                else:
                    result += [VarDecl(id, type)]
        else:
            attr_id_idx = 0
            attr_expr_idx = num_of_attr + 1
            for i in range(num_of_attr):
                id = attributes[attr_id_idx]
                expr = attributes[attr_expr_idx]
                result += [VarDecl(id, type, expr)]
                attr_id_idx += 1
                attr_expr_idx += 1
        return result
    # val_attr_stmt: VAL attr_stmt SEMI;
    def visitVal_attr_stmt(self, ctx:D96Parser.Val_attr_stmtContext):
        attributes = self.visit(ctx.attr_stmt())
        num_of_attr = len(attributes) // 2
        type = attributes[num_of_attr]
        result = []
        if len(attributes) == 2:
            for id in attributes[0]: # list_ids
                result += [ConstDecl(id, type)]
        else:
            attr_id_idx = 0
            attr_expr_idx = num_of_attr + 1
            for i in range(num_of_attr):
                id = attributes[attr_id_idx]
                expr = attributes[attr_expr_idx]
                result += [ConstDecl(id, type, expr)]
                attr_id_idx += 1
                attr_expr_idx += 1
        return result
    # attr_stmt: attr_stmt_no_init | attr_stmt_full;
    def visitAttr_stmt(self, ctx:D96Parser.Attr_stmtContext):
        return self.visit(ctx.getChild(0))
    # attr_stmt_no_init: id_list_without_static COLON all_type;
    def visitAttr_stmt_no_init(self, ctx:D96Parser.Attr_stmt_no_initContext):
        list_ids = self.visit(ctx.id_list_without_static())
        type = self.visit(ctx.all_type())
        return (list_ids, type)
    # id_list_without_static:
    # 	IDENTIFIERS COMMA id_list_without_static
    # 	| IDENTIFIERS;
    def visitId_list_without_static(self, ctx:D96Parser.Id_list_without_staticContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.IDENTIFIERS().getText())]
        else:
            return [Id(ctx.IDENTIFIERS().getText())] + self.visit(ctx.id_list_without_static())
    # attr_stmt_full:
    # 	IDENTIFIERS COMMA attr_stmt_full COMMA expression
    # 	| IDENTIFIERS mid1 expression;
    def visitAttr_stmt_full(self, ctx:D96Parser.Attr_stmt_fullContext):
        id = Id(ctx.IDENTIFIERS().getText())
        expression = self.visit(ctx.expression())
        if ctx.mid1():
            type = self.visit(ctx.mid1())
            return [id, type, expression]
        else:
            return [id] + self.visit(ctx.attr_stmt_full()) + [expression]
    # block_stmt: LP stmt3* RP;
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        stmtList = []
        if ctx.stmt3():
            for x in ctx.stmt3():
                stmt = self.visit(x)
                if isinstance(stmt, list):
                    stmtList += stmt
                else:
                    stmtList += [stmt]
        return Block(stmtList)
    # stmt3:
    # 	var_declare_stmt
    # 	| assign_stmt
    # 	| if_stmt
    # 	| for_stmt
    # 	| block_stmt
    # 	| break_stmt
    # 	| continue_stmt
    # 	| return_stmt
    # 	| invoca_stmt;
    def visitStmt3(self, ctx:D96Parser.Stmt3Context):
        return self.visit(ctx.getChild(0))
    # assign_stmt: lhs ASSOP expression SEMI;
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expression())
        return Assign(lhs, expr)
    # lhs: IDENTIFIERS (LSB expression7 RSB)* | expression7;
    def visitLhs(self, ctx:D96Parser.LhsContext):
        if ctx.IDENTIFIERS() and ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIERS().getText())
        elif ctx.expression7() and ctx.getChildCount() == 1:
            return self.visit(ctx.expression7(0))
        else:
            idx = []
            for x in ctx.expression7():
                idx += [self.visit(x)]
            return ArrayCell(Id(ctx.IDENTIFIERS().getText()), idx)
    # if_stmt:
    # 	IF LB expression RB block_stmt (
    # 		ELSEIF LB expression RB block_stmt
    # 	)* (ELSE block_stmt)?;
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        expr = self.visit(ctx.expression(0))
        thenStmt = self.visit(ctx.block_stmt(0))
        if ctx.getChildCount() == 5:
            elseStmt = None
            return If(expr, thenStmt, elseStmt)
        elif not ctx.ELSEIF() and ctx.ELSE():
            elseStmt = self.visit(ctx.block_stmt(1))
            return If(expr, thenStmt, elseStmt)
        elif ctx.ELSEIF():
            elseif_exprs = []
            for x in ctx.expression():
                if x == ctx.expression(0):
                    continue
                elseif_exprs += [self.visit(x)]
            elseif_stmts = []
            for y in ctx.block_stmt():
                if y == ctx.block_stmt(0):
                    continue
                elseif_stmts += [self.visit(y)]
            
            num_of_elseifs = len(elseif_exprs)
            elseif_leaf = If(elseif_exprs[-1], elseif_stmts[-1])
            if ctx.ELSE():
                elseif_stmts.pop(-1)
                elseif_leaf = If(elseif_exprs[-1], elseif_stmts[-1], self.visit(ctx.block_stmt()[-1]))
            for i in range(2, num_of_elseifs + 1):
                elseif_leaf = If(elseif_exprs[-i], elseif_stmts[-i], elseif_leaf)
            return If(expr, thenStmt, elseif_leaf)
    # for_stmt:
    # 	FOREACH LB IDENTIFIERS IN expression DOTDOT expression (BY expression)? RB block_stmt;
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        id = Id(ctx.IDENTIFIERS().getText())
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1))
        loop = self.visit(ctx.block_stmt())
        if ctx.BY():
            return For(id, expr1, expr2, loop, self.visit(ctx.expression(2)))
        else:
            return For(id, expr1, expr2, loop, IntLiteral(1))
    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return Break()
    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return Continue()
    # return_stmt: RETURN expression SEMI | RETURN SEMI;
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return Return(self.visit(ctx.expression())) if ctx.expression() else Return()
    # invoca_stmt:
    # 	IDENTIFIERS SCOOP STATIC_MEM LB expression_list? RB SEMI
    # 	| expression8 DOTOP IDENTIFIERS LB expression_list? RB SEMI;
    def visitInvoca_stmt(self, ctx:D96Parser.Invoca_stmtContext):
        arguments = self.visit(ctx.expression_list()) if ctx.expression_list() else []
        if ctx.DOTOP():
            obj = self.visit(ctx.expression8())
            method = Id(ctx.IDENTIFIERS().getText())
        else:
            obj = Id(ctx.IDENTIFIERS().getText())
            method = Id(ctx.STATIC_MEM().getText())
        return CallStmt(obj, method, arguments)
    # // type
    # all_type: prim_type | arr_type | class_type;
    def visitAll_type(self, ctx:D96Parser.All_typeContext):
        return self.visit(ctx.getChild(0))
    # prim_type: int_type | float_type | boolean_type | string_type;
    def visitPrim_type(self, ctx:D96Parser.Prim_typeContext):
        return self.visit(ctx.getChild(0))
    # arr_type: ARRAY LSB (prim_type | arr_type) COMMA NZINTLIT RSB;
    def visitArr_type(self, ctx:D96Parser.Arr_typeContext):
        num = ctx.NZINTLIT().getText()
        if num == "0":
            size = int(num, 0)
        elif num[0] == "0" and num[1] != "b" and num[1] != "B" and num[1] != "x" and num[1] != "X":
            result_num = num[1:]
            result_num = "0o" + result_num
            size = int(result_num, 0)
        else:
            size = int(num, 0)
        arr_type = self.visit(ctx.getChild(2))
        return ArrayType(size, arr_type)
    # class_type: IDENTIFIERS;
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return ClassType(Id(ctx.IDENTIFIERS().getText()))
    # int_type: INT;
    def visitInt_type(self, ctx:D96Parser.Int_typeContext):
        return IntType()
    # float_type: FLOAT;
    def visitFloat_type(self, ctx:D96Parser.Float_typeContext):
        return FloatType()
    # string_type: STRING;
    def visitString_type(self, ctx:D96Parser.String_typeContext):
        return StringType()
    # boolean_type: BOOLEAN;
    def visitBoolean_type(self, ctx:D96Parser.Boolean_typeContext):
        return BoolType()
    # primitive_type:
    #     INTLIT
    #     | NZINTLIT
    #     | FLOATLIT
    #     | STRINGLIT
    #     | BOOLIT;
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        if ctx.INTLIT():
            num = ctx.INTLIT().getText()
            if num == "0":
                return IntLiteral(int(num, 0))
            elif num[0] == "0" and num[1] != "b" and num[1] != "B" and num[1] != "x" and num[1] != "X":
                result_num = num[1:]
                result_num = "0o" + result_num
                return IntLiteral(int(result_num, 8))
            else:
                return IntLiteral(int(num, 0))
        elif ctx.NZINTLIT():
            num = ctx.NZINTLIT().getText()
            if num == "0":
                return IntLiteral(int(num, 0))
            elif num[0] == "0" and num[1] != "b" and num[1] != "B" and num[1] != "x" and num[1] != "X":
                result_num = num[1:]
                result_num = "0o" + result_num
                return IntLiteral(int(result_num, 8))
            else:
                return IntLiteral(int(num, 0))
        elif ctx.FLOATLIT():
            num = ctx.FLOATLIT().getText()
            if num[0] == "." and num[1] == "e":
                num = "0" + num
            return FloatLiteral(float(num))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            value = True if ctx.BOOLIT().getText() == "True" else False
            return BooleanLiteral(ctx.BOOLIT().getText())
    # array_member_type: (primitive_type | expression);
    def visitArray_member_type(self, ctx:D96Parser.Array_member_typeContext):
        return self.visit(ctx.getChild(0))
    # indexed_array: ARRAY LB (array_member |) RB;
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        if ctx.array_member():
            return ArrayLiteral(self.visit(ctx.array_member()))
        else:
            return ArrayLiteral([])
    # array_member: array_member_type (COMMA array_member_type)*;
    def visitArray_member(self, ctx:D96Parser.Array_memberContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.array_member_type())
        else:
            arr_mem_typ = []
            for x in ctx.array_member_type():
                arr_mem_typ += [self.visit(x)]
            return arr_mem_typ
    # multi_array: multi_in_multi | index_in_multi | empty_multi;
    def visitMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        return self.visit(ctx.getChild(0))
    # multi_in_multi: ARRAY LB multi_arrays RB;
    def visitMulti_in_multi(self, ctx:D96Parser.Multi_in_multiContext):
        return ArrayLiteral(self.visit(ctx.multi_arrays()))
    # index_in_multi: ARRAY LB multi_array_mem RB;
    def visitIndex_in_multi(self, ctx:D96Parser.Index_in_multiContext):
        return ArrayLiteral(self.visit(ctx.multi_array_mem()))
    # empty_multi: ARRAY LB RB;
    def visitEmpty_multi(self, ctx:D96Parser.Empty_multiContext):
        return ArrayLiteral([])
    # multi_arrays: multi_array COMMA multi_arrays | multi_array;
    def visitMulti_arrays(self, ctx:D96Parser.Multi_arraysContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multi_array())
        else:
            return [self.visit(ctx.multi_array)] + self.visit(ctx.multi_arrays())
    # multi_array_mem: indexed_array (COMMA multi_array_mem)*;
    def visitMulti_array_mem(self, ctx:D96Parser.Multi_array_memContext):
        if ctx.multi_array_mem():
            mem = []
            for i in ctx.multi_array_mem():
                mem += [self.visit(i)]
        else:
            return [self.visit(ctx.getChild(0))]
    # literals: primitive_type | indexed_array | multi_array;
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visit(ctx.getChild(0))