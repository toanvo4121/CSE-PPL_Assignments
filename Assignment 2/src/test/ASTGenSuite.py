import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
	def test1(self):
		input = """
		Class  Spider_man {
			Var Peter_1: Tobey = (a::$b).c;
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_man),[AttributeDecl(Instance,VarDecl(Id(Peter_1),ClassType(Id(Tobey)),FieldAccess(FieldAccess(Id(a),Id($b)),Id(c))))])])"""
		self.assertTrue(TestAST.test(input,expect,301))
		
	def test2(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val num: Int;
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(num),IntType,None))])])"""
		self.assertTrue(TestAST.test(input,expect,302))

	def test3(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.num;
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(num)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,303))

	def test4(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val Num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.Num;
			}
			
			Constructor(Suits: String; name: String; Num: Int) {
				Self.Suits = Suits;
				Self.name = name;
				Self.Num = Num;
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(Num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(Num)))])),MethodDecl(Id(Constructor),Instance,[param(Id(Suits),StringType),param(Id(name),StringType),param(Id(Num),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(Suits)),Id(Suits)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(Num)),Id(Num))]))])])"""
		self.assertTrue(TestAST.test(input,expect,304))
		
	def test5(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val Num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.Num;
			}
			
			Constructor(Suits: String; name: String; Num: Int) {
				Self.Suits = Suits;
				Self.name = name;
				Self.Num = Num;
			}
			Destructor() {
			
			}
		}
			
		Class Program {
			main() {
				Var Peter_1: Spider_verse = New Spider_verse("Red", "Peter Parker", 1);
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(Num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(Num)))])),MethodDecl(Id(Constructor),Instance,[param(Id(Suits),StringType),param(Id(name),StringType),param(Id(Num),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(Suits)),Id(Suits)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(Num)),Id(Num))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Peter_1),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[StringLit(Red),StringLit(Peter Parker),IntLit(1)]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,305))

	def test6(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val Num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.Num;
			}
			
			Constructor(Suits: String; name: String; Num: Int) {
				Self.Suits = Suits;
				Self.name = name;
				Self.Num = Num;
			}
			Destructor() {
			
			}
		}
			
		Class Program {
			main() {
				Var Peter_1: Spider_verse = New Spider_verse("Red", "Peter Parker", 1);
				Val Peter_1_Suits: String = Peter_1.getSuits();
				Var Peter_1_name: String = Peter_1.getName();
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(Num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(Num)))])),MethodDecl(Id(Constructor),Instance,[param(Id(Suits),StringType),param(Id(name),StringType),param(Id(Num),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(Suits)),Id(Suits)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(Num)),Id(Num))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Peter_1),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[StringLit(Red),StringLit(Peter Parker),IntLit(1)])),ConstDecl(Id(Peter_1_Suits),StringType,CallExpr(Id(Peter_1),Id(getSuits),[])),VarDecl(Id(Peter_1_name),StringType,CallExpr(Id(Peter_1),Id(getName),[]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,306))
		
	def test7(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val Num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.Num;
			}
			
			Constructor(Suits: String; name: String; Num: Int) {
				Self.Suits = Suits;
				Self.name = name;
				Self.Num = Num;
			}
			Destructor() {
			
			}
		}
			
		Class Program {
			main() {
				Var Peter_1: Spider_verse = New Spider_verse("Red", "Peter Parker", 1);
				Var Peter_2: Spider_verse = New Spider_verse(Peter_1.getSuits(), Peter_1.getName(), 2);
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(Num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(Num)))])),MethodDecl(Id(Constructor),Instance,[param(Id(Suits),StringType),param(Id(name),StringType),param(Id(Num),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(Suits)),Id(Suits)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(Num)),Id(Num))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Peter_1),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[StringLit(Red),StringLit(Peter Parker),IntLit(1)])),VarDecl(Id(Peter_2),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_1),Id(getName),[]),IntLit(2)]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,307))
		
	def test8(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val Num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.Num;
			}
			
			Constructor(Suits: String; name: String; Num: Int) {
				Self.Suits = Suits;
				Self.name = name;
				Self.Num = Num;
			}
			Destructor() {
			
			}
		}
			
		Class Program {
			main() {
				Var Peter_1: Spider_verse = New Spider_verse("Red", "Peter Parker", 1);
				Var Peter_2: Spider_verse = New Spider_verse(Peter_1.getSuits(), Peter_1.getName(), 2);
				
				If (Peter_1.getName() ==. Peter_2.getName()) {
					SOut.Println("Different universe!");
					If (Peter_1.getSuits() ==. Peter_2.getSuits()) {
						SOut.Println("But same suits!");
					}
					Else {
					SOut.Println("And different suits, too!");
					}
				}
				Else {
					SOut.Println("Same universe");
				}
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(Num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(Num)))])),MethodDecl(Id(Constructor),Instance,[param(Id(Suits),StringType),param(Id(name),StringType),param(Id(Num),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(Suits)),Id(Suits)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(Num)),Id(Num))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Peter_1),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[StringLit(Red),StringLit(Peter Parker),IntLit(1)])),VarDecl(Id(Peter_2),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_1),Id(getName),[]),IntLit(2)])),If(BinaryOp(==.,CallExpr(Id(Peter_1),Id(getName),[]),CallExpr(Id(Peter_2),Id(getName),[])),Block([Call(Id(SOut),Id(Println),[StringLit(Different universe!)]),If(BinaryOp(==.,CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_2),Id(getSuits),[])),Block([Call(Id(SOut),Id(Println),[StringLit(But same suits!)])]),Block([Call(Id(SOut),Id(Println),[StringLit(And different suits, too!)])]))]),Block([Call(Id(SOut),Id(Println),[StringLit(Same universe)])]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,308))
    
	def test9(self):
		input = """
		Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val Num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.Num;
			}
			
			Constructor(Suits: String; name: String; Num: Int) {
				Self.Suits = Suits;
				Self.name = name;
				Self.Num = Num;
			}
			Destructor() {
			
			}
		}
			
		Class Program {
			main() {
				Var Peter_1: Spider_verse = New Spider_verse("Red", "Peter Parker", 1);
				Var Peter_2: Spider_verse = New Spider_verse(Peter_1.getSuits(), Peter_1.getName(), 2);
				
				If ((Peter_1.getName() ==. Peter_2.getName()) && (Peter_1.getSuits() ==. Peter_2.getSuits())) {
				SOut.Println("Different universe but same suits");
				}
				Elseif (Peter_1.getName() ==. Peter_2.getName()) {
				SOut.Println("Different universe and different suits, too!");
				}
				Elseif (Peter_1.getSuits() ==. Peter_2.getSuits()) {
				SOut.Println("Same universe but different suits!");
				}
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(Num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(Num)))])),MethodDecl(Id(Constructor),Instance,[param(Id(Suits),StringType),param(Id(name),StringType),param(Id(Num),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(Suits)),Id(Suits)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(Num)),Id(Num))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Peter_1),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[StringLit(Red),StringLit(Peter Parker),IntLit(1)])),VarDecl(Id(Peter_2),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_1),Id(getName),[]),IntLit(2)])),If(BinaryOp(&&,BinaryOp(==.,CallExpr(Id(Peter_1),Id(getName),[]),CallExpr(Id(Peter_2),Id(getName),[])),BinaryOp(==.,CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_2),Id(getSuits),[]))),Block([Call(Id(SOut),Id(Println),[StringLit(Different universe but same suits)])]),If(BinaryOp(==.,CallExpr(Id(Peter_1),Id(getName),[]),CallExpr(Id(Peter_2),Id(getName),[])),Block([Call(Id(SOut),Id(Println),[StringLit(Different universe and different suits, too!)])]),If(BinaryOp(==.,CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_2),Id(getSuits),[])),Block([Call(Id(SOut),Id(Println),[StringLit(Same universe but different suits!)])]))))]))])])"""
		self.assertTrue(TestAST.test(input,expect,309))

	def test10(self):
		input = """
		Class Program{
			main(){
				Var x: Int = 7;
				Var e: Int = 12;
				Var q: Boolean = (x + 7) >= e;
				Var t: Boolean = ((q == True) != False) == ((e <= 3) == (x >= 2));
			}
		}
		"""
		expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,IntLit(7)),VarDecl(Id(e),IntType,IntLit(12)),VarDecl(Id(q),BoolType,BinaryOp(>=,BinaryOp(+,Id(x),IntLit(7)),Id(e))),VarDecl(Id(t),BoolType,BinaryOp(==,BinaryOp(!=,BinaryOp(==,Id(q),BooleanLit(True)),BooleanLit(False)),BinaryOp(==,BinaryOp(<=,Id(e),IntLit(3)),BinaryOp(>=,Id(x),IntLit(2)))))]))])])"
		self.assertTrue(TestAST.test(input, expect, 310))
        
	def test11(self):
		input = """
		Class Program {
			main() {
				Var expr: Exp = New Exp(1,"+",2);
				Var lhv_expr: Int = expr.BExp.op1;
			}
		}
		Class BinExp {
			Var op1: Int;
			Var op: String;
			Var op2: Int;
			Constructor(op1: Int; op: String; op2:Int) {
				Self.op1 = op1;
				Self.op = op;
				Self.op2 = op2;
			}
		}
		Class Expr {
			Var BExp: BinExp;
			Constructor(op1: Int; op: String; op2: Int) {
				Self.BExp = New BinExp(op1, op, op2);
			}
		}
		
		"""
		expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(expr),ClassType(Id(Exp)),NewExpr(Id(Exp),[IntLit(1),StringLit(+),IntLit(2)])),VarDecl(Id(lhv_expr),IntType,FieldAccess(FieldAccess(Id(expr),Id(BExp)),Id(op1)))]))]),ClassDecl(Id(BinExp),[AttributeDecl(Instance,VarDecl(Id(op1),IntType)),AttributeDecl(Instance,VarDecl(Id(op),StringType)),AttributeDecl(Instance,VarDecl(Id(op2),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(op1),IntType),param(Id(op),StringType),param(Id(op2),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(op1)),Id(op1)),AssignStmt(FieldAccess(Self(),Id(op)),Id(op)),AssignStmt(FieldAccess(Self(),Id(op2)),Id(op2))]))]),ClassDecl(Id(Expr),[AttributeDecl(Instance,VarDecl(Id(BExp),ClassType(Id(BinExp)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(op1),IntType),param(Id(op),StringType),param(Id(op2),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(BExp)),NewExpr(Id(BinExp),[Id(op1),Id(op),Id(op2)]))]))])])"
		self.assertTrue(TestAST.test(input, expect, 311))
    
	def test12(self):
		input = """
        Class Spider_verse {
			Val Suits: String;
			Var name: String;
			Val Num: Int;
			
			getSuits() {
				Return Self.Suits;
			}
			
			getName() {
				Return Self.name;
			}
			
			getNum() {
				Return Self.Num;
			}
			
			Constructor(Suits: String; name: String; Num: Int) {
				Self.Suits = Suits;
				Self.name = name;
				Self.Num = Num;
			}
			Destructor() {
			
			}
		}
			
		Class Program {
			main() {
				Var Peter_1: Spider_verse = New Spider_verse("Red", "Peter Parker", 1);
				Var Peter_2: Spider_verse = New Spider_verse(Peter_1.getSuits(), Peter_1.getName(), 2);
				
				If ((Peter_1.getName() ==. Peter_2.getName()) && (Peter_1.getSuits() ==. Peter_2.getSuits())) {
				SOut.Println("Different universe but same suits");
				}
				Elseif (Peter_1.getName() ==. Peter_2.getName()) {
				SOut.Println("Different universe and different suits, too!");
				}
				Elseif (Peter_1.getSuits() ==. Peter_2.getSuits()) {
				SOut.Println("Same universe but different suits!");
				}
				Else {
				SOut.Println("Something was wrong!");
				}
			}
		}
        """
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(Suits),StringType,None)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,ConstDecl(Id(Num),IntType,None)),MethodDecl(Id(getSuits),Instance,[],Block([Return(FieldAccess(Self(),Id(Suits)))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(getNum),Instance,[],Block([Return(FieldAccess(Self(),Id(Num)))])),MethodDecl(Id(Constructor),Instance,[param(Id(Suits),StringType),param(Id(name),StringType),param(Id(Num),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(Suits)),Id(Suits)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(Num)),Id(Num))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Peter_1),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[StringLit(Red),StringLit(Peter Parker),IntLit(1)])),VarDecl(Id(Peter_2),ClassType(Id(Spider_verse)),NewExpr(Id(Spider_verse),[CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_1),Id(getName),[]),IntLit(2)])),If(BinaryOp(&&,BinaryOp(==.,CallExpr(Id(Peter_1),Id(getName),[]),CallExpr(Id(Peter_2),Id(getName),[])),BinaryOp(==.,CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_2),Id(getSuits),[]))),Block([Call(Id(SOut),Id(Println),[StringLit(Different universe but same suits)])]),If(BinaryOp(==.,CallExpr(Id(Peter_1),Id(getName),[]),CallExpr(Id(Peter_2),Id(getName),[])),Block([Call(Id(SOut),Id(Println),[StringLit(Different universe and different suits, too!)])]),If(BinaryOp(==.,CallExpr(Id(Peter_1),Id(getSuits),[]),CallExpr(Id(Peter_2),Id(getSuits),[])),Block([Call(Id(SOut),Id(Println),[StringLit(Same universe but different suits!)])]),Block([Call(Id(SOut),Id(Println),[StringLit(Something was wrong!)])]))))]))])])"""
		self.assertTrue(TestAST.test(input,expect,312))
    
	def test13(self):
		input = """
        Class TestEmptyClass {
			
		}
        """
		expect = """Program([ClassDecl(Id(TestEmptyClass),[])])"""
		self.assertTrue(TestAST.test(input,expect,313))
        
	def test14(self):
		input = """
        Class Base {
			Var testFloat: Float = 0.00000E000000;
		}
		Class Derived {
			Var testObj: Base;
		}
        """
		expect = """Program([ClassDecl(Id(Base),[AttributeDecl(Instance,VarDecl(Id(testFloat),FloatType,FloatLit(0.0)))]),ClassDecl(Id(Derived),[AttributeDecl(Instance,VarDecl(Id(testObj),ClassType(Id(Base)),NullLiteral()))])])"""
		self.assertTrue(TestAST.test(input,expect,314))
    
	def test15(self):
		input = """
        Class testMathExpressions {
            main() {
               	Var testFloat_1: Float = 0.00000E00000 * 10.;
				Var testInt_1: Int = 0B10_0_110_0100_1 + 0XA_BCD_EF;
				Var testFloat_2: Float = Math.PI / 15.5;
				Var testInt_2: Int = 20 % 3;
			}
		}
        """
		expect = """Program([ClassDecl(Id(testMathExpressions),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(testFloat_1),FloatType,BinaryOp(*,FloatLit(0.0),FloatLit(10.0))),VarDecl(Id(testInt_1),IntType,BinaryOp(+,IntLit(1225),IntLit(11259375))),VarDecl(Id(testFloat_2),FloatType,BinaryOp(/,FieldAccess(Id(Math),Id(PI)),FloatLit(15.5))),VarDecl(Id(testInt_2),IntType,BinaryOp(%,IntLit(20),IntLit(3)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,315))
        
	def test16(self):
		input = """
        Class testMathExpressions {
			main() {
				Val PI: Float = 3.1415924;
				Var radius: Float = 4.12;
				Var perimeter: Float = Self.PI * 2 * Self.radius;
				Var area: Float = Self.radius * Self.radius * Self.PI;
				Var test: Float = ((10 + 2) * 4 - 5) / 6; 
			}
		}
        """
		expect = """Program([ClassDecl(Id(testMathExpressions),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(PI),FloatType,FloatLit(3.1415924)),VarDecl(Id(radius),FloatType,FloatLit(4.12)),VarDecl(Id(perimeter),FloatType,BinaryOp(*,BinaryOp(*,FieldAccess(Self(),Id(PI)),IntLit(2)),FieldAccess(Self(),Id(radius)))),VarDecl(Id(area),FloatType,BinaryOp(*,BinaryOp(*,FieldAccess(Self(),Id(radius)),FieldAccess(Self(),Id(radius))),FieldAccess(Self(),Id(PI)))),VarDecl(Id(test),FloatType,BinaryOp(/,BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLit(10),IntLit(2)),IntLit(4)),IntLit(5)),IntLit(6)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,316))
        
	def test17(self):
		input = """
        Class testClass {
			Var $testStatic: Int = 17;
			$testStaticMethod() {
				Var testVar: Float = 23.412e15;
			}
			main() {
				Val testConst: String = "test String";
			}
		}
        """
		expect = """Program([ClassDecl(Id(testClass),[AttributeDecl(Static,VarDecl(Id($testStatic),IntType,IntLit(17))),MethodDecl(Id($testStaticMethod),Static,[],Block([VarDecl(Id(testVar),FloatType,FloatLit(2.3412e+16))])),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(testConst),StringType,StringLit(test String))]))])])"""
		self.assertTrue(TestAST.test(input,expect,317))
    
	def test18(self):
		input = """
        Class testVar {
            test() {
				Val testArr: Array[Int, 0x4_12F_A216];
				Var testBool: Boolean;
				Val testString: String = "String to test";
            }
		}
        """
		expect = """Program([ClassDecl(Id(testVar),[MethodDecl(Id(test),Instance,[],Block([ConstDecl(Id(testArr),ArrayType(1093640726,IntType),None),VarDecl(Id(testBool),BoolType),ConstDecl(Id(testString),StringType,StringLit(String to test))]))])])"""
		self.assertTrue(TestAST.test(input,expect,318))
    
	def test19(self):
		input = """
        Class testConcatString{
            main() {
				Val subStr_1: String = "Spider-man";
				Val subStr_2: String = "into";
				Val subStr_3: String = "the";
				Val subStr_4: String = "Spider-verse";
				Val spider_verse: String = ((((((subStr_1 +. " ") +. subStr_2) +. " ") +. subStr_3) +. " ") +. subStr_4); 
			}
		}
        """
		expect = """Program([ClassDecl(Id(testConcatString),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(subStr_1),StringType,StringLit(Spider-man)),ConstDecl(Id(subStr_2),StringType,StringLit(into)),ConstDecl(Id(subStr_3),StringType,StringLit(the)),ConstDecl(Id(subStr_4),StringType,StringLit(Spider-verse)),ConstDecl(Id(spider_verse),StringType,BinaryOp(+.,BinaryOp(+.,BinaryOp(+.,BinaryOp(+.,BinaryOp(+.,BinaryOp(+.,Id(subStr_1),StringLit( )),Id(subStr_2)),StringLit( )),Id(subStr_3)),StringLit( )),Id(subStr_4)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,319))
        
	def test20(self):
		input = """
        Class testComment{
            main() {
				## 
					This is a
					multi-line
					comment
				##
				## so it won't be compiled ## 
            }
		}
        """
		expect = """Program([ClassDecl(Id(testComment),[MethodDecl(Id(main),Instance,[],Block([]))])])"""
		self.assertTrue(TestAST.test(input,expect,320))
    
	def test21(self):
		input = """
        Class testArray{
            main(){
				Var testArr: Array[Int, 5]= Array(4 , 12 , 2001 , 1915570 , 3005);
				Foreach (i In 1 .. 5){
					SOut.Println(testArr[i]);
				}
			}
		}
        """
		expect = """Program([ClassDecl(Id(testArray),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(testArr),ArrayType(5,IntType),[IntLit(4),IntLit(12),IntLit(2001),IntLit(1915570),IntLit(3005)]),For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([Call(Id(SOut),Id(Println),[ArrayCell(Id(testArr),[Id(i)])])])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,321))
    
	def test22(self):
		input = """
        Class testFor{
            main(){
				Val testArr: Array[Float, 5]= Array(4. , 12. , 2001. , 1915570. , 3005.);
				Var multi_arr: Array[Array[Int, 7],4];
				Foreach (i In 1 .. 4){
					multi_arr[i][i]= arr[i];
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(testFor),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(testArr),ArrayType(5,FloatType),[FloatLit(4.0),FloatLit(12.0),FloatLit(2001.0),FloatLit(1915570.0),FloatLit(3005.0)]),VarDecl(Id(multi_arr),ArrayType(4,ArrayType(7,IntType))),For(Id(i),IntLit(1),IntLit(4),IntLit(1),Block([AssignStmt(ArrayCell(Id(multi_arr),[Id(i),Id(i)]),ArrayCell(Id(arr),[Id(i)]))])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,322))
        
	def test23(self):
		input = """
        Class testNestedFor{
            main(){
				Val testArr: Array[Float, 5]= Array(4. , 12. , 2001. , 1915570. , 3005.);
				Var multi_arr: Array[Array[Int, 7],4];
				Foreach (i In 1 .. 4){
					Foreach(j In 1 .. 7){
						multi_arr[i][j] = arr[j];
					}
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(testNestedFor),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(testArr),ArrayType(5,FloatType),[FloatLit(4.0),FloatLit(12.0),FloatLit(2001.0),FloatLit(1915570.0),FloatLit(3005.0)]),VarDecl(Id(multi_arr),ArrayType(4,ArrayType(7,IntType))),For(Id(i),IntLit(1),IntLit(4),IntLit(1),Block([For(Id(j),IntLit(1),IntLit(7),IntLit(1),Block([AssignStmt(ArrayCell(Id(multi_arr),[Id(i),Id(j)]),ArrayCell(Id(arr),[Id(j)]))])])])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,323))
    
	def test24(self):
		input = """
        Class testAlgorithms{
            selectionSort(arr: Array[Int, 100])
            {
				Var n: Int = arr.length();
			
				## One by one move boundary of unsorted subarray ##
				Foreach (i In 1 .. (n-1) By 1)
				{
					## Find the minimum element in unsorted array ##
					Var min_idx: Int = i;
					Foreach (j In (i+1) .. n By 1) {
						If (arr[j] < arr[min_idx]) {
							min_idx = j;
						}
					}
					## Swap the found minimum element with the first element ##
					Var temp: Int = arr[min_idx];
					arr[min_idx] = arr[i];
					arr[i] = temp;
				}
            }
            ## Prints the array ##
            printArray(arr: Array[Int, 100])
            {
				Val n: Int = arr.length();
				Foreach (i In 0 .. n By 1) {
					System.out.print(arr[i] + " ");
				}
				System.out.println();
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(selectionSort),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),IntLit(1),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([VarDecl(Id(min_idx),IntType,Id(i)),For(Id(j),BinaryOp(+,Id(i),IntLit(1)),Id(n),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[Id(min_idx)])),Block([AssignStmt(Id(min_idx),Id(j))]))])]),VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(min_idx)])),AssignStmt(ArrayCell(Id(arr),[Id(min_idx)]),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),Id(temp))])])])),MethodDecl(Id(printArray),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([ConstDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,ArrayCell(Id(arr),[Id(i)]),StringLit( ))])])]),Call(FieldAccess(Id(System),Id(out)),Id(println),[])]))])])"""
		self.assertTrue(TestAST.test(input,expect,324))
        
	def test25(self):
		input = """
        Class testAlgorithms {
            gcd(a: Int; b: Int) {
				If (b == 0) {
					Return a;
				}
				Return Self.gcd(b, a % b);
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(gcd),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(BinaryOp(==,Id(b),IntLit(0)),Block([Return(Id(a))])),Return(CallExpr(Self(),Id(gcd),[Id(b),BinaryOp(%,Id(a),Id(b))]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,325))
        
	def test26(self):
		input = """
        Class testAlgorithms {
            binarySearch(arr: Array[Int, 10]; l: Int; r: Int; x: Int) 
            { 
				If (r >= l) { 
					Var mid: Int = l + (r - l) / 2;  
					If (arr[mid] == x) {
						Return mid;
					}
					If (arr[mid] > x) {
						Return Self.binarySearch(arr, l, mid - 1, x);
					}
					Return Self.binarySearch(arr, mid + 1, r, x); 
				} 
				Return -1; 
            } 
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(binarySearch),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(l),IntType),param(Id(r),IntType),param(Id(x),IntType)],Block([If(BinaryOp(>=,Id(r),Id(l)),Block([VarDecl(Id(mid),IntType,BinaryOp(+,Id(l),BinaryOp(/,BinaryOp(-,Id(r),Id(l)),IntLit(2)))),If(BinaryOp(==,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(Id(mid))])),If(BinaryOp(>,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(CallExpr(Self(),Id(binarySearch),[Id(arr),Id(l),BinaryOp(-,Id(mid),IntLit(1)),Id(x)]))])),Return(CallExpr(Self(),Id(binarySearch),[Id(arr),BinaryOp(+,Id(mid),IntLit(1)),Id(r),Id(x)]))])),Return(UnaryOp(-,IntLit(1)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,326))
    
	def test27(self):
		input = """
        Class testAlgorithms {
            factorial(n: Int)
            {
				If (n == 0) {
					Return 1;
				}
                Return n * Self.factorial(n - 1);
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(1))])),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))])))]))])])"""
		self.assertTrue(TestAST.test(input,expect,327))
        
	def test28(self):
		input = """
        Class testAlgorithms {
            Fibonacci(n: Int)
            {
				If ((n == 1) || (n == 2)) {
					Return 1;
				}
				Return Self.Fibonacci(n - 1) + Self.Fibonacci(n - 2);
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(Fibonacci),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(n),IntLit(1)),BinaryOp(==,Id(n),IntLit(2))),Block([Return(IntLit(1))])),Return(BinaryOp(+,CallExpr(Self(),Id(Fibonacci),[BinaryOp(-,Id(n),IntLit(1))]),CallExpr(Self(),Id(Fibonacci),[BinaryOp(-,Id(n),IntLit(2))])))]))])])"""
		self.assertTrue(TestAST.test(input,expect,328))
        
	def test29(self):
		input = """
        Class testAlgorithms {
            SumRecursion(n: Int) {
				##
					sum = 1 + ... + n
				##
				If (n == 0) {
					Return 0;
				}
				Return n + Self.SumRecursion(n - 1);
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(SumRecursion),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(0))])),Return(BinaryOp(+,Id(n),CallExpr(Self(),Id(SumRecursion),[BinaryOp(-,Id(n),IntLit(1))])))]))])])"""
		self.assertTrue(TestAST.test(input,expect,329))
    
	def test30(self):
		input = """
        Class testAlgorithms {
            isPalRec(str: Array[String, 100]; s: Int; e: Int)
            {
				If (s == e) {
					Return True;
				}
				If (str[s] != str[e]) {
					Return False;
				}
				If (s < e + 1) {
					Return Self.isPalRec(str, s + 1, e - 1);
				}
				Return True;
            }
            
            isPalindrome(str: Array[String, 100])
            {
				Val n: Int = Str.strlen(str);
				If (n == 0) {
					Return True;
				}
				Return Self.isPalRec(str, 0, n - 1);
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(isPalRec),Instance,[param(Id(str),ArrayType(100,StringType)),param(Id(s),IntType),param(Id(e),IntType)],Block([If(BinaryOp(==,Id(s),Id(e)),Block([Return(BooleanLit(True))])),If(BinaryOp(!=,ArrayCell(Id(str),[Id(s)]),ArrayCell(Id(str),[Id(e)])),Block([Return(BooleanLit(False))])),If(BinaryOp(<,Id(s),BinaryOp(+,Id(e),IntLit(1))),Block([Return(CallExpr(Self(),Id(isPalRec),[Id(str),BinaryOp(+,Id(s),IntLit(1)),BinaryOp(-,Id(e),IntLit(1))]))])),Return(BooleanLit(True))])),MethodDecl(Id(isPalindrome),Instance,[param(Id(str),ArrayType(100,StringType))],Block([ConstDecl(Id(n),IntType,CallExpr(Id(Str),Id(strlen),[Id(str)])),If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(BooleanLit(True))])),Return(CallExpr(Self(),Id(isPalRec),[Id(str),IntLit(0),BinaryOp(-,Id(n),IntLit(1))]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,330))
    
	def test31(self):
		input = """
        Class testAlgorithms {
            reverseStr(str: Array[String, 100])
            {
				Val n: Int = str.length();
				
				## Swap character starting from two corners ##
				Foreach (i In 0 .. (n / 2) By 1) {
					str.swap(str[i], str[n - i - 1]);
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(reverseStr),Instance,[param(Id(str),ArrayType(100,StringType))],Block([ConstDecl(Id(n),IntType,CallExpr(Id(str),Id(length),[])),For(Id(i),IntLit(0),BinaryOp(/,Id(n),IntLit(2)),IntLit(1),Block([Call(Id(str),Id(swap),[ArrayCell(Id(str),[Id(i)]),ArrayCell(Id(str),[BinaryOp(-,BinaryOp(-,Id(n),Id(i)),IntLit(1))])])])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,331))
        
	def test32(self):
		input = """
        Class testAlgorithms {
            search(arr: Array[Int, 100]; n: Int; x: Int)
            {
				Var i: Int;
				Foreach (i In 0 .. n By 1) {
					If (arr[i] == x) {
						Return i;
					}
				}
				Return -1;
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(search),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(x),IntType)],Block([VarDecl(Id(i),IntType),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([If(BinaryOp(==,ArrayCell(Id(arr),[Id(i)]),Id(x)),Block([Return(Id(i))]))])]),Return(UnaryOp(-,IntLit(1)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,332))
    
	def test33(self):
		input = """
        Class testAlgorithms {
            getMax(arr: Array[Int, 10]; n: Int)
            {
				Var mx: Int = arr[0];
				Foreach (i In 1 .. n By 1) {
					If (arr[i] > mx) {
						mx = arr[i];
					}
				}
				Return mx;
            }
            countSort(arr: Array[Int, 100]; n: Int; exp: Int)
            {
				Var output: Array[Int, 100];
				Var count: Array[Int, 10] = Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
				
				## Store count of occurrences in count[] ##
				Foreach (i In 0 .. n By 1) {
					Val temp: Int = (arr[i] / exp) % 10;
					count[temp] = count[temp] + 1;
				}
				
            
				## Change count[i] so that count[i] now contains actual
				#  position of this digit in output[] ##
				Foreach (i In 1 .. 10 By 1) {
					count[i] = count[i] + count[i - 1];
				}
				## Build the output array ##
				Foreach (i In (n - 1) .. 0 By -1) {
					Val temp: Int = (arr[i] / exp) % 10;
					output[count[temp] - 1] = arr[i];
					count[temp] = count[temp] - 1;
				}
            
				## Copy the output array to arr[], so that arr[] now
				#  contains sorted numbers according to current digit ##
				Foreach (i In 0 .. n By 1) {
					arr[i] = output[i];
				}
            }
            
            radixsort(arr: Array[Int, 100]; n: Int)
            {
				## Find the maximum number to know number of digits ##
				Var m: Int = Self.getMax(arr, n);
				
				## Do counting sort for every digit. Note that instead
				#  of passing digit number, exp is passed. exp is 10^i
				#  where i is current digit number ##
				Foreach (exp In 1 .. (m / exp > 0) By Math.times(10)) {
					Self.countSort(arr, n, exp);
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(getMax),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(mx),IntType,ArrayCell(Id(arr),[IntLit(0)])),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(i)]),Id(mx)),Block([AssignStmt(Id(mx),ArrayCell(Id(arr),[Id(i)]))]))])]),Return(Id(mx))])),MethodDecl(Id(countSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(exp),IntType)],Block([VarDecl(Id(output),ArrayType(100,IntType)),VarDecl(Id(count),ArrayType(10,IntType),[IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0)]),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([ConstDecl(Id(temp),IntType,BinaryOp(%,BinaryOp(/,ArrayCell(Id(arr),[Id(i)]),Id(exp)),IntLit(10))),AssignStmt(ArrayCell(Id(count),[Id(temp)]),BinaryOp(+,ArrayCell(Id(count),[Id(temp)]),IntLit(1)))])]),For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([AssignStmt(ArrayCell(Id(count),[Id(i)]),BinaryOp(+,ArrayCell(Id(count),[Id(i)]),ArrayCell(Id(count),[BinaryOp(-,Id(i),IntLit(1))])))])]),For(Id(i),BinaryOp(-,Id(n),IntLit(1)),IntLit(0),UnaryOp(-,IntLit(1)),Block([ConstDecl(Id(temp),IntType,BinaryOp(%,BinaryOp(/,ArrayCell(Id(arr),[Id(i)]),Id(exp)),IntLit(10))),AssignStmt(ArrayCell(Id(output),[BinaryOp(-,ArrayCell(Id(count),[Id(temp)]),IntLit(1))]),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(count),[Id(temp)]),BinaryOp(-,ArrayCell(Id(count),[Id(temp)]),IntLit(1)))])]),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(output),[Id(i)]))])])])),MethodDecl(Id(radixsort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(m),IntType,CallExpr(Self(),Id(getMax),[Id(arr),Id(n)])),For(Id(exp),IntLit(1),BinaryOp(>,BinaryOp(/,Id(m),Id(exp)),IntLit(0)),CallExpr(Id(Math),Id(times),[IntLit(10)]),Block([Call(Self(),Id(countSort),[Id(arr),Id(n),Id(exp)])])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,333))
        
	def test34(self):
		input = """
        Class testAlgorithms {
            bubbleSort(arr: Array[Int, 100]; n: Int)
            {
				## Base case ##
				If (n == 1) {
					Return;
				}
            
				## One pass of bubble sort. After this pass, the largest element is moved (or bubbled) to end. ##
				Foreach (i In 0 .. (n-1) By 1) {
					If (arr[i] > arr[i+1]) {
						Algorithms.swap(arr[i], arr[i+1]);
					}
				}
				## Largest element is fixed, recur for remaining array ##
				Self.bubbleSort(arr, n-1);
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(bubbleSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(1)),Block([Return()])),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])),Block([Call(Id(Algorithms),Id(swap),[ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])])]))])]),Call(Self(),Id(bubbleSort),[Id(arr),BinaryOp(-,Id(n),IntLit(1))])]))])])"""
		self.assertTrue(TestAST.test(input,expect,334))
        
	def test35(self):
		input = """
        Class testAlgorithms {
            merge(array: Array[Int, 100]; left: Int; mid: Int; right: Int)
            {
				Val subArrayOne: Int = mid - left + 1;
				Val subArrayTwo: Int = right - mid;
				
				## Create temp arrays ##
				Var leftArray, rightArray: Array[Int, 50];
				
				## Copy data to temp arrays leftArray[] and rightArray[] ##
				Foreach (i In 0 .. subArrayOne By 1) {
					leftArray[i] = array[left + i];
				}
				Foreach (j In 0 .. subArrayTwo By 1) {
					rightArray[j] = array[mid + 1 + j];
				}
				
				Var indexOfSubArrayOne, indexOfSubArrayTwo, indexOfMergedArray: Int = 0, 0, left;
				
				## Merge the temp arrays back into array[left..right] ##
				Foreach (i In 0 .. ((indexOfSubArrayOne < subArrayOne) && (indexOfSubArrayTwo < subArrayTwo)) By 1) {
					If (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
						array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
						indexOfSubArrayOne = indexOfSubArrayOne + 1;
					}
					Else {
						array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
						indexOfSubArrayTwo = indexOfSubArrayTwo + 1;
					}
					indexOfMergedArray = indexOfMergedArray + 1;
				}
				## Copy the remaining elements of left[], if there are any ##
				Foreach (i In indexOfSubArrayOne .. (indexOfSubArrayOne < subArrayOne) By 1)
				{
					array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
					indexOfSubArrayOne = indexOfSubArrayOne + 1;
					indexOfMergedArray = indexOfMergedArray + 1;
				}
				## Copy the remaining elements of right[], if there are any ##
				Foreach (i In indexOfSubArrayTwo .. (indexOfSubArrayTwo < subArrayTwo) By 1) {
					array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
					indexOfSubArrayTwo = indexOfSubArrayTwo + 1;
					indexOfMergedArray = indexOfMergedArray + 1;
				}
            }
            
            ## begin is for left index and end is right index of the sub-array of arr to be sorted ##
            mergeSort(array: Array[Int, 100]; begin: Int; end: Int)
            {
				If (begin >= end) {
					Return; 
				}
				Var mid: Int = begin + (end - begin) / 2;
				Self.mergeSort(array, begin, mid);
				Self.mergeSort(array, mid + 1, end);
				Self.merge(array, begin, mid, end);
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(merge),Instance,[param(Id(array),ArrayType(100,IntType)),param(Id(left),IntType),param(Id(mid),IntType),param(Id(right),IntType)],Block([ConstDecl(Id(subArrayOne),IntType,BinaryOp(+,BinaryOp(-,Id(mid),Id(left)),IntLit(1))),ConstDecl(Id(subArrayTwo),IntType,BinaryOp(-,Id(right),Id(mid))),VarDecl(Id(leftArray),ArrayType(50,IntType)),VarDecl(Id(rightArray),ArrayType(50,IntType)),For(Id(i),IntLit(0),Id(subArrayOne),IntLit(1),Block([AssignStmt(ArrayCell(Id(leftArray),[Id(i)]),ArrayCell(Id(array),[BinaryOp(+,Id(left),Id(i))]))])]),For(Id(j),IntLit(0),Id(subArrayTwo),IntLit(1),Block([AssignStmt(ArrayCell(Id(rightArray),[Id(j)]),ArrayCell(Id(array),[BinaryOp(+,BinaryOp(+,Id(mid),IntLit(1)),Id(j))]))])]),VarDecl(Id(indexOfSubArrayOne),IntType,IntLit(0)),VarDecl(Id(indexOfSubArrayTwo),IntType,IntLit(0)),VarDecl(Id(indexOfMergedArray),IntType,Id(left)),For(Id(i),IntLit(0),BinaryOp(&&,BinaryOp(<,Id(indexOfSubArrayOne),Id(subArrayOne)),BinaryOp(<,Id(indexOfSubArrayTwo),Id(subArrayTwo))),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)])),AssignStmt(Id(indexOfSubArrayOne),BinaryOp(+,Id(indexOfSubArrayOne),IntLit(1)))]),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),AssignStmt(Id(indexOfSubArrayTwo),BinaryOp(+,Id(indexOfSubArrayTwo),IntLit(1)))])),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])]),For(Id(i),Id(indexOfSubArrayOne),BinaryOp(<,Id(indexOfSubArrayOne),Id(subArrayOne)),IntLit(1),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)])),AssignStmt(Id(indexOfSubArrayOne),BinaryOp(+,Id(indexOfSubArrayOne),IntLit(1))),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])]),For(Id(i),Id(indexOfSubArrayTwo),BinaryOp(<,Id(indexOfSubArrayTwo),Id(subArrayTwo)),IntLit(1),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),AssignStmt(Id(indexOfSubArrayTwo),BinaryOp(+,Id(indexOfSubArrayTwo),IntLit(1))),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])])])),MethodDecl(Id(mergeSort),Instance,[param(Id(array),ArrayType(100,IntType)),param(Id(begin),IntType),param(Id(end),IntType)],Block([If(BinaryOp(>=,Id(begin),Id(end)),Block([Return()])),VarDecl(Id(mid),IntType,BinaryOp(+,Id(begin),BinaryOp(/,BinaryOp(-,Id(end),Id(begin)),IntLit(2)))),Call(Self(),Id(mergeSort),[Id(array),Id(begin),Id(mid)]),Call(Self(),Id(mergeSort),[Id(array),BinaryOp(+,Id(mid),IntLit(1)),Id(end)]),Call(Self(),Id(merge),[Id(array),Id(begin),Id(mid),Id(end)])]))])])"""
		self.assertTrue(TestAST.test(input,expect,335))
    
	def test36(self):
		input = """
        Class testAlgorithms {
            swap(arr: Array[Int, 100]; i: Int; j: Int)
            {
				Var temp: Int = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
			
			## This function takes last element as pivot, places
			the pivot element at its correct position in sorted
			array, and places all smaller (smaller than pivot)
			to left of pivot and all greater elements to right
			of pivot ##
			partition(arr: Array[Int, 100]; low: Int; high: Int)
			{
				Var pivot: Int = arr[high];
				
				## Index of smaller element and indicates the right position of pivot found so far ##
				Var i: Int = (low - 1);
				Foreach (j In low .. (high - 1) By 1)
				{
					If (arr[j] < pivot)
					{
						i = i + 1;
						Self.swap(arr, i, j);
					}
				}
				Self.swap(arr, i + 1, high);
				Return (i + 1);
			}
				
			## The main function that implements QuickSort
				arr[] --> Array to be sorted,
				low --> Starting index,
				high --> Ending index
			##
			quickSort(arr: Array[Int, 100]; low: Int; high: Int)
			{
				If (low < high)
				{
					Var pi: Int = Self.partition(arr, low, high);
					Self.quickSort(arr, low, pi - 1);
					Self.quickSort(arr, pi + 1, high);
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(swap),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(i),IntType),param(Id(j),IntType)],Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))])),MethodDecl(Id(partition),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),For(Id(j),Id(low),BinaryOp(-,Id(high),IntLit(1)),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Call(Self(),Id(swap),[Id(arr),Id(i),Id(j)])]))])]),Call(Self(),Id(swap),[Id(arr),BinaryOp(+,Id(i),IntLit(1)),Id(high)]),Return(BinaryOp(+,Id(i),IntLit(1)))])),MethodDecl(Id(quickSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(<,Id(low),Id(high)),Block([VarDecl(Id(pi),IntType,CallExpr(Self(),Id(partition),[Id(arr),Id(low),Id(high)])),Call(Self(),Id(quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Self(),Id(quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,336))
        
	def test37(self):
		input = """
        Class testAlgorithms {
            Val $RUN: Int = 32;

            insertionSort(arr: Array[Int, 100]; left: Int; right: Int)
            {
				Foreach (i In (left + 1) .. right By 1)
				{
					Var temp: Int = arr[i];
					Var j: Int = i - 1;
					Foreach (j In (i - 1) .. left By -1) {
						If (arr[j] > temp) {
							Break;
						}
						arr[j+1] = arr[j];
						j = j + 1;
					}
					arr[j+1] = temp;
				}
            }

            merge(array: Array[Int, 100]; left: Int; mid: Int; right: Int)
            {
				Val subArrayOne: Int = mid - left + 1;
				Val subArrayTwo: Int = right - mid;
            
				## Create temp arrays ##
				Var leftArray, rightArray: Array[Int, 50];
            
				## Copy data to temp arrays leftArray[] and rightArray[] ##
				Foreach (i In 0 .. subArrayOne By 1) {
					leftArray[i] = array[left + i];
				}
				Foreach (j In 0 .. subArrayTwo By 1) {
					rightArray[j] = array[mid + 1 + j];
				}
            
				Var indexOfSubArrayOne, indexOfSubArrayTwo, indexOfMergedArray: Int = 0, 0, left;
            
				## Merge the temp arrays back into array[left..right] ##
				Foreach (i In 0 .. ((indexOfSubArrayOne < subArrayOne) && (indexOfSubArrayTwo < subArrayTwo)) By 1) {
					If (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
						array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
						indexOfSubArrayOne = indexOfSubArrayOne + 1;
					}
					Else {
						array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
						indexOfSubArrayTwo = indexOfSubArrayTwo + 1;
					}
					indexOfMergedArray = indexOfMergedArray + 1;
				}
				## Copy the remaining elements of left[], if there are any ##
				Foreach (i In indexOfSubArrayOne .. (indexOfSubArrayOne < subArrayOne) By 1)
				{
					array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
					indexOfSubArrayOne = indexOfSubArrayOne + 1;
					indexOfMergedArray = indexOfMergedArray + 1;
				}
				## Copy the remaining elements of right[], if there are any ##
				Foreach (i In indexOfSubArrayTwo .. (indexOfSubArrayTwo < subArrayTwo) By 1) {
					array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
					indexOfSubArrayTwo = indexOfSubArrayTwo + 1;
					indexOfMergedArray = indexOfMergedArray + 1;
				}
            }

            ## Iterative Timsort function to sort the array[0...n-1] (similar to merge sort) ##
            timSort(arr: Array[Int, 100]; n: Int)
            {
				Foreach (i In 0 .. n By testAlgorithms::$RUN) {
					Self.insertionSort(arr, i, Algorithms.min((i + testAlgorithms::$RUN - 1), (n - 1)));
				}
				Foreach (size In RUN .. n)
				{
					Foreach (left In 0 .. n By (2*size))
					{
						Var mid: Int = left + size - 1;
						Var right: Int = Algorithms.min((left + 2*size - 1), (n-1));
						If (mid < right) {
                        Self.merge(arr, left, mid, right);
						}
					}
                  	size = size * 2;
				}
            }
        }
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[AttributeDecl(Static,ConstDecl(Id($RUN),IntType,IntLit(32))),MethodDecl(Id(insertionSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(left),IntType),param(Id(right),IntType)],Block([For(Id(i),BinaryOp(+,Id(left),IntLit(1)),Id(right),IntLit(1),Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(i)])),VarDecl(Id(j),IntType,BinaryOp(-,Id(i),IntLit(1))),For(Id(j),BinaryOp(-,Id(i),IntLit(1)),Id(left),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(temp)),Block([Break])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))])]),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(temp))])])])),MethodDecl(Id(merge),Instance,[param(Id(array),ArrayType(100,IntType)),param(Id(left),IntType),param(Id(mid),IntType),param(Id(right),IntType)],Block([ConstDecl(Id(subArrayOne),IntType,BinaryOp(+,BinaryOp(-,Id(mid),Id(left)),IntLit(1))),ConstDecl(Id(subArrayTwo),IntType,BinaryOp(-,Id(right),Id(mid))),VarDecl(Id(leftArray),ArrayType(50,IntType)),VarDecl(Id(rightArray),ArrayType(50,IntType)),For(Id(i),IntLit(0),Id(subArrayOne),IntLit(1),Block([AssignStmt(ArrayCell(Id(leftArray),[Id(i)]),ArrayCell(Id(array),[BinaryOp(+,Id(left),Id(i))]))])]),For(Id(j),IntLit(0),Id(subArrayTwo),IntLit(1),Block([AssignStmt(ArrayCell(Id(rightArray),[Id(j)]),ArrayCell(Id(array),[BinaryOp(+,BinaryOp(+,Id(mid),IntLit(1)),Id(j))]))])]),VarDecl(Id(indexOfSubArrayOne),IntType,IntLit(0)),VarDecl(Id(indexOfSubArrayTwo),IntType,IntLit(0)),VarDecl(Id(indexOfMergedArray),IntType,Id(left)),For(Id(i),IntLit(0),BinaryOp(&&,BinaryOp(<,Id(indexOfSubArrayOne),Id(subArrayOne)),BinaryOp(<,Id(indexOfSubArrayTwo),Id(subArrayTwo))),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)])),AssignStmt(Id(indexOfSubArrayOne),BinaryOp(+,Id(indexOfSubArrayOne),IntLit(1)))]),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),AssignStmt(Id(indexOfSubArrayTwo),BinaryOp(+,Id(indexOfSubArrayTwo),IntLit(1)))])),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])]),For(Id(i),Id(indexOfSubArrayOne),BinaryOp(<,Id(indexOfSubArrayOne),Id(subArrayOne)),IntLit(1),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)])),AssignStmt(Id(indexOfSubArrayOne),BinaryOp(+,Id(indexOfSubArrayOne),IntLit(1))),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])]),For(Id(i),Id(indexOfSubArrayTwo),BinaryOp(<,Id(indexOfSubArrayTwo),Id(subArrayTwo)),IntLit(1),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),AssignStmt(Id(indexOfSubArrayTwo),BinaryOp(+,Id(indexOfSubArrayTwo),IntLit(1))),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])])])),MethodDecl(Id(timSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([For(Id(i),IntLit(0),Id(n),FieldAccess(Id(testAlgorithms),Id($RUN)),Block([Call(Self(),Id(insertionSort),[Id(arr),Id(i),CallExpr(Id(Algorithms),Id(min),[BinaryOp(-,BinaryOp(+,Id(i),FieldAccess(Id(testAlgorithms),Id($RUN))),IntLit(1)),BinaryOp(-,Id(n),IntLit(1))])])])]),For(Id(size),Id(RUN),Id(n),IntLit(1),Block([For(Id(left),IntLit(0),Id(n),BinaryOp(*,IntLit(2),Id(size)),Block([VarDecl(Id(mid),IntType,BinaryOp(-,BinaryOp(+,Id(left),Id(size)),IntLit(1))),VarDecl(Id(right),IntType,CallExpr(Id(Algorithms),Id(min),[BinaryOp(-,BinaryOp(+,Id(left),BinaryOp(*,IntLit(2),Id(size))),IntLit(1)),BinaryOp(-,Id(n),IntLit(1))])),If(BinaryOp(<,Id(mid),Id(right)),Block([Call(Self(),Id(merge),[Id(arr),Id(left),Id(mid),Id(right)])]))])]),AssignStmt(Id(size),BinaryOp(*,Id(size),IntLit(2)))])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,337))
        
	def test38(self):
		input = """
        Class Node {
            Var data: Int;
            Var next: Node;
            Constructor(d: Int)
            {
				Self.data = d;
				Self.next = Null;
            }
		}
		Class LinkedList: Node {
            Var head: Node;
            
            main(args: Array[String, 2])
            {
				Var llist: LinkedList = New LinkedList();
				llist.head = New Node(1);
				Var second: Node = New Node(2);
				Var third: Node = New Node(3);
				llist.head.next = second;
            }
		}
        """
		expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,VarDecl(Id(next),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(d),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(data)),Id(d)),AssignStmt(FieldAccess(Self(),Id(next)),NullLiteral())]))]),ClassDecl(Id(LinkedList),Id(Node),[AttributeDecl(Instance,VarDecl(Id(head),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,StringType))],Block([VarDecl(Id(llist),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(llist),Id(head)),NewExpr(Id(Node),[IntLit(1)])),VarDecl(Id(second),ClassType(Id(Node)),NewExpr(Id(Node),[IntLit(2)])),VarDecl(Id(third),ClassType(Id(Node)),NewExpr(Id(Node),[IntLit(3)])),AssignStmt(FieldAccess(FieldAccess(Id(llist),Id(head)),Id(next)),Id(second))]))])])"""
		self.assertTrue(TestAST.test(input,expect,338))
    
	def test39(self):
		input = """
        Class Node {
            Var data: Int;
            Var next: Node;
            Constructor(d: Int)
            {
				Self.data = d;
				Self.next = Null;
            }
		}
		Class LinkedList: Node {
            Var head: Node;
            
            push(new_data: Int)
            {
				Var new_node: Node = New Node(new_data);
				new_node.next = head;
				head = new_node;
            }
        
            ## Inserts a new node after the given prev_node. ##
            insertAfter(prev_node: Node; new_data: Int)
            {
				If (prev_node == Null)
				{
					System.out.println("The given previous node cannot be null");
					Return;
				}
				Var new_node: Node = New Node(new_data);
				new_node.next = prev_node.next;
				prev_node.next = new_node;
            }
            
            ## Appends a new node at the end.  This method is
            defined inside LinkedList class shown above ##
            append(new_data: Int)
            {
				Var new_node: Node = New Node(new_data);
				If (Self.head == null)
				{
					Self.head = New Node(new_data);
					Return;
				}
				new_node.next = Null;
				Var last: Node = head;
				Foreach (last In (Self.head) .. (last.next != null)) {
					last = last.next;
				} 
				last.next = new_node;
				Return;
            }
        
            ## This function prints contents of linked list starting from
			the given node ##
            printList()
            {
				Foreach (tnode In (Self.head) .. (tnode.next != null))
				{
					System.out.print(tnode.data + " ");
					tnode = tnode.next;
				}
            }
        
            ## Driver program to test above functions. Ideally this function
			should be in a separate user class.  It is kept here to keep
			code compact ##
            main(args: Array[String, 2])
            {
				Var llist: LinkedList = New LinkedList();
				llist.append(6);
				llist.push(7);
				llist.push(1);
				llist.append(4);
				llist.insertAfter(llist.head.next, 8);
				System.out.println("Created Linked list is: ");
				llist.printList();
            }
		}
        """
		expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,VarDecl(Id(next),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(d),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(data)),Id(d)),AssignStmt(FieldAccess(Self(),Id(next)),NullLiteral())]))]),ClassDecl(Id(LinkedList),Id(Node),[AttributeDecl(Instance,VarDecl(Id(head),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(push),Instance,[param(Id(new_data),IntType)],Block([VarDecl(Id(new_node),ClassType(Id(Node)),NewExpr(Id(Node),[Id(new_data)])),AssignStmt(FieldAccess(Id(new_node),Id(next)),Id(head)),AssignStmt(Id(head),Id(new_node))])),MethodDecl(Id(insertAfter),Instance,[param(Id(prev_node),ClassType(Id(Node))),param(Id(new_data),IntType)],Block([If(BinaryOp(==,Id(prev_node),NullLiteral()),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(The given previous node cannot be null)]),Return()])),VarDecl(Id(new_node),ClassType(Id(Node)),NewExpr(Id(Node),[Id(new_data)])),AssignStmt(FieldAccess(Id(new_node),Id(next)),FieldAccess(Id(prev_node),Id(next))),AssignStmt(FieldAccess(Id(prev_node),Id(next)),Id(new_node))])),MethodDecl(Id(append),Instance,[param(Id(new_data),IntType)],Block([VarDecl(Id(new_node),ClassType(Id(Node)),NewExpr(Id(Node),[Id(new_data)])),If(BinaryOp(==,FieldAccess(Self(),Id(head)),Id(null)),Block([AssignStmt(FieldAccess(Self(),Id(head)),NewExpr(Id(Node),[Id(new_data)])),Return()])),AssignStmt(FieldAccess(Id(new_node),Id(next)),NullLiteral()),VarDecl(Id(last),ClassType(Id(Node)),Id(head)),For(Id(last),FieldAccess(Self(),Id(head)),BinaryOp(!=,FieldAccess(Id(last),Id(next)),Id(null)),IntLit(1),Block([AssignStmt(Id(last),FieldAccess(Id(last),Id(next)))])]),AssignStmt(FieldAccess(Id(last),Id(next)),Id(new_node)),Return()])),MethodDecl(Id(printList),Instance,[],Block([For(Id(tnode),FieldAccess(Self(),Id(head)),BinaryOp(!=,FieldAccess(Id(tnode),Id(next)),Id(null)),IntLit(1),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,FieldAccess(Id(tnode),Id(data)),StringLit( ))]),AssignStmt(Id(tnode),FieldAccess(Id(tnode),Id(next)))])])])),MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,StringType))],Block([VarDecl(Id(llist),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),Call(Id(llist),Id(append),[IntLit(6)]),Call(Id(llist),Id(push),[IntLit(7)]),Call(Id(llist),Id(push),[IntLit(1)]),Call(Id(llist),Id(append),[IntLit(4)]),Call(Id(llist),Id(insertAfter),[FieldAccess(FieldAccess(Id(llist),Id(head)),Id(next)),IntLit(8)]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Created Linked list is: )]),Call(Id(llist),Id(printList),[])]))])])"""
		self.assertTrue(TestAST.test(input,expect,339))
    
	def test40(self):
		input = """
        Class Node
        {
            Var key: Int;
            Var left, right: Node;

            Node(item: Int)
            {
				key = item;
				left = Null;
				right = Null;
            }
		}

		Class BinaryTree
		{
            Var root: Node;

            Constructor(key: Int)
            {
				Self.root = New Node(key);
            }

            Constructor()
            {
				Self.root = null;
            }

            main(args: Array[String, 2])
            {
				Var tree: BinaryTree = New BinaryTree();
				tree.root = New Node(1);
				tree.root.left = New Node(2);
				tree.root.right = New Node(3);
				tree.root.left.left = New Node(4);
            }
        }
        """
		expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Instance,VarDecl(Id(key),IntType)),AttributeDecl(Instance,VarDecl(Id(left),ClassType(Id(Node)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(right),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(Node),Instance,[param(Id(item),IntType)],Block([AssignStmt(Id(key),Id(item)),AssignStmt(Id(left),NullLiteral()),AssignStmt(Id(right),NullLiteral())]))]),ClassDecl(Id(BinaryTree),[AttributeDecl(Instance,VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(key),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(root)),NewExpr(Id(Node),[Id(key)]))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(root)),Id(null))])),MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,StringType))],Block([VarDecl(Id(tree),ClassType(Id(BinaryTree)),NewExpr(Id(BinaryTree),[])),AssignStmt(FieldAccess(Id(tree),Id(root)),NewExpr(Id(Node),[IntLit(1)])),AssignStmt(FieldAccess(FieldAccess(Id(tree),Id(root)),Id(left)),NewExpr(Id(Node),[IntLit(2)])),AssignStmt(FieldAccess(FieldAccess(Id(tree),Id(root)),Id(right)),NewExpr(Id(Node),[IntLit(3)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(tree),Id(root)),Id(left)),Id(left)),NewExpr(Id(Node),[IntLit(4)]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,340))
    
	def test41(self):
		input = """
        Class Node
		{
            Var key: Int;
            Var left, right: Node;

            Node(item: Int)
            {
				key = item;
				left = Null;
				right = Null;
            }
		}

        Class BinaryTree {
            Var root: Node;
            printLevelOrder()
            {
				Var queue: LinkedList = New LinkedList();
				queue.add(Self.root);
				If (!queue.isEmpty()) {
					Var tempNode: Node = queue.poll();
					System.out.print(tempNode.data + " ");
		
					If (tempNode.left != Null) {
						queue.add(tempNode.left);
					}

					If (tempNode.right != null) {
						queue.add(tempNode.right);
					}
				}
            }
        
            main(args: Array[String, 2])
            {
				Var tree_level: BinaryTree = New BinaryTree();
				tree_level.root = New Node(1);
				tree_level.root.left = New Node(2);
				tree_level.root.right = New Node(3);
				tree_level.root.left.left = New Node(4);
				tree_level.root.left.right = New Node(5);
			
				System.out.println("Level order traversal of binary tree is - ");
				tree_level.printLevelOrder();
            }
		}
        """
		expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Instance,VarDecl(Id(key),IntType)),AttributeDecl(Instance,VarDecl(Id(left),ClassType(Id(Node)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(right),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(Node),Instance,[param(Id(item),IntType)],Block([AssignStmt(Id(key),Id(item)),AssignStmt(Id(left),NullLiteral()),AssignStmt(Id(right),NullLiteral())]))]),ClassDecl(Id(BinaryTree),[AttributeDecl(Instance,VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(printLevelOrder),Instance,[],Block([VarDecl(Id(queue),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),Call(Id(queue),Id(add),[FieldAccess(Self(),Id(root))]),If(UnaryOp(!,CallExpr(Id(queue),Id(isEmpty),[])),Block([VarDecl(Id(tempNode),ClassType(Id(Node)),CallExpr(Id(queue),Id(poll),[])),Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,FieldAccess(Id(tempNode),Id(data)),StringLit( ))]),If(BinaryOp(!=,FieldAccess(Id(tempNode),Id(left)),NullLiteral()),Block([Call(Id(queue),Id(add),[FieldAccess(Id(tempNode),Id(left))])])),If(BinaryOp(!=,FieldAccess(Id(tempNode),Id(right)),Id(null)),Block([Call(Id(queue),Id(add),[FieldAccess(Id(tempNode),Id(right))])]))]))])),MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,StringType))],Block([VarDecl(Id(tree_level),ClassType(Id(BinaryTree)),NewExpr(Id(BinaryTree),[])),AssignStmt(FieldAccess(Id(tree_level),Id(root)),NewExpr(Id(Node),[IntLit(1)])),AssignStmt(FieldAccess(FieldAccess(Id(tree_level),Id(root)),Id(left)),NewExpr(Id(Node),[IntLit(2)])),AssignStmt(FieldAccess(FieldAccess(Id(tree_level),Id(root)),Id(right)),NewExpr(Id(Node),[IntLit(3)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(tree_level),Id(root)),Id(left)),Id(left)),NewExpr(Id(Node),[IntLit(4)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(tree_level),Id(root)),Id(left)),Id(right)),NewExpr(Id(Node),[IntLit(5)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Level order traversal of binary tree is - )]),Call(Id(tree_level),Id(printLevelOrder),[])]))])])"""
		self.assertTrue(TestAST.test(input,expect,341))
        
	def test42(self):
		input = """
        Class Node
		{
            Var key: Int;
            Var left, right: Node;

            Node(item: Int)
            {
				key = item;
				left = Null;
				right = Null;
            }
		}

		Class BinaryTree
		{
            Var root: Node;

            Constructor(key: Int)
            {
				Self.root = New Node(key);
            }

            Constructor()
            {
				Self.root = Null;
            }

            printPostorder(node: Node)
            {
				If (node == Null) {
					Return;
				}
				Self.printPostorder(node.left);
				Self.printPostorder(node.right);
				System.out.print(node.key + " ");
            }
            printInorder(node: Node)
            {
				If (node == Null) {
					Return;
				}
				Self.printInorder(node.left);
				System.out.print(node.key + " ");
				Self.printInorder(node.right);
            }
            printPreorder(node: Node)
            {
				If (node == Null) {
					Return;
				}
				System.out.print(node.key + " ");
				Self.printPreorder(node.left);
				Self.printPreorder(node.right);
            }

            printPostorder() { Self.printPostorder(root); }
            printInorder() { Self.printInorder(root); }
            printPreorder() { Self.printPreorder(root); }
            
            main(args: Array[String, 2])
            {
				Var tree: BinaryTree = New BinaryTree();
				tree.root = New Node(1);
				tree.root.left = New Node(2);
				tree.root.right = New Node(3);
				tree.root.left.left = New Node(4);
				tree.root.left.right = New Node(5);

				System.out.println("Preorder traversal of binary tree is ");
				tree.printPreorder();
				System.out.println("Inorder traversal of binary tree is ");
				tree.printInorder();
				System.out.println("Postorder traversal of binary tree is ");
				tree.printPostorder();
            }
		}
        """
		expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Instance,VarDecl(Id(key),IntType)),AttributeDecl(Instance,VarDecl(Id(left),ClassType(Id(Node)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(right),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(Node),Instance,[param(Id(item),IntType)],Block([AssignStmt(Id(key),Id(item)),AssignStmt(Id(left),NullLiteral()),AssignStmt(Id(right),NullLiteral())]))]),ClassDecl(Id(BinaryTree),[AttributeDecl(Instance,VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(key),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(root)),NewExpr(Id(Node),[Id(key)]))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(root)),NullLiteral())])),MethodDecl(Id(printPostorder),Instance,[param(Id(node),ClassType(Id(Node)))],Block([If(BinaryOp(==,Id(node),NullLiteral()),Block([Return()])),Call(Self(),Id(printPostorder),[FieldAccess(Id(node),Id(left))]),Call(Self(),Id(printPostorder),[FieldAccess(Id(node),Id(right))]),Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,FieldAccess(Id(node),Id(key)),StringLit( ))])])),MethodDecl(Id(printInorder),Instance,[param(Id(node),ClassType(Id(Node)))],Block([If(BinaryOp(==,Id(node),NullLiteral()),Block([Return()])),Call(Self(),Id(printInorder),[FieldAccess(Id(node),Id(left))]),Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,FieldAccess(Id(node),Id(key)),StringLit( ))]),Call(Self(),Id(printInorder),[FieldAccess(Id(node),Id(right))])])),MethodDecl(Id(printPreorder),Instance,[param(Id(node),ClassType(Id(Node)))],Block([If(BinaryOp(==,Id(node),NullLiteral()),Block([Return()])),Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,FieldAccess(Id(node),Id(key)),StringLit( ))]),Call(Self(),Id(printPreorder),[FieldAccess(Id(node),Id(left))]),Call(Self(),Id(printPreorder),[FieldAccess(Id(node),Id(right))])])),MethodDecl(Id(printPostorder),Instance,[],Block([Call(Self(),Id(printPostorder),[Id(root)])])),MethodDecl(Id(printInorder),Instance,[],Block([Call(Self(),Id(printInorder),[Id(root)])])),MethodDecl(Id(printPreorder),Instance,[],Block([Call(Self(),Id(printPreorder),[Id(root)])])),MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,StringType))],Block([VarDecl(Id(tree),ClassType(Id(BinaryTree)),NewExpr(Id(BinaryTree),[])),AssignStmt(FieldAccess(Id(tree),Id(root)),NewExpr(Id(Node),[IntLit(1)])),AssignStmt(FieldAccess(FieldAccess(Id(tree),Id(root)),Id(left)),NewExpr(Id(Node),[IntLit(2)])),AssignStmt(FieldAccess(FieldAccess(Id(tree),Id(root)),Id(right)),NewExpr(Id(Node),[IntLit(3)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(tree),Id(root)),Id(left)),Id(left)),NewExpr(Id(Node),[IntLit(4)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(tree),Id(root)),Id(left)),Id(right)),NewExpr(Id(Node),[IntLit(5)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Preorder traversal of binary tree is )]),Call(Id(tree),Id(printPreorder),[]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Inorder traversal of binary tree is )]),Call(Id(tree),Id(printInorder),[]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Postorder traversal of binary tree is )]),Call(Id(tree),Id(printPostorder),[])]))])])"""
		self.assertTrue(TestAST.test(input,expect,342))
        
	def test43(self):
		input = """
        Class testReturnError {
            main(testparam: String) {
				System.out.println("Error");
				Return;
            }
		}
        """
		expect = """Program([ClassDecl(Id(testReturnError),[MethodDecl(Id(main),Instance,[param(Id(testparam),StringType)],Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Error)]),Return()]))])])"""
		self.assertTrue(TestAST.test(input,expect,343))
    
	def test44(self):
		input = """
        Class testArray {
            main(testparam: String) {
				Var arr: Array[Int, 3];
				arr[1] = 1;
				arr[2] = 2;
				arr[3] = 3;
				arr[0] = 0;
				Return;
            }
		}
        """
		expect = """Program([ClassDecl(Id(testArray),[MethodDecl(Id(main),Instance,[param(Id(testparam),StringType)],Block([VarDecl(Id(arr),ArrayType(3,IntType)),AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(arr),[IntLit(2)]),IntLit(2)),AssignStmt(ArrayCell(Id(arr),[IntLit(3)]),IntLit(3)),AssignStmt(ArrayCell(Id(arr),[IntLit(0)]),IntLit(0)),Return()]))])])"""
		self.assertTrue(TestAST.test(input,expect,344))
    
	def test45(self):
		input = """
        Class testErrorArgument {
            main(args : Array[Int,2]) {
				System.out.println(args[1] || args[2]);
            }
        }
        """
		expect = """Program([ClassDecl(Id(testErrorArgument),[MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,IntType))],Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(||,ArrayCell(Id(args),[IntLit(1)]),ArrayCell(Id(args),[IntLit(2)]))])]))])])"""
		self.assertTrue(TestAST.test(input,expect,345))
        
	def test46(self):
		input = """
        Class testErrorArgument {
            main(args : Array[Int,2]) {
				System.out.println(args[1] && args[2]);
            }
        }
        """
		expect = """Program([ClassDecl(Id(testErrorArgument),[MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,IntType))],Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(&&,ArrayCell(Id(args),[IntLit(1)]),ArrayCell(Id(args),[IntLit(2)]))])]))])])"""
		self.assertTrue(TestAST.test(input,expect,346))
    
	def test47(self):
		input = """
        Class TestReturn {
            $main() {
				Return;
				Return (4 + 3) * (2 - (16 % 3));
				Return New Spider_verse();
				Return New BinaryTree(root);
            }
		}
        """
		expect = """Program([ClassDecl(Id(TestReturn),[MethodDecl(Id($main),Static,[],Block([Return(),Return(BinaryOp(*,BinaryOp(+,IntLit(4),IntLit(3)),BinaryOp(-,IntLit(2),BinaryOp(%,IntLit(16),IntLit(3))))),Return(NewExpr(Id(Spider_verse),[])),Return(NewExpr(Id(BinaryTree),[Id(root)]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,347))
    
	def test48(self):
		input = """
        Class Spider_verse {
            ## instance fields ##
            Val num: Int = 15;
            Var name: String;
            Var suits: String;
            
            ## class fields ##
            Val $ratings: Float = 8.9;
            Constructor(name: String; suits: String) {
				Self.name = "Peter Parker";
				Self.suits = "Red";
			}
            Destructor(){
				
            }
		}
        """
		expect = """Program([ClassDecl(Id(Spider_verse),[AttributeDecl(Instance,ConstDecl(Id(num),IntType,IntLit(15))),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(suits),StringType)),AttributeDecl(Static,ConstDecl(Id($ratings),FloatType,FloatLit(8.9))),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(suits),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),StringLit(Peter Parker)),AssignStmt(FieldAccess(Self(),Id(suits)),StringLit(Red))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
		self.assertTrue(TestAST.test(input,expect,348))
        
	def test49(self):
		input = """
        Class Test{
            Var arr : Array[Int, 1];
            Var idx1: Int = arr[0+1];
        }
        """
		expect = """Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1,IntType))),AttributeDecl(Instance,VarDecl(Id(idx1),IntType,ArrayCell(Id(arr),[BinaryOp(+,IntLit(0),IntLit(1))])))])])"""
		self.assertTrue(TestAST.test(input,expect,349))
    
	def test50(self):
		input = """
        Class Test
		{
            Val arr: Array[Int, 5] = Array(12, 34, 54, 2, 3);
            recSearch(arr: Array[Int, 5]; l: Int; r: Int; x: Int)
            {
				If (r < l) {
					Return -1;
				}
				If (arr[l] == x) {
					Return l;
				}
				If (arr[r] == x) {
					Return r;
				}
				Return Self.recSearch(arr, l+1, r-1, x);
            }
            
            main(args: Array[String, 2])
            {
				Var x: Int = 3;
				
				Var index: Int = Self.recSearch(arr, 0, arr.length-1, x);
				If (index != -1) {
					System.out.println("Element " + x + " is present at index " + index);
				}
				Else {
					System.out.println("Element " + x + " is not present");
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(arr),ArrayType(5,IntType),[IntLit(12),IntLit(34),IntLit(54),IntLit(2),IntLit(3)])),MethodDecl(Id(recSearch),Instance,[param(Id(arr),ArrayType(5,IntType)),param(Id(l),IntType),param(Id(r),IntType),param(Id(x),IntType)],Block([If(BinaryOp(<,Id(r),Id(l)),Block([Return(UnaryOp(-,IntLit(1)))])),If(BinaryOp(==,ArrayCell(Id(arr),[Id(l)]),Id(x)),Block([Return(Id(l))])),If(BinaryOp(==,ArrayCell(Id(arr),[Id(r)]),Id(x)),Block([Return(Id(r))])),Return(CallExpr(Self(),Id(recSearch),[Id(arr),BinaryOp(+,Id(l),IntLit(1)),BinaryOp(-,Id(r),IntLit(1)),Id(x)]))])),MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,StringType))],Block([VarDecl(Id(x),IntType,IntLit(3)),VarDecl(Id(index),IntType,CallExpr(Self(),Id(recSearch),[Id(arr),IntLit(0),BinaryOp(-,FieldAccess(Id(arr),Id(length)),IntLit(1)),Id(x)])),If(BinaryOp(!=,Id(index),UnaryOp(-,IntLit(1))),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(Element ),Id(x)),StringLit( is present at index )),Id(index))])]),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,BinaryOp(+,StringLit(Element ),Id(x)),StringLit( is not present))])]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,350))
        
	def test51(self):
		input = """
        Class  Spider_man {
			Var Peter_3: Tom = (b::$c).a;
		}
        """
		expect = """Program([ClassDecl(Id(Spider_man),[AttributeDecl(Instance,VarDecl(Id(Peter_3),ClassType(Id(Tom)),FieldAccess(FieldAccess(Id(b),Id($c)),Id(a))))])])"""
		self.assertTrue(TestAST.test(input,expect,351))
        
	def test52(self):
		input = """
        Class Main
		{
            countOccurrences(arr: Array[Int, 100]; n: Int; x: Int)
            {
				Var res: Int = 0;
				Foreach (i In 0 .. n By 1) {
					If (x == arr[i]) {
						res = res + 1;
					}
				}
				Return res;
            }
            
            main(args: Array[String, 2])
            {
				Val arr: Array[Int, 10] = Array(1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8 );
				Var n: Int = arr.length();
				Var x: Int = 2;
				System.out.println(Self.countOccurrences(arr, n, x));
            }
		}
        """
		expect = """Program([ClassDecl(Id(Main),[MethodDecl(Id(countOccurrences),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(x),IntType)],Block([VarDecl(Id(res),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([If(BinaryOp(==,Id(x),ArrayCell(Id(arr),[Id(i)])),Block([AssignStmt(Id(res),BinaryOp(+,Id(res),IntLit(1)))]))])]),Return(Id(res))])),MethodDecl(Id(main),Instance,[param(Id(args),ArrayType(2,StringType))],Block([ConstDecl(Id(arr),ArrayType(10,IntType),[IntLit(1),IntLit(2),IntLit(2),IntLit(2),IntLit(2),IntLit(3),IntLit(4),IntLit(7),IntLit(8),IntLit(8)]),VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),VarDecl(Id(x),IntType,IntLit(2)),Call(FieldAccess(Id(System),Id(out)),Id(println),[CallExpr(Self(),Id(countOccurrences),[Id(arr),Id(n),Id(x)])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,352))
    
	def test53(self):
		input = """
        Class GFG {
            $getMin(arr: Array[Int, 100]; n: Int)
            {
				Var res: Int = arr[0];
				Foreach (i In 1 .. n By 1) {
					res = Math.min(res, arr[i]);
				}
				Return res;
            }
            $getMax(arr: Array[Int, 100]; n: Int)
            {
				Var res: Int = arr[0];
				Foreach (i In 1 .. n By 1) {
					res = Math.max(res, arr[i]);
				}
				Return res;
            }
            $main (args: Array[Int,2])
            {
				Var arr: Array[Int, 5] = Array(12, 1234, 45, 67, 1);
				Var n: Int = arr.length();
				System.out.println( "Minimum element" + " of array: " + GFG::$getMin(arr, n));
				System.out.println( "Maximum element" + " of array: " + GFG::$getMax(arr, n));
            }
		}
        """
		expect = """Program([ClassDecl(Id(GFG),[MethodDecl(Id($getMin),Static,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(res),IntType,ArrayCell(Id(arr),[IntLit(0)])),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([AssignStmt(Id(res),CallExpr(Id(Math),Id(min),[Id(res),ArrayCell(Id(arr),[Id(i)])]))])]),Return(Id(res))])),MethodDecl(Id($getMax),Static,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(res),IntType,ArrayCell(Id(arr),[IntLit(0)])),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([AssignStmt(Id(res),CallExpr(Id(Math),Id(max),[Id(res),ArrayCell(Id(arr),[Id(i)])]))])]),Return(Id(res))])),MethodDecl(Id($main),Static,[param(Id(args),ArrayType(2,IntType))],Block([VarDecl(Id(arr),ArrayType(5,IntType),[IntLit(12),IntLit(1234),IntLit(45),IntLit(67),IntLit(1)]),VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,BinaryOp(+,StringLit(Minimum element),StringLit( of array: )),CallExpr(Id(GFG),Id($getMin),[Id(arr),Id(n)]))]),Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,BinaryOp(+,StringLit(Maximum element),StringLit( of array: )),CallExpr(Id(GFG),Id($getMax),[Id(arr),Id(n)]))])]))])])"""
		self.assertTrue(TestAST.test(input,expect,353))
        
	def test54(self):
		input = """
        Class testAlgorithms {
            insertionSortRecursive(arr: Array[Int, 100]; n: Int)
            {
				## Base case ##
				If (n <= 1) {
					Return;
				}
            
				## Sort first n-1 elements ##
				Self.insertionSortRecursive(arr, n-1);
            
				## Insert last element at its correct position in sorted array. ##
				Var last: Int = arr[n-1];

				##
				Move elements of arr[0..i-1], that are
				greater than key, to one position ahead
				of their current position
				##
				Foreach (j In (n-2) .. 0 By -1) {
					If (arr[j] > last) {
						Break;
					}
					arr[j+1] = arr[j];
				}
				arr[j+1] = last;
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(insertionSortRecursive),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([If(BinaryOp(<=,Id(n),IntLit(1)),Block([Return()])),Call(Self(),Id(insertionSortRecursive),[Id(arr),BinaryOp(-,Id(n),IntLit(1))]),VarDecl(Id(last),IntType,ArrayCell(Id(arr),[BinaryOp(-,Id(n),IntLit(1))])),For(Id(j),BinaryOp(-,Id(n),IntLit(2)),IntLit(0),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(last)),Block([Break])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),ArrayCell(Id(arr),[Id(j)]))])]),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(last))]))])])"""
		self.assertTrue(TestAST.test(input,expect,354))
        
	def test55(self):
		input = """
        Class  Spider_man {
			Var Peter_2: Andrew = (c::$a).b;
		}
        """
		expect = """Program([ClassDecl(Id(Spider_man),[AttributeDecl(Instance,VarDecl(Id(Peter_2),ClassType(Id(Andrew)),FieldAccess(FieldAccess(Id(c),Id($a)),Id(b))))])])"""
		self.assertTrue(TestAST.test(input,expect,355))
    
	def test56(self):
		input = """
        ## Day la test so 56 !!!!! ##
		Class HeapSort {
            sort(arr: Array[Int, 100])
            {
				Var n: Int = arr.length();
				Foreach (i In (n / 2 - 1) .. 0 By -1) {
					Self.heapify(arr, n, i);
				}
				Foreach (i In (n - 1) .. 0 By -1) {
					Var temp: Int = arr[0];
					arr[0] = arr[i];
					arr[i] = temp;
					Self.heapify(arr, i, 0);
				}
            }
            heapify(arr: Array[Int, 100]; n: Int; i: Int)
            {
				Var largest: Int = i;
				Var l: Int = 2 * i + 1;
				Var r: Int = 2 * i + 2;
				If ((l < n) && (arr[l] > arr[largest])) {
					largest = l;
				}
				If ((r < n) && (arr[r] > arr[largest])) {
					largest = r;
				}
				If (largest != i) {
					Var swap: Int = arr[i];
					arr[i] = arr[largest];
					arr[largest] = swap;
					Self.heapify(arr, n, largest);
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(HeapSort),[MethodDecl(Id(sort),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),BinaryOp(-,BinaryOp(/,Id(n),IntLit(2)),IntLit(1)),IntLit(0),UnaryOp(-,IntLit(1)),Block([Call(Self(),Id(heapify),[Id(arr),Id(n),Id(i)])])]),For(Id(i),BinaryOp(-,Id(n),IntLit(1)),IntLit(0),UnaryOp(-,IntLit(1)),Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[IntLit(0)])),AssignStmt(ArrayCell(Id(arr),[IntLit(0)]),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),Id(temp)),Call(Self(),Id(heapify),[Id(arr),Id(i),IntLit(0)])])])])),MethodDecl(Id(heapify),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(i),IntType)],Block([VarDecl(Id(largest),IntType,Id(i)),VarDecl(Id(l),IntType,BinaryOp(+,BinaryOp(*,IntLit(2),Id(i)),IntLit(1))),VarDecl(Id(r),IntType,BinaryOp(+,BinaryOp(*,IntLit(2),Id(i)),IntLit(2))),If(BinaryOp(&&,BinaryOp(<,Id(l),Id(n)),BinaryOp(>,ArrayCell(Id(arr),[Id(l)]),ArrayCell(Id(arr),[Id(largest)]))),Block([AssignStmt(Id(largest),Id(l))])),If(BinaryOp(&&,BinaryOp(<,Id(r),Id(n)),BinaryOp(>,ArrayCell(Id(arr),[Id(r)]),ArrayCell(Id(arr),[Id(largest)]))),Block([AssignStmt(Id(largest),Id(r))])),If(BinaryOp(!=,Id(largest),Id(i)),Block([VarDecl(Id(swap),IntType,ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(largest)])),AssignStmt(ArrayCell(Id(arr),[Id(largest)]),Id(swap)),Call(Self(),Id(heapify),[Id(arr),Id(n),Id(largest)])]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,356))
    
	def test57(self):
		input = """
        Class Test{
            printArray(arr: Array[Int, 100])
            {
				Var n: Int = arr.length();
				Foreach (i In 0 .. (n-1) By 1) {
					System.out.print(arr[i] + " ");
				}
				System.out.println();
            }
		}
        """
		expect = """Program([ClassDecl(Id(Test),[MethodDecl(Id(printArray),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,ArrayCell(Id(arr),[Id(i)]),StringLit( ))])])]),Call(FieldAccess(Id(System),Id(out)),Id(println),[])]))])])"""
		self.assertTrue(TestAST.test(input,expect,357))
        
	def test58(self):
		input = """
        Class TestAlgorithms {
            isPrime(n: Int)
            {
				If (n <= 1) {
					Return False;
				}
				Foreach (i In 2 .. n By 1) {
					If (n % i == 0) {
						Return False;
					}
				}
				Return True;
            }
		}
        """
		expect = """Program([ClassDecl(Id(TestAlgorithms),[MethodDecl(Id(isPrime),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(<=,Id(n),IntLit(1)),Block([Return(BooleanLit(False))])),For(Id(i),IntLit(2),Id(n),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLit(0)),Block([Return(BooleanLit(False))]))])]),Return(BooleanLit(True))]))])])"""
		self.assertTrue(TestAST.test(input,expect,358))
    
	def test59(self):
		input = """
        Class testAlgorithms {
            bubbleSort(arr: Array[Int, 100])
            {
				Var n: Int = arr.length();
				Foreach (i In 0 .. (n-1) By 1) {
					Foreach (j In 0 .. (n-i-1) By 1) {
						If (arr[j] > arr[j+1])
						{
							Var temp: Int = arr[j];
							arr[j] = arr[j+1];
							arr[j+1] = temp;
						}
					}
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(bubbleSort),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,Id(n),Id(i)),IntLit(1)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])),Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(temp))]))])])])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,359))
        
	def test60(self):
		input = """
        Class Program {
            main(){
				Var x: Int = Spidey.swing();
				Return x;
            }
		}
		Class Test {
            testloop(a: Int; b: Float) {
				Foreach (i In 0 .. 15) {
					s = s + a[i];
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,CallExpr(Id(Spidey),Id(swing),[])),Return(Id(x))]))]),ClassDecl(Id(Test),[MethodDecl(Id(testloop),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(0),IntLit(15),IntLit(1),Block([AssignStmt(Id(s),BinaryOp(+,Id(s),ArrayCell(Id(a),[Id(i)])))])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,360))
        
	def test61(self):
		input = """
		Class Test{
			Val _: Float = 5.897;
			Var __: Array[Array[String, 3], 7];
			Var ___: Array[Array[Array[Int, 12], 7], 8];
		}
		"""
		expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(_),FloatType,FloatLit(5.897))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(7,ArrayType(3,StringType)))),AttributeDecl(Instance,VarDecl(Id(___),ArrayType(8,ArrayType(7,ArrayType(12,IntType)))))])])"
		self.assertTrue(TestAST.test(input, expect, 361))
    
	def test62(self):
		input = """
		Class Operator
		{
			main()
			{
				a[(3+x.foo(2))/5*3-25] = a[b[2]] +3*a[4]/3;
			}
		}
        """
		expect = """Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[BinaryOp(-,BinaryOp(*,BinaryOp(/,BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)])),IntLit(5)),IntLit(3)),IntLit(25))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(2)])]),BinaryOp(/,BinaryOp(*,IntLit(3),ArrayCell(Id(a),[IntLit(4)])),IntLit(3))))]))])])"""
		self.assertTrue(TestAST.test(input,expect,362))
        
	def test63(self):
		input = """
        Class ElectricGadgets {
            Var batteryUsing: Boolean;
			Var gravity: Float;
			
			Constructor() {
				
			}
			Constructor(batteryUsing:Boolean; gravity: Float) {
				Self.batteryUsing = batteryUsing;
				Self.gravity = gravity / 9.8;
			}
		}
		Class ElectricCar : ElectricGadgets {
			__init__() {
				ElectricCar::$noUse();
				Return batteryUsing;
			}
		}
        """
		expect = "Program([ClassDecl(Id(ElectricGadgets),[AttributeDecl(Instance,VarDecl(Id(batteryUsing),BoolType)),AttributeDecl(Instance,VarDecl(Id(gravity),FloatType)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(batteryUsing),BoolType),param(Id(gravity),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(batteryUsing)),Id(batteryUsing)),AssignStmt(FieldAccess(Self(),Id(gravity)),BinaryOp(/,Id(gravity),FloatLit(9.8)))]))]),ClassDecl(Id(ElectricCar),Id(ElectricGadgets),[MethodDecl(Id(__init__),Instance,[],Block([Call(Id(ElectricCar),Id($noUse),[]),Return(Id(batteryUsing))]))])])"
		self.assertTrue(TestAST.test(input, expect, 363))
        
	def test64(self):
		input = """
        Class Program {
            checkCompletedNumber(num: Int) {
                Var dividedSum: Int = 0;
                Foreach (i In 1 .. n-1 By 1) {
                    If ((n % i) == 0) {
						dividedSum = dividedSum + i;
					}
                }
                Return (dividedSum == num);
            }

            main() {
                Var num: Int;
                num = Scan.in();
                System.out.println(Self.checkCompletedNumber(num));
            }
        }"""
		expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(checkCompletedNumber),Instance,[param(Id(num),IntType)],Block([VarDecl(Id(dividedSum),IntType,IntLit(0)),For(Id(i),IntLit(1),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLit(0)),Block([AssignStmt(Id(dividedSum),BinaryOp(+,Id(dividedSum),Id(i)))]))])]),Return(BinaryOp(==,Id(dividedSum),Id(num)))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(num),IntType),AssignStmt(Id(num),CallExpr(Id(Scan),Id(in),[])),Call(FieldAccess(Id(System),Id(out)),Id(println),[CallExpr(Self(),Id(checkCompletedNumber),[Id(num)])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,364))
    
	def test65(self):
		input = """
		Class Test: QA {
			Var check: Main = New Main(Program);
		}
		"""
		expect = """Program([ClassDecl(Id(Test),Id(QA),[AttributeDecl(Instance,VarDecl(Id(check),ClassType(Id(Main)),NewExpr(Id(Main),[Id(Program)])))])])"""
		self.assertTrue(TestAST.test(input,expect,365))

	def test66(self):
		input = """
		Class Test {
			Val sub: Int = Self.b.mul[12];
			Val add: String = s.subStr(ta, tv, tm)[11][25][15];
		}
		"""
		expect = """Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(sub),IntType,ArrayCell(FieldAccess(FieldAccess(Self(),Id(b)),Id(mul)),[IntLit(12)]))),AttributeDecl(Instance,ConstDecl(Id(add),StringType,ArrayCell(CallExpr(Id(s),Id(subStr),[Id(ta),Id(tv),Id(tm)]),[IntLit(11),IntLit(25),IntLit(15)])))])])"""
		self.assertTrue(TestAST.test(input,expect,366))
        
	def test67(self):
		input = """
            Class Program {
                main() {
                    newObject = New Expression((52 - 2.5 * v / 8) <= 9 && x || (x + y));
                    exprArray[1] = New Expr((52 - 2.5 * v / 8) <= 9 && x || (x + y));
                    Return Self.castStringToExpression(exprArr[23][10]);
                }
                checkNullExpr(expr :String) {
                    expr = Self.castStringToExpression(expr);
                    If (expr != Null) {
                        Return True;
                    }
                    Return False;
                }
                castStringToExpression(expression: String) {
                    Return New Expression(expression.getValue());
                }
            }
            """
		expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(newObject),NewExpr(Id(Expression),[BinaryOp(<=,BinaryOp(-,IntLit(52),BinaryOp(/,BinaryOp(*,FloatLit(2.5),Id(v)),IntLit(8))),BinaryOp(||,BinaryOp(&&,IntLit(9),Id(x)),BinaryOp(+,Id(x),Id(y))))])),AssignStmt(ArrayCell(Id(exprArray),[IntLit(1)]),NewExpr(Id(Expr),[BinaryOp(<=,BinaryOp(-,IntLit(52),BinaryOp(/,BinaryOp(*,FloatLit(2.5),Id(v)),IntLit(8))),BinaryOp(||,BinaryOp(&&,IntLit(9),Id(x)),BinaryOp(+,Id(x),Id(y))))])),Return(CallExpr(Self(),Id(castStringToExpression),[ArrayCell(Id(exprArr),[IntLit(23),IntLit(10)])]))])),MethodDecl(Id(checkNullExpr),Instance,[param(Id(expr),StringType)],Block([AssignStmt(Id(expr),CallExpr(Self(),Id(castStringToExpression),[Id(expr)])),If(BinaryOp(!=,Id(expr),NullLiteral()),Block([Return(BooleanLit(True))])),Return(BooleanLit(False))])),MethodDecl(Id(castStringToExpression),Instance,[param(Id(expression),StringType)],Block([Return(NewExpr(Id(Expression),[CallExpr(Id(expression),Id(getValue),[])]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,367))
    
	def test68(self):
		input = """
        Class ConvertNumber {
            $reverseNumber(num, digitCount:Int) {
                Var result: Int = 0;
                result = result * 10 + num % 10;
                num = 10;
                digitCount = - 1;
                Return result;
            }
            $convertNumberToBaseN(num, base_n :Int) {
                Var result: Int = 0;
                Var digitCount: Int = 0;
                result = result * 10 + (num % base_n);
                num = base_n;
                digitCount = -12;
                Return Self.reverseNumber(result, digitCount);
            }
        }
        Class Program {
            main() {
                Var number: Int;
                number = Scan.input();
                ConvertNumber::$convertNumberToBaseN(number, 2);
                ConvertNumber::$convertNumberToBaseN(number, 16);
            }
        }
        """
		expect = """Program([ClassDecl(Id(ConvertNumber),[MethodDecl(Id($reverseNumber),Static,[param(Id(num),IntType),param(Id(digitCount),IntType)],Block([VarDecl(Id(result),IntType,IntLit(0)),AssignStmt(Id(result),BinaryOp(+,BinaryOp(*,Id(result),IntLit(10)),BinaryOp(%,Id(num),IntLit(10)))),AssignStmt(Id(num),IntLit(10)),AssignStmt(Id(digitCount),UnaryOp(-,IntLit(1))),Return(Id(result))])),MethodDecl(Id($convertNumberToBaseN),Static,[param(Id(num),IntType),param(Id(base_n),IntType)],Block([VarDecl(Id(result),IntType,IntLit(0)),VarDecl(Id(digitCount),IntType,IntLit(0)),AssignStmt(Id(result),BinaryOp(+,BinaryOp(*,Id(result),IntLit(10)),BinaryOp(%,Id(num),Id(base_n)))),AssignStmt(Id(num),Id(base_n)),AssignStmt(Id(digitCount),UnaryOp(-,IntLit(12))),Return(CallExpr(Self(),Id(reverseNumber),[Id(result),Id(digitCount)]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(number),IntType),AssignStmt(Id(number),CallExpr(Id(Scan),Id(input),[])),Call(Id(ConvertNumber),Id($convertNumberToBaseN),[Id(number),IntLit(2)]),Call(Id(ConvertNumber),Id($convertNumberToBaseN),[Id(number),IntLit(16)])]))])])"""
		self.assertTrue(TestAST.test(input,expect,368))
        
	def test69(self):
		input = """
        Class Search {
            $recursiveSearch(n, m: Int; arr: Array[Int,4]; idx: Int)
            {
                If ((n == 0) || (idx >= n)) 
                {
                    Return -1;
                }
                If (arr[idx] == m)
                {
                    Foreach (i In idx .. n)
                    {
                        arr[i]= arr[i+1];
                    }
                    n = n-1;
                    Return idx;
                }
                Return Search::$recursiveSearch(n, m, arr, idx + 1);
            }
        }
        """
		expect = """Program([ClassDecl(Id(Search),[MethodDecl(Id($recursiveSearch),Static,[param(Id(n),IntType),param(Id(m),IntType),param(Id(arr),ArrayType(4,IntType)),param(Id(idx),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(n),IntLit(0)),BinaryOp(>=,Id(idx),Id(n))),Block([Return(UnaryOp(-,IntLit(1)))])),If(BinaryOp(==,ArrayCell(Id(arr),[Id(idx)]),Id(m)),Block([For(Id(i),Id(idx),Id(n),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))]))])]),AssignStmt(Id(n),BinaryOp(-,Id(n),IntLit(1))),Return(Id(idx))])),Return(CallExpr(Id(Search),Id($recursiveSearch),[Id(n),Id(m),Id(arr),BinaryOp(+,Id(idx),IntLit(1))]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,369))
        
	def test70(self):
		input = """
		Class ListFlattening {
			flatten (lst: Array[Int, 04]) {
				If (lst == Array()) {
					Return lst;
				}
				If (list.isinstance(lst[0], list)) {
					Return Self.flatten(lst[0]) + Self.flatten(list.from(1).to().of(lst));
				}
				Return list.from().to(1).of(lst) + Self.flatten(list.from(1).to().of(lst));
			}
		}
		Class Program {
			main() {
				Var s: Array[Int, 15] = Array(Array(2,5), Array(3,7), Array(4,9));
				os.print("Flattened list is: ", Flatten.flatten(s));
			}
		}
		"""
		expect = """Program([ClassDecl(Id(ListFlattening),[MethodDecl(Id(flatten),Instance,[param(Id(lst),ArrayType(4,IntType))],Block([If(BinaryOp(==,Id(lst),[]),Block([Return(Id(lst))])),If(CallExpr(Id(list),Id(isinstance),[ArrayCell(Id(lst),[IntLit(0)]),Id(list)]),Block([Return(BinaryOp(+,CallExpr(Self(),Id(flatten),[ArrayCell(Id(lst),[IntLit(0)])]),CallExpr(Self(),Id(flatten),[CallExpr(CallExpr(CallExpr(Id(list),Id(from),[IntLit(1)]),Id(to),[]),Id(of),[Id(lst)])])))])),Return(BinaryOp(+,CallExpr(CallExpr(CallExpr(Id(list),Id(from),[]),Id(to),[IntLit(1)]),Id(of),[Id(lst)]),CallExpr(Self(),Id(flatten),[CallExpr(CallExpr(CallExpr(Id(list),Id(from),[IntLit(1)]),Id(to),[]),Id(of),[Id(lst)])])))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(s),ArrayType(15,IntType),[[IntLit(2),IntLit(5)],[IntLit(3),IntLit(7)],[IntLit(4),IntLit(9)]]),Call(Id(os),Id(print),[StringLit(Flattened list is: ),CallExpr(Id(Flatten),Id(flatten),[Id(s)])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,370))
    
	def test71(self):
		input = """
        Class Character {
            mostFrequentCharacter(str, result: String; frequency: Int) {
                Var count: Array[Int, 500] = New List(integer, 500);
                current = ptr.addr(str);
                If (("A" <= current) && (current <= "Z")) {
                    current = current - "A" +. "a";
                }
                Math.increase1(count[current]);
                Math.increase1(str);
                frequency = 0;
                Foreach (ch In "a" .. "z") {
                    If (count[ch] > frequency) {
                        result = ch;
                        frequency = count[ch];
                    }
                }
            }
        }
        """
		expect = """Program([ClassDecl(Id(Character),[MethodDecl(Id(mostFrequentCharacter),Instance,[param(Id(str),StringType),param(Id(result),StringType),param(Id(frequency),IntType)],Block([VarDecl(Id(count),ArrayType(500,IntType),NewExpr(Id(List),[Id(integer),IntLit(500)])),AssignStmt(Id(current),CallExpr(Id(ptr),Id(addr),[Id(str)])),If(BinaryOp(&&,BinaryOp(<=,StringLit(A),Id(current)),BinaryOp(<=,Id(current),StringLit(Z))),Block([AssignStmt(Id(current),BinaryOp(+.,BinaryOp(-,Id(current),StringLit(A)),StringLit(a)))])),Call(Id(Math),Id(increase1),[ArrayCell(Id(count),[Id(current)])]),Call(Id(Math),Id(increase1),[Id(str)]),AssignStmt(Id(frequency),IntLit(0)),For(Id(ch),StringLit(a),StringLit(z),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(count),[Id(ch)]),Id(frequency)),Block([AssignStmt(Id(result),Id(ch)),AssignStmt(Id(frequency),ArrayCell(Id(count),[Id(ch)]))]))])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,371))
    
	def test72(self):
		input = """
        Class SortAlgorithms {
			selectionSort(arr: Array[Int, 100])
            {
				Var n: Int = arr.length();
			
				## One by one move boundary of unsorted subarray ##
				Foreach (i In 1 .. (n-1) By 1)
				{
					## Find the minimum element in unsorted array ##
					Var min_idx: Int = i;
					Foreach (j In (i+1) .. n By 1) {
						If (arr[j] < arr[min_idx]) {
							min_idx = j;
						}
					}
					## Swap the found minimum element with the first element ##
					Var temp: Int = arr[min_idx];
					arr[min_idx] = arr[i];
					arr[i] = temp;
				}
            }
            
            bubbleSort(arr: Array[Int, 100])
            {
				Var n: Int = arr.length();
				Foreach (i In 0 .. (n-1) By 1) {
					Foreach (j In 0 .. (n-i-1) By 1) {
						If (arr[j] > arr[j+1])
						{
							Var temp: Int = arr[j];
							arr[j] = arr[j+1];
							arr[j+1] = temp;
						}
					}
				}
            }
            
            insertionSortRecursive(arr: Array[Int, 100]; n: Int)
            {
				## Base case ##
				If (n <= 1) {
					Return;
				}
            
				## Sort first n-1 elements ##
				Self.insertionSortRecursive(arr, n-1);
            
				## Insert last element at its correct position in sorted array. ##
				Var last: Int = arr[n-1];

				##
				Move elements of arr[0..i-1], that are
				greater than key, to one position ahead
				of their current position
				##
				Foreach (j In (n-2) .. 0 By -1) {
					If (arr[j] > last) {
						Break;
					}
					arr[j+1] = arr[j];
				}
				arr[j+1] = last;
            }
            
            insertionSort(arr: Array[Int, 100]; left: Int; right: Int)
            {
				Foreach (i In (left + 1) .. right By 1)
				{
					Var temp: Int = arr[i];
					Var j: Int = i - 1;
					Foreach (j In (i - 1) .. left By -1) {
						If (arr[j] > temp) {
							Break;
						}
						arr[j+1] = arr[j];
						j = j + 1;
					}
					arr[j+1] = temp;
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(SortAlgorithms),[MethodDecl(Id(selectionSort),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),IntLit(1),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([VarDecl(Id(min_idx),IntType,Id(i)),For(Id(j),BinaryOp(+,Id(i),IntLit(1)),Id(n),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[Id(min_idx)])),Block([AssignStmt(Id(min_idx),Id(j))]))])]),VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(min_idx)])),AssignStmt(ArrayCell(Id(arr),[Id(min_idx)]),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),Id(temp))])])])),MethodDecl(Id(bubbleSort),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,Id(n),Id(i)),IntLit(1)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])),Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(temp))]))])])])])])),MethodDecl(Id(insertionSortRecursive),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([If(BinaryOp(<=,Id(n),IntLit(1)),Block([Return()])),Call(Self(),Id(insertionSortRecursive),[Id(arr),BinaryOp(-,Id(n),IntLit(1))]),VarDecl(Id(last),IntType,ArrayCell(Id(arr),[BinaryOp(-,Id(n),IntLit(1))])),For(Id(j),BinaryOp(-,Id(n),IntLit(2)),IntLit(0),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(last)),Block([Break])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),ArrayCell(Id(arr),[Id(j)]))])]),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(last))])),MethodDecl(Id(insertionSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(left),IntType),param(Id(right),IntType)],Block([For(Id(i),BinaryOp(+,Id(left),IntLit(1)),Id(right),IntLit(1),Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(i)])),VarDecl(Id(j),IntType,BinaryOp(-,Id(i),IntLit(1))),For(Id(j),BinaryOp(-,Id(i),IntLit(1)),Id(left),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(temp)),Block([Break])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))])]),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(temp))])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,372))
        
	def test73(self):
		input = """
        Class SortAlgorithms {
			merge(array: Array[Int, 100]; left: Int; mid: Int; right: Int)
            {
				Val subArrayOne: Int = mid - left + 1;
				Val subArrayTwo: Int = right - mid;
				
				## Create temp arrays ##
				Var leftArray, rightArray: Array[Int, 50];
				
				## Copy data to temp arrays leftArray[] and rightArray[] ##
				Foreach (i In 0 .. subArrayOne By 1) {
					leftArray[i] = array[left + i];
				}
				Foreach (j In 0 .. subArrayTwo By 1) {
					rightArray[j] = array[mid + 1 + j];
				}
				
				Var indexOfSubArrayOne, indexOfSubArrayTwo, indexOfMergedArray: Int = 0, 0, left;
				
				## Merge the temp arrays back into array[left..right] ##
				Foreach (i In 0 .. ((indexOfSubArrayOne < subArrayOne) && (indexOfSubArrayTwo < subArrayTwo)) By 1) {
					If (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
						array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
						indexOfSubArrayOne = indexOfSubArrayOne + 1;
					}
					Else {
						array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
						indexOfSubArrayTwo = indexOfSubArrayTwo + 1;
					}
					indexOfMergedArray = indexOfMergedArray + 1;
				}
				## Copy the remaining elements of left[], if there are any ##
				Foreach (i In indexOfSubArrayOne .. (indexOfSubArrayOne < subArrayOne) By 1)
				{
					array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
					indexOfSubArrayOne = indexOfSubArrayOne + 1;
					indexOfMergedArray = indexOfMergedArray + 1;
				}
				## Copy the remaining elements of right[], if there are any ##
				Foreach (i In indexOfSubArrayTwo .. (indexOfSubArrayTwo < subArrayTwo) By 1) {
					array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
					indexOfSubArrayTwo = indexOfSubArrayTwo + 1;
					indexOfMergedArray = indexOfMergedArray + 1;
				}
            }
            
            ## begin is for left index and end is right index of the sub-array of arr to be sorted ##
            mergeSort(array: Array[Int, 100]; begin: Int; end: Int)
            {
				If (begin >= end) {
					Return; 
				}
				Var mid: Int = begin + (end - begin) / 2;
				Self.mergeSort(array, begin, mid);
				Self.mergeSort(array, mid + 1, end);
				Self.merge(array, begin, mid, end);
            }
            
            swap(arr: Array[Int, 100]; i: Int; j: Int)
            {
				Var temp: Int = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
			
			## This function takes last element as pivot, places
			the pivot element at its correct position in sorted
			array, and places all smaller (smaller than pivot)
			to left of pivot and all greater elements to right
			of pivot ##
			partition(arr: Array[Int, 100]; low: Int; high: Int)
			{
				Var pivot: Int = arr[high];
				
				## Index of smaller element and indicates the right position of pivot found so far ##
				Var i: Int = (low - 1);
				Foreach (j In low .. (high - 1) By 1)
				{
					If (arr[j] < pivot)
					{
						i = i + 1;
						Self.swap(arr, i, j);
					}
				}
				Self.swap(arr, i + 1, high);
				Return (i + 1);
			}
				
			## The main function that implements QuickSort
				arr[] --> Array to be sorted,
				low --> Starting index,
				high --> Ending index
			##
			quickSort(arr: Array[Int, 100]; low: Int; high: Int)
			{
				If (low < high)
				{
					Var pi: Int = Self.partition(arr, low, high);
					Self.quickSort(arr, low, pi - 1);
					Self.quickSort(arr, pi + 1, high);
				}
            }
            
            insertionSort(arr: Array[Int, 100]; left: Int; right: Int)
            {
				Foreach (i In (left + 1) .. right By 1)
				{
					Var temp: Int = arr[i];
					Var j: Int = i - 1;
					Foreach (j In (i - 1) .. left By -1) {
						If (arr[j] > temp) {
							Break;
						}
						arr[j+1] = arr[j];
						j = j + 1;
					}
					arr[j+1] = temp;
				}
            }
            
            timSort(arr: Array[Int, 100]; n: Int)
            {
				Foreach (i In 0 .. n By testAlgorithms::$RUN) {
					Self.insertionSort(arr, i, Algorithms.min((i + testAlgorithms::$RUN - 1), (n - 1)));
				}
				Foreach (size In RUN .. n)
				{
					Foreach (left In 0 .. n By (2*size))
					{
						Var mid: Int = left + size - 1;
						Var right: Int = Algorithms.min((left + 2*size - 1), (n-1));
						If (mid < right) {
                        Self.merge(arr, left, mid, right);
						}
					}
                  	size = size * 2;
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(SortAlgorithms),[MethodDecl(Id(merge),Instance,[param(Id(array),ArrayType(100,IntType)),param(Id(left),IntType),param(Id(mid),IntType),param(Id(right),IntType)],Block([ConstDecl(Id(subArrayOne),IntType,BinaryOp(+,BinaryOp(-,Id(mid),Id(left)),IntLit(1))),ConstDecl(Id(subArrayTwo),IntType,BinaryOp(-,Id(right),Id(mid))),VarDecl(Id(leftArray),ArrayType(50,IntType)),VarDecl(Id(rightArray),ArrayType(50,IntType)),For(Id(i),IntLit(0),Id(subArrayOne),IntLit(1),Block([AssignStmt(ArrayCell(Id(leftArray),[Id(i)]),ArrayCell(Id(array),[BinaryOp(+,Id(left),Id(i))]))])]),For(Id(j),IntLit(0),Id(subArrayTwo),IntLit(1),Block([AssignStmt(ArrayCell(Id(rightArray),[Id(j)]),ArrayCell(Id(array),[BinaryOp(+,BinaryOp(+,Id(mid),IntLit(1)),Id(j))]))])]),VarDecl(Id(indexOfSubArrayOne),IntType,IntLit(0)),VarDecl(Id(indexOfSubArrayTwo),IntType,IntLit(0)),VarDecl(Id(indexOfMergedArray),IntType,Id(left)),For(Id(i),IntLit(0),BinaryOp(&&,BinaryOp(<,Id(indexOfSubArrayOne),Id(subArrayOne)),BinaryOp(<,Id(indexOfSubArrayTwo),Id(subArrayTwo))),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)])),AssignStmt(Id(indexOfSubArrayOne),BinaryOp(+,Id(indexOfSubArrayOne),IntLit(1)))]),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),AssignStmt(Id(indexOfSubArrayTwo),BinaryOp(+,Id(indexOfSubArrayTwo),IntLit(1)))])),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])]),For(Id(i),Id(indexOfSubArrayOne),BinaryOp(<,Id(indexOfSubArrayOne),Id(subArrayOne)),IntLit(1),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(leftArray),[Id(indexOfSubArrayOne)])),AssignStmt(Id(indexOfSubArrayOne),BinaryOp(+,Id(indexOfSubArrayOne),IntLit(1))),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])]),For(Id(i),Id(indexOfSubArrayTwo),BinaryOp(<,Id(indexOfSubArrayTwo),Id(subArrayTwo)),IntLit(1),Block([AssignStmt(ArrayCell(Id(array),[Id(indexOfMergedArray)]),ArrayCell(Id(rightArray),[Id(indexOfSubArrayTwo)])),AssignStmt(Id(indexOfSubArrayTwo),BinaryOp(+,Id(indexOfSubArrayTwo),IntLit(1))),AssignStmt(Id(indexOfMergedArray),BinaryOp(+,Id(indexOfMergedArray),IntLit(1)))])])])),MethodDecl(Id(mergeSort),Instance,[param(Id(array),ArrayType(100,IntType)),param(Id(begin),IntType),param(Id(end),IntType)],Block([If(BinaryOp(>=,Id(begin),Id(end)),Block([Return()])),VarDecl(Id(mid),IntType,BinaryOp(+,Id(begin),BinaryOp(/,BinaryOp(-,Id(end),Id(begin)),IntLit(2)))),Call(Self(),Id(mergeSort),[Id(array),Id(begin),Id(mid)]),Call(Self(),Id(mergeSort),[Id(array),BinaryOp(+,Id(mid),IntLit(1)),Id(end)]),Call(Self(),Id(merge),[Id(array),Id(begin),Id(mid),Id(end)])])),MethodDecl(Id(swap),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(i),IntType),param(Id(j),IntType)],Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))])),MethodDecl(Id(partition),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),For(Id(j),Id(low),BinaryOp(-,Id(high),IntLit(1)),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Call(Self(),Id(swap),[Id(arr),Id(i),Id(j)])]))])]),Call(Self(),Id(swap),[Id(arr),BinaryOp(+,Id(i),IntLit(1)),Id(high)]),Return(BinaryOp(+,Id(i),IntLit(1)))])),MethodDecl(Id(quickSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(<,Id(low),Id(high)),Block([VarDecl(Id(pi),IntType,CallExpr(Self(),Id(partition),[Id(arr),Id(low),Id(high)])),Call(Self(),Id(quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Self(),Id(quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])]))])),MethodDecl(Id(insertionSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(left),IntType),param(Id(right),IntType)],Block([For(Id(i),BinaryOp(+,Id(left),IntLit(1)),Id(right),IntLit(1),Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(i)])),VarDecl(Id(j),IntType,BinaryOp(-,Id(i),IntLit(1))),For(Id(j),BinaryOp(-,Id(i),IntLit(1)),Id(left),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(temp)),Block([Break])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))])]),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(temp))])])])),MethodDecl(Id(timSort),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType)],Block([For(Id(i),IntLit(0),Id(n),FieldAccess(Id(testAlgorithms),Id($RUN)),Block([Call(Self(),Id(insertionSort),[Id(arr),Id(i),CallExpr(Id(Algorithms),Id(min),[BinaryOp(-,BinaryOp(+,Id(i),FieldAccess(Id(testAlgorithms),Id($RUN))),IntLit(1)),BinaryOp(-,Id(n),IntLit(1))])])])]),For(Id(size),Id(RUN),Id(n),IntLit(1),Block([For(Id(left),IntLit(0),Id(n),BinaryOp(*,IntLit(2),Id(size)),Block([VarDecl(Id(mid),IntType,BinaryOp(-,BinaryOp(+,Id(left),Id(size)),IntLit(1))),VarDecl(Id(right),IntType,CallExpr(Id(Algorithms),Id(min),[BinaryOp(-,BinaryOp(+,Id(left),BinaryOp(*,IntLit(2),Id(size))),IntLit(1)),BinaryOp(-,Id(n),IntLit(1))])),If(BinaryOp(<,Id(mid),Id(right)),Block([Call(Self(),Id(merge),[Id(arr),Id(left),Id(mid),Id(right)])]))])]),AssignStmt(Id(size),BinaryOp(*,Id(size),IntLit(2)))])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,373))
    
	def test74(self):
		input = """
        Class searchAlgorithms {
			search(arr: Array[Int, 100]; n: Int; x: Int)
            {
				Var i: Int;
				Foreach (i In 0 .. n By 1) {
					If (arr[i] == x) {
						Return i;
					}
				}
				Return -1;
            }
            binarySearch(arr: Array[Int, 10]; l: Int; r: Int; x: Int) 
            { 
				If (r >= l) { 
					Var mid: Int = l + (r - l) / 2;  
					If (arr[mid] == x) {
						Return mid;
					}
					If (arr[mid] > x) {
						Return Self.binarySearch(arr, l, mid - 1, x);
					}
					Return Self.binarySearch(arr, mid + 1, r, x); 
				} 
				Return -1; 
            }
            recSearch(arr: Array[Int, 5]; l: Int; r: Int; x: Int)
            {
				If (r < l) {
					Return -1;
				}
				If (arr[l] == x) {
					Return l;
				}
				If (arr[r] == x) {
					Return r;
				}
				Return Self.recSearch(arr, l+1, r-1, x);
            }
		}
        """
		expect = """Program([ClassDecl(Id(searchAlgorithms),[MethodDecl(Id(search),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(x),IntType)],Block([VarDecl(Id(i),IntType),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([If(BinaryOp(==,ArrayCell(Id(arr),[Id(i)]),Id(x)),Block([Return(Id(i))]))])]),Return(UnaryOp(-,IntLit(1)))])),MethodDecl(Id(binarySearch),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(l),IntType),param(Id(r),IntType),param(Id(x),IntType)],Block([If(BinaryOp(>=,Id(r),Id(l)),Block([VarDecl(Id(mid),IntType,BinaryOp(+,Id(l),BinaryOp(/,BinaryOp(-,Id(r),Id(l)),IntLit(2)))),If(BinaryOp(==,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(Id(mid))])),If(BinaryOp(>,ArrayCell(Id(arr),[Id(mid)]),Id(x)),Block([Return(CallExpr(Self(),Id(binarySearch),[Id(arr),Id(l),BinaryOp(-,Id(mid),IntLit(1)),Id(x)]))])),Return(CallExpr(Self(),Id(binarySearch),[Id(arr),BinaryOp(+,Id(mid),IntLit(1)),Id(r),Id(x)]))])),Return(UnaryOp(-,IntLit(1)))])),MethodDecl(Id(recSearch),Instance,[param(Id(arr),ArrayType(5,IntType)),param(Id(l),IntType),param(Id(r),IntType),param(Id(x),IntType)],Block([If(BinaryOp(<,Id(r),Id(l)),Block([Return(UnaryOp(-,IntLit(1)))])),If(BinaryOp(==,ArrayCell(Id(arr),[Id(l)]),Id(x)),Block([Return(Id(l))])),If(BinaryOp(==,ArrayCell(Id(arr),[Id(r)]),Id(x)),Block([Return(Id(r))])),Return(CallExpr(Self(),Id(recSearch),[Id(arr),BinaryOp(+,Id(l),IntLit(1)),BinaryOp(-,Id(r),IntLit(1)),Id(x)]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,374))
    
	def test75(self):
		input = """
        Class RecursiveAlgorithms {
			recSearch(arr: Array[Int, 5]; l: Int; r: Int; x: Int)
            {
				If (r < l) {
					Return -1;
				}
				If (arr[l] == x) {
					Return l;
				}
				If (arr[r] == x) {
					Return r;
				}
				Return Self.recSearch(arr, l+1, r-1, x);
            }
            
            isPalRec(str: Array[String, 100]; s: Int; e: Int)
            {
				If (s == e) {
					Return True;
				}
				If (str[s] != str[e]) {
					Return False;
				}
				If (s < e + 1) {
					Return Self.isPalRec(str, s + 1, e - 1);
				}
				Return True;
            }
            
            isPalindrome(str: Array[String, 100])
            {
				Val n: Int = Str.strlen(str);
				If (n == 0) {
					Return True;
				}
				Return Self.isPalRec(str, 0, n - 1);
            }
            
            SumRecursion(n: Int) {
				##
					sum = 1 + ... + n
				##
				If (n == 0) {
					Return 0;
				}
				Return n + Self.SumRecursion(n - 1);
            }
            
            Fibonacci(n: Int)
            {
				If ((n == 1) || (n == 2)) {
					Return 1;
				}
				Return Self.Fibonacci(n - 1) + Self.Fibonacci(n - 2);
            }
            
            factorial(n: Int)
            {
				If (n == 0) {
					Return 1;
				}
                Return n * Self.factorial(n - 1);
            }
		}
        """
		expect = """Program([ClassDecl(Id(RecursiveAlgorithms),[MethodDecl(Id(recSearch),Instance,[param(Id(arr),ArrayType(5,IntType)),param(Id(l),IntType),param(Id(r),IntType),param(Id(x),IntType)],Block([If(BinaryOp(<,Id(r),Id(l)),Block([Return(UnaryOp(-,IntLit(1)))])),If(BinaryOp(==,ArrayCell(Id(arr),[Id(l)]),Id(x)),Block([Return(Id(l))])),If(BinaryOp(==,ArrayCell(Id(arr),[Id(r)]),Id(x)),Block([Return(Id(r))])),Return(CallExpr(Self(),Id(recSearch),[Id(arr),BinaryOp(+,Id(l),IntLit(1)),BinaryOp(-,Id(r),IntLit(1)),Id(x)]))])),MethodDecl(Id(isPalRec),Instance,[param(Id(str),ArrayType(100,StringType)),param(Id(s),IntType),param(Id(e),IntType)],Block([If(BinaryOp(==,Id(s),Id(e)),Block([Return(BooleanLit(True))])),If(BinaryOp(!=,ArrayCell(Id(str),[Id(s)]),ArrayCell(Id(str),[Id(e)])),Block([Return(BooleanLit(False))])),If(BinaryOp(<,Id(s),BinaryOp(+,Id(e),IntLit(1))),Block([Return(CallExpr(Self(),Id(isPalRec),[Id(str),BinaryOp(+,Id(s),IntLit(1)),BinaryOp(-,Id(e),IntLit(1))]))])),Return(BooleanLit(True))])),MethodDecl(Id(isPalindrome),Instance,[param(Id(str),ArrayType(100,StringType))],Block([ConstDecl(Id(n),IntType,CallExpr(Id(Str),Id(strlen),[Id(str)])),If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(BooleanLit(True))])),Return(CallExpr(Self(),Id(isPalRec),[Id(str),IntLit(0),BinaryOp(-,Id(n),IntLit(1))]))])),MethodDecl(Id(SumRecursion),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(0))])),Return(BinaryOp(+,Id(n),CallExpr(Self(),Id(SumRecursion),[BinaryOp(-,Id(n),IntLit(1))])))])),MethodDecl(Id(Fibonacci),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(n),IntLit(1)),BinaryOp(==,Id(n),IntLit(2))),Block([Return(IntLit(1))])),Return(BinaryOp(+,CallExpr(Self(),Id(Fibonacci),[BinaryOp(-,Id(n),IntLit(1))]),CallExpr(Self(),Id(Fibonacci),[BinaryOp(-,Id(n),IntLit(2))])))])),MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(1))])),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))])))]))])])"""
		self.assertTrue(TestAST.test(input,expect,375))
        
	def test76(self):
		input = """
		Class Program {
			Test() {
				a = Self.b + Self.c() - Mains::$method(a,b,c) * ((r >= 6) && (17 - 10e3));
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Test),Instance,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,FieldAccess(Self(),Id(b)),CallExpr(Self(),Id(c),[])),BinaryOp(*,CallExpr(Id(Mains),Id($method),[Id(a),Id(b),Id(c)]),BinaryOp(&&,BinaryOp(>=,Id(r),IntLit(6)),BinaryOp(-,IntLit(17),FloatLit(10000.0))))))]))])])"""
		self.assertTrue(TestAST.test(input,expect,376))
    
	def test77(self):
		input = """
        Class Test {
			swap(arr: Array[Int, 100]; i: Int; j: Int)
            {
				Var temp: Int = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
        """
		expect = """Program([ClassDecl(Id(Test),[MethodDecl(Id(swap),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(i),IntType),param(Id(j),IntType)],Block([VarDecl(Id(temp),IntType,ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))]))])])"""
		self.assertTrue(TestAST.test(input,expect,377))
        
	def test78(self):
		input = """
        Class testAlgorithms {
            getMin(arr: Array[Int, 10]; n: Int)
            {
				Var min: Int = arr[0];
				Foreach (i In 1 .. n By 1) {
					If (arr[i] < min) {
						min = arr[i];
					}
				}
				Return min;
            }
        }
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(getMin),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(min),IntType,ArrayCell(Id(arr),[IntLit(0)])),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(i)]),Id(min)),Block([AssignStmt(Id(min),ArrayCell(Id(arr),[Id(i)]))]))])]),Return(Id(min))]))])])"""
		self.assertTrue(TestAST.test(input,expect,378))

	def test79(self):
		input = """
		Class Program {
			Var ab: Int;
			Val $c, d: Float = 1.2, 3.41;    
			func() {
				If (a > c) {
					If (b < d) {
						b = d;
					}
					Elseif (b == d) {
						b = d - 1;
					} 
					Elseif (b > d) {
						b = d + 1;
					}
					Else {
						d = b - 1;
					}
				}
				Elseif (a == c) {
					a = c ;
				}
				Else {
					a = c + 1;
				}
				Return a;
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(ab),IntType)),AttributeDecl(Static,ConstDecl(Id($c),FloatType,FloatLit(1.2))),AttributeDecl(Instance,ConstDecl(Id(d),FloatType,FloatLit(3.41))),MethodDecl(Id(func),Instance,[],Block([If(BinaryOp(>,Id(a),Id(c)),Block([If(BinaryOp(<,Id(b),Id(d)),Block([AssignStmt(Id(b),Id(d))]),If(BinaryOp(==,Id(b),Id(d)),Block([AssignStmt(Id(b),BinaryOp(-,Id(d),IntLit(1)))]),If(BinaryOp(>,Id(b),Id(d)),Block([AssignStmt(Id(b),BinaryOp(+,Id(d),IntLit(1)))]),Block([AssignStmt(Id(d),BinaryOp(-,Id(b),IntLit(1)))]))))]),If(BinaryOp(==,Id(a),Id(c)),Block([AssignStmt(Id(a),Id(c))]),Block([AssignStmt(Id(a),BinaryOp(+,Id(c),IntLit(1)))]))),Return(Id(a))]))])])"""
		self.assertTrue(TestAST.test(input,expect,379))
    
	def test80(self):
		input = """
        Class EncryptedText {
            encryption(rawText: String; key: Int) {
                If (key < 0) {
                    key = (key % 26) + 26;
                }
                Elseif (key >= 26) {
                    key = key % 26;
                }
                Var idx: Int = 0;
                Var temp: Int = rawText[idx] + key;
                If ((rawText[i] <= "z") && (temp > "z") || (rawText[i] <= "Z") && (temp > "Z")) {
                    temp = temp - 26;
                }
                rawText[i] = temp;
                i = i + 1;
            }
        }
        """
		expect = """Program([ClassDecl(Id(EncryptedText),[MethodDecl(Id(encryption),Instance,[param(Id(rawText),StringType),param(Id(key),IntType)],Block([If(BinaryOp(<,Id(key),IntLit(0)),Block([AssignStmt(Id(key),BinaryOp(+,BinaryOp(%,Id(key),IntLit(26)),IntLit(26)))]),If(BinaryOp(>=,Id(key),IntLit(26)),Block([AssignStmt(Id(key),BinaryOp(%,Id(key),IntLit(26)))]))),VarDecl(Id(idx),IntType,IntLit(0)),VarDecl(Id(temp),IntType,BinaryOp(+,ArrayCell(Id(rawText),[Id(idx)]),Id(key))),If(BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(<=,ArrayCell(Id(rawText),[Id(i)]),StringLit(z)),BinaryOp(>,Id(temp),StringLit(z))),BinaryOp(<=,ArrayCell(Id(rawText),[Id(i)]),StringLit(Z))),BinaryOp(>,Id(temp),StringLit(Z))),Block([AssignStmt(Id(temp),BinaryOp(-,Id(temp),IntLit(26)))])),AssignStmt(ArrayCell(Id(rawText),[Id(i)]),Id(temp)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,380))
        
	def test81(self):
		input = """
		Class Program {
			Val $c, d: Float = 1.2, 3.41;    
			func() {
				If (a > c) {
					If (b < d) {
						b = d;
					}
					Elseif (b == d) {
						b = d - 1;
					}
				}
				Elseif (a == c) {
					a = c ;
				}
				Return (a || b);
			}
		}
		"""
		expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($c),FloatType,FloatLit(1.2))),AttributeDecl(Instance,ConstDecl(Id(d),FloatType,FloatLit(3.41))),MethodDecl(Id(func),Instance,[],Block([If(BinaryOp(>,Id(a),Id(c)),Block([If(BinaryOp(<,Id(b),Id(d)),Block([AssignStmt(Id(b),Id(d))]),If(BinaryOp(==,Id(b),Id(d)),Block([AssignStmt(Id(b),BinaryOp(-,Id(d),IntLit(1)))])))]),If(BinaryOp(==,Id(a),Id(c)),Block([AssignStmt(Id(a),Id(c))]))),Return(BinaryOp(||,Id(a),Id(b)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,381))
        
	def test82(self):
		input = """
        Class ArrayAlgorithms {
            getMin(arr: Array[Int, 10]; n: Int)
            {
				Var min: Int = arr[0];
				Foreach (i In 1 .. n By 1) {
					If (arr[i] < min) {
						min = arr[i];
					}
				}
				Return min;
            }
			getMax(arr: Array[Int, 10]; n: Int)
            {
				Var mx: Int = arr[0];
				Foreach (i In 1 .. n By 1) {
					If (arr[i] > mx) {
						mx = arr[i];
					}
				}
				Return mx;
            }
            printArray(arr: Array[Int, 100])
            {
				Val n: Int = arr.length();
				Foreach (i In 0 .. n By 1) {
					System.out.print(arr[i] + " ");
				}
				System.out.println();
            }
		}
        """
		expect = """Program([ClassDecl(Id(ArrayAlgorithms),[MethodDecl(Id(getMin),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(min),IntType,ArrayCell(Id(arr),[IntLit(0)])),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(i)]),Id(min)),Block([AssignStmt(Id(min),ArrayCell(Id(arr),[Id(i)]))]))])]),Return(Id(min))])),MethodDecl(Id(getMax),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(n),IntType)],Block([VarDecl(Id(mx),IntType,ArrayCell(Id(arr),[IntLit(0)])),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(i)]),Id(mx)),Block([AssignStmt(Id(mx),ArrayCell(Id(arr),[Id(i)]))]))])]),Return(Id(mx))])),MethodDecl(Id(printArray),Instance,[param(Id(arr),ArrayType(100,IntType))],Block([ConstDecl(Id(n),IntType,CallExpr(Id(arr),Id(length),[])),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,ArrayCell(Id(arr),[Id(i)]),StringLit( ))])])]),Call(FieldAccess(Id(System),Id(out)),Id(println),[])]))])])"""
		self.assertTrue(TestAST.test(input,expect,382))
        
	def test83(self):
		input = """
        Class testArray {
			Var arr: Array[Array[String, 3], 3] = Array (
                Array("Volvo", "22", "18"),
                Array("Saab", "5", "2"),
                Array("Land Rover", "17", "15")
            );
		}
        """
		expect = """Program([ClassDecl(Id(testArray),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]))])])"""
		self.assertTrue(TestAST.test(input,expect,383))
    
	def test84(self):
		input = """
        Class SolveEquation {
            Var delta: Float;
            Var x: Array[Float, 2];
			twoDegEquation() {
				## a^2 + bx + c = 0 ##
				If (a == 0) {
					If (b != 0) {
						Var x: Float;
						Self.x[0] = Math.round((-c/b) * 100.0) / 100.0;
						Return Self.x[0];
					}
					Elseif (b==0) {
						System.out.println("Wrong equation format !!!");
						Return;
					}
				}
				Else {
					Self.delta = b*b - 4*a*c;
					If (Self.delta < 0) {
						System.out.println("Can't solve equation");
					}
					Elseif (delta == 0) {
						Self.x[0] = (-b) / (2*a);
						System.out.println("The equation has one root: ");
						System.out.println(Math.round(Self.x[0]));
					}
					Else {
						Self.x[0] = (-b) + Math.sqrt(delta) / (2*a);
						Self.x[1] = (-b) - Math.sqrt(delta) / (2*a);
						System.out.println("The equation has two roots: ");
						System.out.println(Math.round(Self.x[0]) + " and " + Math.round(Self.x[1]));
					}
				}
            }
        }
        """
		expect = """Program([ClassDecl(Id(SolveEquation),[AttributeDecl(Instance,VarDecl(Id(delta),FloatType)),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,FloatType))),MethodDecl(Id(twoDegEquation),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([If(BinaryOp(!=,Id(b),IntLit(0)),Block([VarDecl(Id(x),FloatType),AssignStmt(ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)]),BinaryOp(/,CallExpr(Id(Math),Id(round),[BinaryOp(*,BinaryOp(/,UnaryOp(-,Id(c)),Id(b)),FloatLit(100.0))]),FloatLit(100.0))),Return(ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)]))]),If(BinaryOp(==,Id(b),IntLit(0)),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Wrong equation format !!!)]),Return()])))]),Block([AssignStmt(FieldAccess(Self(),Id(delta)),BinaryOp(-,BinaryOp(*,Id(b),Id(b)),BinaryOp(*,BinaryOp(*,IntLit(4),Id(a)),Id(c)))),If(BinaryOp(<,FieldAccess(Self(),Id(delta)),IntLit(0)),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Can't solve equation)])]),If(BinaryOp(==,Id(delta),IntLit(0)),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)]),BinaryOp(/,UnaryOp(-,Id(b)),BinaryOp(*,IntLit(2),Id(a)))),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(The equation has one root: )]),Call(FieldAccess(Id(System),Id(out)),Id(println),[CallExpr(Id(Math),Id(round),[ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)])])])]),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)]),BinaryOp(+,UnaryOp(-,Id(b)),BinaryOp(/,CallExpr(Id(Math),Id(sqrt),[Id(delta)]),BinaryOp(*,IntLit(2),Id(a))))),AssignStmt(ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(1)]),BinaryOp(-,UnaryOp(-,Id(b)),BinaryOp(/,CallExpr(Id(Math),Id(sqrt),[Id(delta)]),BinaryOp(*,IntLit(2),Id(a))))),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(The equation has two roots: )]),Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,BinaryOp(+,CallExpr(Id(Math),Id(round),[ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)])]),StringLit( and )),CallExpr(Id(Math),Id(round),[ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(1)])]))])])))]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,384))
    
	def test85(self):
		input = """
		Class Student {
            Val firstName: String;
            Val lastName: String;
            Var ID: Int;
            getFirstName() {
				Return Self.firstName;
            }
            getLastName() {
				Return Self.lastName;
            }
            getID() {
				Return Self.ID;
            }
            Constructor(firstName: String; lastName: String; ID: Int) {
				Self.firstName = firstName;
				Self.lastName = lastName;
				Self.ID = ID;
            }
            Destructor() {
                    
            }
        }
            
        Class Program {
            main() {
				Var first_student: Student = New Student("Nguyen", "Ton", "1915570");
				Var second_student: Student = New Student("Vox", "Ton", "1915570");
				If (first_student.getFirstName() ==. second_student.getFirstName()) {
					If (first_student.getLastName() ==. second_student.getLastName()) {
						If (first_student.getID() == second_student.getID()) {
							System.out.println("Same student");
						}
						Else {
							System.out.println("Same name");
						}
					}
					Else {
						System.out.println("Same firstname");
					}
				}
				Else {
					System.out.println("Different student");
				}
            }
		}
		"""
		expect = """Program([ClassDecl(Id(Student),[AttributeDecl(Instance,ConstDecl(Id(firstName),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(lastName),StringType,None)),AttributeDecl(Instance,VarDecl(Id(ID),IntType)),MethodDecl(Id(getFirstName),Instance,[],Block([Return(FieldAccess(Self(),Id(firstName)))])),MethodDecl(Id(getLastName),Instance,[],Block([Return(FieldAccess(Self(),Id(lastName)))])),MethodDecl(Id(getID),Instance,[],Block([Return(FieldAccess(Self(),Id(ID)))])),MethodDecl(Id(Constructor),Instance,[param(Id(firstName),StringType),param(Id(lastName),StringType),param(Id(ID),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(firstName)),Id(firstName)),AssignStmt(FieldAccess(Self(),Id(lastName)),Id(lastName)),AssignStmt(FieldAccess(Self(),Id(ID)),Id(ID))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(first_student),ClassType(Id(Student)),NewExpr(Id(Student),[StringLit(Nguyen),StringLit(Ton),StringLit(1915570)])),VarDecl(Id(second_student),ClassType(Id(Student)),NewExpr(Id(Student),[StringLit(Vox),StringLit(Ton),StringLit(1915570)])),If(BinaryOp(==.,CallExpr(Id(first_student),Id(getFirstName),[]),CallExpr(Id(second_student),Id(getFirstName),[])),Block([If(BinaryOp(==.,CallExpr(Id(first_student),Id(getLastName),[]),CallExpr(Id(second_student),Id(getLastName),[])),Block([If(BinaryOp(==,CallExpr(Id(first_student),Id(getID),[]),CallExpr(Id(second_student),Id(getID),[])),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Same student)])]),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Same name)])]))]),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Same firstname)])]))]),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Different student)])]))]))])])"""
		self.assertTrue(TestAST.test(input, expect, 385))
        
	def test86(self):
		input = """
		Class Program {
			getArr() {
				Val PI: Float = 3.1415926;
				(arr[3])[1] = 5.15;
			}               
		}
		"""
		expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArr),Instance,[],Block([ConstDecl(Id(PI),FloatType,FloatLit(3.1415926)),AssignStmt(ArrayCell(ArrayCell(Id(arr),[IntLit(3)]),[IntLit(1)]),FloatLit(5.15))]))])])"""
		self.assertTrue(TestAST.test(input, expect, 386))

	def test87(self):
		input = """
		Class Program {
			getArr() {
				Val PI: Float = 3.1415926;
				(arr[3])[1] = 5.15;
			}               
		}
		"""
		expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArr),Instance,[],Block([ConstDecl(Id(PI),FloatType,FloatLit(3.1415926)),AssignStmt(ArrayCell(ArrayCell(Id(arr),[IntLit(3)]),[IntLit(1)]),FloatLit(5.15))]))])])"""
		self.assertTrue(TestAST.test(input, expect, 387))
        
	def test88(self):
		input = """Class Expr {
            Val a: Int = A.a;
            Var b: Float = c.d[1];
            Val e: String = f.g[1][2];
            Var h: Int = Number::$num;
            Var i: Boolean = Number::$dec[0];
            Val j: String = Number.qq[0];
            Val k: Float = Number.qq;
        }"""
		expect = """Program([ClassDecl(Id(Expr),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,FieldAccess(Id(A),Id(a)))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,ArrayCell(FieldAccess(Id(c),Id(d)),[IntLit(1)]))),AttributeDecl(Instance,ConstDecl(Id(e),StringType,ArrayCell(FieldAccess(Id(f),Id(g)),[IntLit(1),IntLit(2)]))),AttributeDecl(Instance,VarDecl(Id(h),IntType,FieldAccess(Id(Number),Id($num)))),AttributeDecl(Instance,VarDecl(Id(i),BoolType,ArrayCell(FieldAccess(Id(Number),Id($dec)),[IntLit(0)]))),AttributeDecl(Instance,ConstDecl(Id(j),StringType,ArrayCell(FieldAccess(Id(Number),Id(qq)),[IntLit(0)]))),AttributeDecl(Instance,ConstDecl(Id(k),FloatType,FieldAccess(Id(Number),Id(qq))))])])"""
		self.assertTrue(TestAST.test(input,expect,388))
        
	def test89(self):
		input = """
		Class Program {
			main() {
				Val testArray: Array[Int, 5]= Array(1, 2, 3, 4, 5);
				Var multi_dimension_array: Array[Array[String, 5], 5];
				Foreach (i In 1 .. 5) {
					Foreach (j In 1 .. 5) {
						multi_dimension_array[i][j] = testArray[i];
					}
				}
			}
		}
		"""
		expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(testArray),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),VarDecl(Id(multi_dimension_array),ArrayType(5,ArrayType(5,StringType))),For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([For(Id(j),IntLit(1),IntLit(5),IntLit(1),Block([AssignStmt(ArrayCell(Id(multi_dimension_array),[Id(i),Id(j)]),ArrayCell(Id(testArray),[Id(i)]))])])])])]))])])"
		self.assertTrue(TestAST.test(input, expect, 389))
    
	def test90(self):
		input = """
        Class testAlgorithms {
			heapify (arr: Array[Int, 100]; n: Int; i: Int)
            {
				Var largest: Int = i;
				Var l: Int = 2 * i + 1;
				Var r: Int = 2 * i + 2;
				If ((l < n) && (arr[l] > arr[largest])) {
					largest = l;
				}
				If ((r < n) && (arr[r] > arr[largest])) {
					largest = r;
				}
				If (largest != i) {
					Var swap: Int = arr[i];
					arr[i] = arr[largest];
					arr[largest] = swap;
					Self.heapify(arr, n, largest);
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(testAlgorithms),[MethodDecl(Id(heapify),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(i),IntType)],Block([VarDecl(Id(largest),IntType,Id(i)),VarDecl(Id(l),IntType,BinaryOp(+,BinaryOp(*,IntLit(2),Id(i)),IntLit(1))),VarDecl(Id(r),IntType,BinaryOp(+,BinaryOp(*,IntLit(2),Id(i)),IntLit(2))),If(BinaryOp(&&,BinaryOp(<,Id(l),Id(n)),BinaryOp(>,ArrayCell(Id(arr),[Id(l)]),ArrayCell(Id(arr),[Id(largest)]))),Block([AssignStmt(Id(largest),Id(l))])),If(BinaryOp(&&,BinaryOp(<,Id(r),Id(n)),BinaryOp(>,ArrayCell(Id(arr),[Id(r)]),ArrayCell(Id(arr),[Id(largest)]))),Block([AssignStmt(Id(largest),Id(r))])),If(BinaryOp(!=,Id(largest),Id(i)),Block([VarDecl(Id(swap),IntType,ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(largest)])),AssignStmt(ArrayCell(Id(arr),[Id(largest)]),Id(swap)),Call(Self(),Id(heapify),[Id(arr),Id(n),Id(largest)])]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,390))
    
	def test91(self):
		input = """
        Class  Spider_man {
			countOccurrences(arr: Array[Int, 100]; n: Int; x: Int)
            {
				Var res: Int = 0;
				Foreach (i In 0 .. n By 1) {
					If (x == arr[i]) {
						res = res + 1;
					}
				}
				Return res;
            }
		}
        """
		expect = """Program([ClassDecl(Id(Spider_man),[MethodDecl(Id(countOccurrences),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(x),IntType)],Block([VarDecl(Id(res),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([If(BinaryOp(==,Id(x),ArrayCell(Id(arr),[Id(i)])),Block([AssignStmt(Id(res),BinaryOp(+,Id(res),IntLit(1)))]))])]),Return(Id(res))]))])])"""
		self.assertTrue(TestAST.test(input,expect,391))
        
	def test92(self):
		input = """
		Class Number {
			$testRandom() {
				Return (3 + 5.8 - a + !x <= 3.14) || ((y - z) * (x + y));
			}
		}
		Class Program {
			main() {
				Var a: Int = 1;
				Return Self.idx(a);
			}
		}
		"""
		expect = "Program([ClassDecl(Id(Number),[MethodDecl(Id($testRandom),Static,[],Block([Return(BinaryOp(||,BinaryOp(<=,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(3),FloatLit(5.8)),Id(a)),UnaryOp(!,Id(x))),FloatLit(3.14)),BinaryOp(*,BinaryOp(-,Id(y),Id(z)),BinaryOp(+,Id(x),Id(y)))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(1)),Return(CallExpr(Self(),Id(idx),[Id(a)]))]))])])"
		self.assertTrue(TestAST.test(input, expect, 392))
    
	def test93(self):
		input = """
            Class main {
                randomFunc(n, b: Int) {
                    If ((n == 0) || (a > 7) || (x <= 15)) {
                        Return (n + b);
                    }
                    
                    Var sb: StringBuilder = New StringBuilder();
                    Val y: Float = 3.14;
                    Var gemini: String = "Gemini";
					If (b > 10) {
						m = remainder % b;
						If (m >= 10) {
							sb.append(CHAR_55 + m);
						} Else {
							sb.append(m);
						}
					} Else {
						sb.append(remainder % b);
					}
					remainder = remainder / b;

                    Return sb.reverse();
                }
            }
            """
		expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(randomFunc),Instance,[param(Id(n),IntType),param(Id(b),IntType)],Block([If(BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(n),IntLit(0)),BinaryOp(>,Id(a),IntLit(7))),BinaryOp(<=,Id(x),IntLit(15))),Block([Return(BinaryOp(+,Id(n),Id(b)))])),VarDecl(Id(sb),ClassType(Id(StringBuilder)),NewExpr(Id(StringBuilder),[])),ConstDecl(Id(y),FloatType,FloatLit(3.14)),VarDecl(Id(gemini),StringType,StringLit(Gemini)),If(BinaryOp(>,Id(b),IntLit(10)),Block([AssignStmt(Id(m),BinaryOp(%,Id(remainder),Id(b))),If(BinaryOp(>=,Id(m),IntLit(10)),Block([Call(Id(sb),Id(append),[BinaryOp(+,Id(CHAR_55),Id(m))])]),Block([Call(Id(sb),Id(append),[Id(m)])]))]),Block([Call(Id(sb),Id(append),[BinaryOp(%,Id(remainder),Id(b))])])),AssignStmt(Id(remainder),BinaryOp(/,Id(remainder),Id(b))),Return(CallExpr(Id(sb),Id(reverse),[]))]))])])"
		self.assertTrue(TestAST.test(input, expect, 393))
    
	def test94(self):
		input = """
        Class  Spider_man {
			countSort(inArr: Array[Int, 100]; n: Int; exponent: Int)
            {
				Var result: Array[Int, 250];
				Var count: Array[Int, 10] = Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
				Foreach (i In 0 .. n By 1) {
					Val tmp: Int = (inArr[i] / exponent) % 10;
					count[tmp] = count[tmp] + 1;
				}
				Foreach (i In 1 .. 10 By 1) {
					count[i] = count[i] + count[i - 1];
				}
				Foreach (i In (n - 1) .. 0 By -1) {
					Val tmp: Int = (inArr[i] / exponent) % 10;
					result[count[tmp] - 1] = inArr[i];
					count[tmp] = count[tmp] - 1;
				}
				Foreach (i In 0 .. n By 1) {
					inArr[i] = result[i];
				}
            }
		}
        """
		expect = """Program([ClassDecl(Id(Spider_man),[MethodDecl(Id(countSort),Instance,[param(Id(inArr),ArrayType(100,IntType)),param(Id(n),IntType),param(Id(exponent),IntType)],Block([VarDecl(Id(result),ArrayType(250,IntType)),VarDecl(Id(count),ArrayType(10,IntType),[IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0),IntLit(0)]),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([ConstDecl(Id(tmp),IntType,BinaryOp(%,BinaryOp(/,ArrayCell(Id(inArr),[Id(i)]),Id(exponent)),IntLit(10))),AssignStmt(ArrayCell(Id(count),[Id(tmp)]),BinaryOp(+,ArrayCell(Id(count),[Id(tmp)]),IntLit(1)))])]),For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([AssignStmt(ArrayCell(Id(count),[Id(i)]),BinaryOp(+,ArrayCell(Id(count),[Id(i)]),ArrayCell(Id(count),[BinaryOp(-,Id(i),IntLit(1))])))])]),For(Id(i),BinaryOp(-,Id(n),IntLit(1)),IntLit(0),UnaryOp(-,IntLit(1)),Block([ConstDecl(Id(tmp),IntType,BinaryOp(%,BinaryOp(/,ArrayCell(Id(inArr),[Id(i)]),Id(exponent)),IntLit(10))),AssignStmt(ArrayCell(Id(result),[BinaryOp(-,ArrayCell(Id(count),[Id(tmp)]),IntLit(1))]),ArrayCell(Id(inArr),[Id(i)])),AssignStmt(ArrayCell(Id(count),[Id(tmp)]),BinaryOp(-,ArrayCell(Id(count),[Id(tmp)]),IntLit(1)))])]),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([AssignStmt(ArrayCell(Id(inArr),[Id(i)]),ArrayCell(Id(result),[Id(i)]))])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,394))
        
	def test95(self):
		input = """
        Class Search {
			interpolationSearch(arr: Array[Int, 100]; lo, hi, x: Int) {
				Var pos: Int;
				If ((lo <= hi) && (x >= arr[lo]) && (x <= arr[hi])) {
					pos = lo + (((hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));
					If (arr[pos] == x) {
						Return pos;
					}
					Elseif (arr[pos] < x) {
						Return Self.interpolationSearch(arr, pos + 1, hi, x);
					}
					Elseif (arr[pos] > x) {
						Return Self.interpolationSearch(arr, lo, pos - 1, x);
					}
				}
				Return -1;
			}
		}
        """
		expect = """Program([ClassDecl(Id(Search),[MethodDecl(Id(interpolationSearch),Instance,[param(Id(arr),ArrayType(100,IntType)),param(Id(lo),IntType),param(Id(hi),IntType),param(Id(x),IntType)],Block([VarDecl(Id(pos),IntType),If(BinaryOp(&&,BinaryOp(&&,BinaryOp(<=,Id(lo),Id(hi)),BinaryOp(>=,Id(x),ArrayCell(Id(arr),[Id(lo)]))),BinaryOp(<=,Id(x),ArrayCell(Id(arr),[Id(hi)]))),Block([AssignStmt(Id(pos),BinaryOp(+,Id(lo),BinaryOp(*,BinaryOp(/,BinaryOp(-,Id(hi),Id(lo)),BinaryOp(-,ArrayCell(Id(arr),[Id(hi)]),ArrayCell(Id(arr),[Id(lo)]))),BinaryOp(-,Id(x),ArrayCell(Id(arr),[Id(lo)]))))),If(BinaryOp(==,ArrayCell(Id(arr),[Id(pos)]),Id(x)),Block([Return(Id(pos))]),If(BinaryOp(<,ArrayCell(Id(arr),[Id(pos)]),Id(x)),Block([Return(CallExpr(Self(),Id(interpolationSearch),[Id(arr),BinaryOp(+,Id(pos),IntLit(1)),Id(hi),Id(x)]))]),If(BinaryOp(>,ArrayCell(Id(arr),[Id(pos)]),Id(x)),Block([Return(CallExpr(Self(),Id(interpolationSearch),[Id(arr),Id(lo),BinaryOp(-,Id(pos),IntLit(1)),Id(x)]))]))))])),Return(UnaryOp(-,IntLit(1)))]))])])"""
		self.assertTrue(TestAST.test(input,expect,395))
    
	def test96(self):
		input = """
        Class Permutation
		{
			main()
			{
				Val str: String = "ABC";
				Var n: Int = str.length();
				Var permutation: Permutation = New Permutation();
				permutation.permute(str, 0, n-1);
			}
		
			permute(str: String; l, r: Int)
			{
				If (l == r) {
					System.out.println(str);
				}
				Else
				{
					Foreach (i In l .. r)
					{
						str = Algorithms.swap(str, l, i);
						Self.permute(str, l+1, r);
						str = Algorithms.swap(str, l, i);
					}
				}
			}
			swap(a: String; i, j: Int)
			{
				Var temp: String;
				Var charArray: Array[String, 100] = a.toCharArray();
				temp = charArray[i];
				charArray[i] = charArray[j];
				charArray[j] = temp;
				Return toString.valueOf(charArray);
			}
		}
        """
		expect = """Program([ClassDecl(Id(Permutation),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(str),StringType,StringLit(ABC)),VarDecl(Id(n),IntType,CallExpr(Id(str),Id(length),[])),VarDecl(Id(permutation),ClassType(Id(Permutation)),NewExpr(Id(Permutation),[])),Call(Id(permutation),Id(permute),[Id(str),IntLit(0),BinaryOp(-,Id(n),IntLit(1))])])),MethodDecl(Id(permute),Instance,[param(Id(str),StringType),param(Id(l),IntType),param(Id(r),IntType)],Block([If(BinaryOp(==,Id(l),Id(r)),Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[Id(str)])]),Block([For(Id(i),Id(l),Id(r),IntLit(1),Block([AssignStmt(Id(str),CallExpr(Id(Algorithms),Id(swap),[Id(str),Id(l),Id(i)])),Call(Self(),Id(permute),[Id(str),BinaryOp(+,Id(l),IntLit(1)),Id(r)]),AssignStmt(Id(str),CallExpr(Id(Algorithms),Id(swap),[Id(str),Id(l),Id(i)]))])])]))])),MethodDecl(Id(swap),Instance,[param(Id(a),StringType),param(Id(i),IntType),param(Id(j),IntType)],Block([VarDecl(Id(temp),StringType),VarDecl(Id(charArray),ArrayType(100,StringType),CallExpr(Id(a),Id(toCharArray),[])),AssignStmt(Id(temp),ArrayCell(Id(charArray),[Id(i)])),AssignStmt(ArrayCell(Id(charArray),[Id(i)]),ArrayCell(Id(charArray),[Id(j)])),AssignStmt(ArrayCell(Id(charArray),[Id(j)]),Id(temp)),Return(CallExpr(Id(toString),Id(valueOf),[Id(charArray)]))]))])])"""
		self.assertTrue(TestAST.test(input,expect,396))
        
	def test97(self):
		input = """
        Class Job
		{
			Var id: String;
			Var deadline, profit: Int;
			Job() {}
		
			Job(id: String; deadline, profit: Int)
			{
				Self.id = id;
				Self.deadline = deadline;
				Self.profit = profit;
			}
			printJobScheduling(arr: Array[String, 100]; t: Int)
			{
				Var n: Int = arr.size();
				Collections.sort(arr, b.profit - a.profit);
				Var result: Array[Boolean, 100];
				Var job: Array[String, 100];
				Foreach (i In 0 .. n)
				{
					Foreach (j In Math.min(t - 1, arr.get(i).deadline - 1) .. 0 By -1) {
						If (result[j] == false)
						{
							result[j] = true;
							job[j] = arr.get(i).id;
							Break;
						}
					}
				}
				Foreach (jb In job[0] .. job[size])
				{
					System.out.print(jb + " ");
				}
				System.out.println();
			}
		}
        """
		expect = """Program([ClassDecl(Id(Job),[AttributeDecl(Instance,VarDecl(Id(id),StringType)),AttributeDecl(Instance,VarDecl(Id(deadline),IntType)),AttributeDecl(Instance,VarDecl(Id(profit),IntType)),MethodDecl(Id(Job),Instance,[],Block([])),MethodDecl(Id(Job),Instance,[param(Id(id),StringType),param(Id(deadline),IntType),param(Id(profit),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(id)),Id(id)),AssignStmt(FieldAccess(Self(),Id(deadline)),Id(deadline)),AssignStmt(FieldAccess(Self(),Id(profit)),Id(profit))])),MethodDecl(Id(printJobScheduling),Instance,[param(Id(arr),ArrayType(100,StringType)),param(Id(t),IntType)],Block([VarDecl(Id(n),IntType,CallExpr(Id(arr),Id(size),[])),Call(Id(Collections),Id(sort),[Id(arr),BinaryOp(-,FieldAccess(Id(b),Id(profit)),FieldAccess(Id(a),Id(profit)))]),VarDecl(Id(result),ArrayType(100,BoolType)),VarDecl(Id(job),ArrayType(100,StringType)),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([For(Id(j),CallExpr(Id(Math),Id(min),[BinaryOp(-,Id(t),IntLit(1)),BinaryOp(-,FieldAccess(CallExpr(Id(arr),Id(get),[Id(i)]),Id(deadline)),IntLit(1))]),IntLit(0),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(==,ArrayCell(Id(result),[Id(j)]),Id(false)),Block([AssignStmt(ArrayCell(Id(result),[Id(j)]),Id(true)),AssignStmt(ArrayCell(Id(job),[Id(j)]),FieldAccess(CallExpr(Id(arr),Id(get),[Id(i)]),Id(id))),Break]))])])])]),For(Id(jb),ArrayCell(Id(job),[IntLit(0)]),ArrayCell(Id(job),[Id(size)]),IntLit(1),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+,Id(jb),StringLit( ))])])]),Call(FieldAccess(Id(System),Id(out)),Id(println),[])]))])])"""
		self.assertTrue(TestAST.test(input,expect,397))

	def test98(self):
		input = """
		Class StringAlgorithms {
			findLength(str: String)
			{
				Var n: Int = str.length();
				Var maxlen: Int = 0;
				Foreach (i In 0 .. n)
				{
					Foreach (j In i + 1 .. n By 2)
					{  
						Var length: Int = j - i + 1;
						Var leftsum, rightsum: Int = 0, 0;
						Foreach (k In 0 .. length/2)
						{
							leftsum = leftsum + (str.charAt(i + k) - "0");
							rightsum = rightSum + (str.charAt(i + k + length/2) - "0");
						}
						If ((leftsum == rightsum) && (maxlen < length)) {
							maxlen = length;
						}
					}
				}
				Return maxlen;
			}
		}
		"""
		expect = """Program([ClassDecl(Id(StringAlgorithms),[MethodDecl(Id(findLength),Instance,[param(Id(str),StringType)],Block([VarDecl(Id(n),IntType,CallExpr(Id(str),Id(length),[])),VarDecl(Id(maxlen),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([For(Id(j),BinaryOp(+,Id(i),IntLit(1)),Id(n),IntLit(2),Block([VarDecl(Id(length),IntType,BinaryOp(+,BinaryOp(-,Id(j),Id(i)),IntLit(1))),VarDecl(Id(leftsum),IntType,IntLit(0)),VarDecl(Id(rightsum),IntType,IntLit(0)),For(Id(k),IntLit(0),BinaryOp(/,Id(length),IntLit(2)),IntLit(1),Block([AssignStmt(Id(leftsum),BinaryOp(+,Id(leftsum),BinaryOp(-,CallExpr(Id(str),Id(charAt),[BinaryOp(+,Id(i),Id(k))]),StringLit(0)))),AssignStmt(Id(rightsum),BinaryOp(+,Id(rightSum),BinaryOp(-,CallExpr(Id(str),Id(charAt),[BinaryOp(+,BinaryOp(+,Id(i),Id(k)),BinaryOp(/,Id(length),IntLit(2)))]),StringLit(0))))])]),If(BinaryOp(&&,BinaryOp(==,Id(leftsum),Id(rightsum)),BinaryOp(<,Id(maxlen),Id(length))),Block([AssignStmt(Id(maxlen),Id(length))]))])])])]),Return(Id(maxlen))]))])])"""
		self.assertTrue(TestAST.test(input,expect,398))

	def test99(self):
		input = """
		Class randomAlgorithms {
			countSetBits(n: Int)
			{
					Var bitCount: Int = 0;
					Foreach (i In 1 .. n) {
						bitCount = bitCount + Self.countSetBitsUtil(i);
					}
					Return bitCount;
			}
			countSetBitsUtil(x: Int)
			{
					If (x <= 0) {
						Return 0;
					}
					Elseif (x % 2 == 0) {
						Return Self.countSetBitsUtil(x / 2);
					}
					Else {
						Return 1 + Self.countSetBitsUtil(x / 2);
					}
			}
			main()
			{
					Var n: Int = 4;
					System.out.print("Total set bit count is: ");
					System.out.print(Self.countSetBits(n));
			}
		}
		"""
		expect = """Program([ClassDecl(Id(randomAlgorithms),[MethodDecl(Id(countSetBits),Instance,[param(Id(n),IntType)],Block([VarDecl(Id(bitCount),IntType,IntLit(0)),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([AssignStmt(Id(bitCount),BinaryOp(+,Id(bitCount),CallExpr(Self(),Id(countSetBitsUtil),[Id(i)])))])]),Return(Id(bitCount))])),MethodDecl(Id(countSetBitsUtil),Instance,[param(Id(x),IntType)],Block([If(BinaryOp(<=,Id(x),IntLit(0)),Block([Return(IntLit(0))]),If(BinaryOp(==,BinaryOp(%,Id(x),IntLit(2)),IntLit(0)),Block([Return(CallExpr(Self(),Id(countSetBitsUtil),[BinaryOp(/,Id(x),IntLit(2))]))]),Block([Return(BinaryOp(+,IntLit(1),CallExpr(Self(),Id(countSetBitsUtil),[BinaryOp(/,Id(x),IntLit(2))])))])))])),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(n),IntType,IntLit(4)),Call(FieldAccess(Id(System),Id(out)),Id(print),[StringLit(Total set bit count is: )]),Call(FieldAccess(Id(System),Id(out)),Id(print),[CallExpr(Self(),Id(countSetBits),[Id(n)])])]))])])"""
		self.assertTrue(TestAST.test(input,expect,399))

	def test100(self):
		input = """
		Class randomAlgorithms {
			snoob(x: Int)
			{
					Var rightOne, nextHigherOneBit, rightOnesPattern, next: Int = 0, 0, 0, 0;
					If (x > 0)
					{
						rightOne = x && -x;
						nextHigherOneBit = x + rightOne;
						rightOnesPattern = Math.power(x, nextHigherOneBit);
						rightOnesPattern = rightOnesPattern / rightOne;
						next = nextHigherOneBit || rightOnesPattern;
					}
					Return next;
			}
		}
		"""
		expect = """Program([ClassDecl(Id(randomAlgorithms),[MethodDecl(Id(snoob),Instance,[param(Id(x),IntType)],Block([VarDecl(Id(rightOne),IntType,IntLit(0)),VarDecl(Id(nextHigherOneBit),IntType,IntLit(0)),VarDecl(Id(rightOnesPattern),IntType,IntLit(0)),VarDecl(Id(next),IntType,IntLit(0)),If(BinaryOp(>,Id(x),IntLit(0)),Block([AssignStmt(Id(rightOne),BinaryOp(&&,Id(x),UnaryOp(-,Id(x)))),AssignStmt(Id(nextHigherOneBit),BinaryOp(+,Id(x),Id(rightOne))),AssignStmt(Id(rightOnesPattern),CallExpr(Id(Math),Id(power),[Id(x),Id(nextHigherOneBit)])),AssignStmt(Id(rightOnesPattern),BinaryOp(/,Id(rightOnesPattern),Id(rightOne))),AssignStmt(Id(next),BinaryOp(||,Id(nextHigherOneBit),Id(rightOnesPattern)))])),Return(Id(next))]))])])"""
		self.assertTrue(TestAST.test(input,expect,400))