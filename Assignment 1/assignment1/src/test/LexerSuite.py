# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase):
#     def test1(self):
#         """test KEYWORD"""
#         self.assertTrue(TestLexer.test(
#             "Val Var Int Float Boolean String Array If Elseif Else True False Foreach In By Break Continue Return Null Class Constructor Destructor New Self",
#             "Val,Var,Int,Float,Boolean,String,Array,If,Elseif,Else,True,False,Foreach,In,By,Break,Continue,Return,Null,Class,Constructor,Destructor,New,Self,<EOF>",101))
        
#     def test2(self):
#         """test Comment"""
#         self.assertTrue(TestLexer.test(
#             "abc ##This is the comment so \n it shouldn't be compiled## xyz",
#             "abc,xyz,<EOF>",102)) 
    
#     def test3(self):
#         """test Comment"""
#         self.assertTrue(TestLexer.test(
#             "abc ## Comments is non-greedy so this case it will cause ## error ## xyz",
#             "abc,error,Error Token #",103))
    
#     def test4(self):
#         """test Comment"""
#         self.assertTrue(TestLexer.test(
#             """ "This is a string so compiler will not skip this part. ## See, it still appears in your string ## uWu" """,
#             "This is a string so compiler will not skip this part. ## See, it still appears in your string ## uWu,<EOF>",104))

#     def test5(self):
#         """test Identifiers"""
#         self.assertTrue(TestLexer.test(
#             "UwU uWu uWU ____D96___ P_P_L _ _MrDuy__ kHalAChaCKeO",
#             "UwU,uWu,uWU,____D96___,P_P_L,_,_MrDuy__,kHalAChaCKeO,<EOF>",105)) 
        
#     def test6(self):
#         """test Identifiers"""
#         self.assertTrue(TestLexer.test(
#             "Email toanvo4121@hcmut",
#             "Email,toanvo4121,Error Token @",106))
        
#     def test7(self):
#         """test Static Identifiers"""
#         self.assertTrue(TestLexer.test(
#             "$xoxo $0 $asap $Lambda $_MrDuy__",
#             "$xoxo,$0,$asap,$Lambda,$_MrDuy__,<EOF>",107))
        
#     def test8(self):
#         """test Static Identifiers"""
#         self.assertTrue(TestLexer.test(
#             "$$",
#             "Error Token $",108))
        
#     def test9(self):
#         """test INTLIT"""
#         self.assertTrue(TestLexer.test(
#             "00 0 0x0 0X0 0b0 0B0",
#             "00,0,0x0,0X0,0b0,0B0,<EOF>",109))
        
#     def test10(self):
#         """test INTLIT"""
#         self.assertTrue(TestLexer.test(
#             "0562_1315_02_464 3122_2_3_215_481_325 0xA_05BC_DE_F_4812 0B1_1_0_0_0101101_101011",
#             "0562131502464,312223215481325,0xA05BCDEF4812,0B11000101101101011,<EOF>",110))
        
#     def test11(self):
#         """test INTLIT"""
#         self.assertTrue(TestLexer.test(
#             "000x0000000 0xABCDEFTOANVO",
#             "00,0x0,00,00,00,0xABCDEF,TOANVO,<EOF>",111))
    
#     def test12(self):
#         """test INTLIT"""
#         self.assertTrue(TestLexer.test(
#             "0x41_FA_1D_2CB_1E5 00000000 012_123_56_7_987",
#             "0x41FA1D2CB1E5,00,00,00,00,012123567,_987,<EOF>",112))
        
#     def test13(self):
#         """test INTLIT"""
#         self.assertTrue(TestLexer.test(
#             "0X1230A 0B10_0_101_10",
#             "0X1230A,0B10010110,<EOF>",113))
    
#     def test14(self):
#         """test INTLIT"""
#         self.assertTrue(TestLexer.test(
#             "00001_0150_1501_522_ABC_1121 0_x15a5_BaE1_20CdF_ 145_15_1_16_",
#             "00,00,101501501522,_ABC_1121,0,_x15a5_BaE1_20CdF_,14515116,_,<EOF>",114))
        
#     def test15(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             "5.5146e1 0.2694e15",
#             "5.5146e1,0.2694e15,<EOF>",115))
        
#     def test16(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             "123.34546e12 1_31_513.0405e12 1_2_3.00534e12",
#             "123.34546e12,131513.0405e12,123.00534e12,<EOF>",116))
        
#     def test17(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             "12_3.12_34_5e12 123.1_3_7_5e73 2683.1234e1_2",
#             "123.12,_34_5e12,123.1,_3_7_5e73,2683.1234e1,_2,<EOF>",117))
        
#     def test18(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             "00.792 32.567 21.00000000000 17.000000001 0.000000e0000000000",
#             "00,.,792,32.567,21.00000000000,17.000000001,0.000000e0000000000,<EOF>",118))
        
#     def test19(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             "0. 1. 2. 10. 99.",
#             "0.,1.,2.,10.,99.,<EOF>",119))
        
#     def test20(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             "1e2 1e0 12e12 12e000001",
#             "1e2,1e0,12e12,12e000001,<EOF>",120))
        
#     def test21(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             ".12e10 .00000e0 .4000004e006",
#             ".12e10,.00000e0,.4000004e006,<EOF>",121))
        
#     def test22(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             ".4 .3",
#             ".,4,.,3,<EOF>",122))
        
#     def test23(self):
#         """test VAR"""
#         self.assertTrue(TestLexer.test(
#             "Var phoneNumber: Int = 0399_575_679",
#             "Var,phoneNumber,:,Int,=,03,99575679,<EOF>",123))
        
#     def test24(self):
#         """test VAL"""
#         self.assertTrue(TestLexer.test(
#             """Val email: String = "toan.vo4121@hcmut.edu.vn" """,
#             "Val,email,:,String,=,toan.vo4121@hcmut.edu.vn,<EOF>",124)) 
        
#     def test25(self):
#         """test VAL"""
#         self.assertTrue(TestLexer.test(
#             """Val skills: Array[String,15]""",
#             "Val,skills,:,Array,[,String,,,15,],<EOF>",125))     
        
#     def test26(self):
#         """test VAL"""
#         self.assertTrue(TestLexer.test(
#             """Val rel_status: String= " """,
#             "Val,rel_status,:,String,=,Unclosed String:  ",126))  
        
#     def test27(self):
#         """test VAL"""
#         self.assertTrue(TestLexer.test(
#             """Val isGay: Boolean= False """,
#             "Val,isGay,:,Boolean,=,False,<EOF>",127))
        
#     def test28(self):
#         """test VAR"""
#         self.assertTrue(TestLexer.test(
#             """Var name: String = "Vo Minh Toan" """,
#             "Var,name,:,String,=,Vo Minh Toan,<EOF>",128))
#     def test29(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "CO3005 HCMUT-K19 \n - BKHCM" """,
#             """Unclosed String: CO3005 HCMUT-K19 """,129))
    
#     def test30(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "abc xyz" """,
#             "abc xyz,<EOF>",130))
        
#     def test31(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Hello '" cac ban khoe khong?" """,
#             """Hello '" cac ban khoe khong?,<EOF>""",131))
        
#     def test32(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Dieu anh luon giu kin trong tim '" """,
#             """Unclosed String: Dieu anh luon giu kin trong tim '" """,132))
        
#     def test33(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Hat mua roi bua '"vay trai ' tim hiu quanh '" " """,
#             """Hat mua roi bua '"vay trai ' tim hiu quanh '" ,<EOF>""",133))
        
#     def test34(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\fcomes great responsibility" """,
#             """Unclosed String: Great power""",134))
        
#     def test35(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\tcomes great responsibility" """,
#             """Illegal Escape In String: Great power	""",135))
        
#     def test36(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\\\\comes great responsibility" """,
#             """Great power\\\\comes great responsibility,<EOF>""",136))
        
#     def test37(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\'comes great responsibility" """,
#             """Great power\'comes great responsibility,<EOF>""",137))
        
#     def test38(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "CO3005 HCMUT-K19 \r - BKHCM" """,
#             """Unclosed String: CO3005 HCMUT-K19 """,138))
        
#     def test39(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "CO3005 HCMUT-K19 \f - BKHCM" """,
#             """Unclosed String: CO3005 HCMUT-K19 """,139))
    
#     def test40(self):
#         """test VAR"""
#         self.assertTrue(TestLexer.test(
#             """Var nationality: String = "Vietnam" """,
#             "Var,nationality,:,String,=,Vietnam,<EOF>",140))
        
#     def test41(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\hcomes great responsibility" """,
#             """Illegal Escape In String: Great power\h""",141))
        
#     def test42(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\\\hcomes great responsibility" """,
#             """Great power\\\hcomes great responsibility,<EOF>""",142))
        
#     def test43(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\jcomes great responsibility" """,
#             """Illegal Escape In String: Great power\j""",143))    
    
#     def test44(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power comes great responsibility """,
#             """Unclosed String: Great power comes great responsibility """,144))    
    
#     def test45(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "" """,
#             """,<EOF>""",145))
        
#     def test46(self):
#         """test STRING"""
#         self.assertTrue(TestLexer.test(
#             """ "Great power\\\\ """,
#             """Unclosed String: Great power\\\\ """,146))
        
#     def test47(self):
#         """test String var"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var greetings: String = "hi there\\"; 
#             """,
#             """Var,greetings,:,String,=,Illegal Escape In String: hi there\\""",147))
        
#     def test48(self):
#         """test String var"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var greetings: String = "hi there\\ 
#             """,
#             """Var,greetings,:,String,=,Unclosed String: hi there\\ """,148))
        
#     def test49(self):
#         """test String var"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var greetings: String = "hi there\t \y test" 
#             """,
#             """Var,greetings,:,String,=,Illegal Escape In String: hi there	""",149))
        
#     def test50(self):
#         """test String var"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var greetings: String = "hi there\t test";
#             Val $test: Float = 4_12.2001#15; 
#             """,
#             """Var,greetings,:,String,=,Illegal Escape In String: hi there	""",150))
        
#     def test51(self):
#         """test String var"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var _str1, _str2: String= "","";
#             """,
#             """Var,_str1,,,_str2,:,String,=,,,,,;,<EOF>""",151))
        
#     def test52(self):
#         """test String var"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var _str1, _str2: String= "",";
#             """,
#             """Var,_str1,,,_str2,:,String,=,,,,Unclosed String: ;""",152))
        
#     def test53(self):
#         """test String var"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var _str1, _str2: String= "'" ";
#             """,
#             """Var,_str1,,,_str2,:,String,=,'" ,;,<EOF>""",153))
        
#     def test54(self):
#         """test something"""
#         self.assertTrue(TestLexer.test(
#             """
#             [12, 24, 36, 48, 60, 72, 84, 96];
#             """,
#             """[,12,,,24,,,36,,,48,,,60,,,72,,,84,,,96,],;,<EOF>""",154))
        
#     def test55(self):
#         """test something"""
#         self.assertTrue(TestLexer.test(
#             """
#             [a, b, c, [ab, ac], [bc], [[abc]]];
#             """,
#             """[,a,,,b,,,c,,,[,ab,,,ac,],,,[,bc,],,,[,[,abc,],],],;,<EOF>""",155))
        
#     def test56(self):
#         """test float lit"""
#         self.assertTrue(TestLexer.test(
#             """ 12.0 4e7 2. 0.412E-21 128e+42 """,
#             """12.0,4e7,2.,0.412E-21,128e+42,<EOF>""",156))

#     def test57(self):
#         """test float lit"""
#         self.assertTrue(TestLexer.test(
#             """ 12.0 4e7 2.. 0.412E-21 128e+42 """,
#             """12.0,4e7,2.,.,0.412E-21,128e+42,<EOF>""",157))

#     def test58(self):
#         """test float lit"""
#         self.assertTrue(TestLexer.test(
#             """ 12.0 4e7 2.. .24 0.412E-21 128e+42 """,
#             """12.0,4e7,2.,.,.,24,0.412E-21,128e+42,<EOF>""",158))
    
#     def test59(self):
#         """test float lit"""
#         self.assertTrue(TestLexer.test(
#             """ 12.0 4e7 2.. .24 2001e 0.412E-21 128e+42 """,
#             """12.0,4e7,2.,.,.,24,2001,e,0.412E-21,128e+42,<EOF>""",159))
    
#     def test60(self):
#         """test comment"""
#         self.assertTrue(TestLexer.test(
#             """ 
#             ##
#                 This is a
#                 multi-line
#                 comment
#             ##
#             """,
#             """<EOF>""",160))
        
#     def test61(self):
#         """test BOOLEAN"""
#         self.assertTrue(TestLexer.test(
#             "True False",
#             "True,False,<EOF>",161))
        
#     def test62(self):
#         """test HEX"""
#         self.assertTrue(TestLexer.test(
#             "0x4_1_2 0x_412 0X41_2_ 0X_4_1_2 0X4__12 0X4__1__2",
#             "0x412,0,x_412,0X412,_,0,X_4_1_2,0X4,__12,0X4,__1__2,<EOF>",162))
    
#     def test63(self):
#         """test OCT"""
#         self.assertTrue(TestLexer.test(
#             "0_0 04_1_2 04__12",
#             "0,_0,0412,04,__12,<EOF>",163))
        
#     def test64(self):
#         """test BIN"""
#         self.assertTrue(TestLexer.test(
#             "0B110011100 0b0110011100 0B1_100_1_110_0_22",
#             "0B110011100,0b0,110011100,0B110011100,_22,<EOF>",164))
        
#     def test65(self):
#         """test FLOAT"""
#         self.assertTrue(TestLexer.test(
#             "412.1234e12 1_23.1234e12 1_2_3.1234e12",
#             "412.1234e12,123.1234e12,123.1234e12,<EOF>",165))
    
#     def test66(self):
#         input = """ Array("new","word") """
#         expected = """Array,(,new,,,word,),<EOF>"""
#         self.assertTrue(TestLexer.test(input, expected, 166))
    
#     def test67(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array(12,5,36,4121)""",
#             "Array,(,12,,,5,,,36,,,4121,),<EOF>",167))   
        
#     def test68(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array("Great","Power","Responsibility")""",
#             "Array,(,Great,,,Power,,,Responsibility,),<EOF>",168))     
        
#     def test69(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array(Array("Great","Power","comes"), Array("with","great","responsibility"), Array("uncle","Ben","said"))""",
#             "Array,(,Array,(,Great,,,Power,,,comes,),,,Array,(,with,,,great,,,responsibility,),,,Array,(,uncle,,,Ben,,,said,),),<EOF>",169))
        
#     def test70(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array[Int, 0B101100101]""",
#             "Array,[,Int,,,0B101100101,],<EOF>",170))
    
#     def test71(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array[Array[Float,12], 12]""",
#             "Array,[,Array,[,Float,,,12,],,,12,],<EOF>",171))
        
#     def test72(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array[Array[Array[Float,13],9], 25]""",
#             "Array,[,Array,[,Array,[,Float,,,13,],,,9,],,,25,],<EOF>",172))    
    
#     def test73(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array[Array[Array[#,15],6], 7]""",
#             "Array,[,Array,[,Array,[,Error Token #",173)) 
    
#     def test74(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array[Array[Array[&,14],7], 21]""",
#             "Array,[,Array,[,Array,[,Error Token &",174))
    
#     def test75(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array[Array[Array[@,19],45], 75]""",
#             "Array,[,Array,[,Array,[,Error Token @",175))
        
#     def test76(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Array[Array[Array[^,10],2], 10]""",
#             "Array,[,Array,[,Array,[,Error Token ^",176))
        
#     def test77(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Class Spidey {
#                 Val Tobey, Andrew, Tom = "I", "II", "III";
#             }""",
#             "Class,Spidey,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,II,,,III,;,},<EOF>",177))
        
#     def test78(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Class Spidey {
#                 Val Tobey, Andrew, Tom = "I", "II", "III;
#             }""",
#             "Class,Spidey,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,II,,,Unclosed String: III;",178)) 
        
#     def test79(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Class Peter_Parker : Spiderman {
#                 Val Tobey, Andrew, Tom = "I", "II", "III\r";
#             }""",
#             "Class,Peter_Parker,:,Spiderman,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,II,,,Unclosed String: III",179))       
    
#     def test80(self):
#         """test ARRAY_TYPE"""
#         self.assertTrue(TestLexer.test(
#             """Class Peter_Parker : Spiderman {
#                 Val Tobey, Andrew, Tom = "I", "I\nI", "III";
#             }""",
#             "Class,Peter_Parker,:,Spiderman,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,Unclosed String: I",180))
        
#     def test81(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var $universe: Int;
#                 $getUniverse() {
#                     return Self::universe;
#                 }
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},},<EOF>",181))

#     def test82(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
                
#                 ## class fields ##
#                 Var $universe: Int;
                
#                 ## class methods ##
#                 $getUniverse() {
#                     return Self::universe;
#                 }
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},},<EOF>",182))
        
#     def test83(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
                
#                 ## class fields ##
#                 Var $universe: Int;
                
#                 ## class methods ##
#                 $getUniverse() {
#                     return Self::universe;
#                 }
#                 Foreach(i In 1 .. 100 By i%2 == 0) {}
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,},},<EOF>",183))
        
#     def test84(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String;
                
#                 ## class fields ##
#                 Var $universe: Int;
                
#                 ## class methods ##
#                 $getUniverse() {
#                     return Self::universe;
#                 }
#                 Foreach(i In 1 .. 100 By i%2 == 0) {
#                     Self.suits = "red";
#                 }
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,Self,.,suits,=,red,;,},},<EOF>",184))      
    
#     def test85(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String = "Blue \\";
                
#                 ## class fields ##
#                 Var $universe: Int;
                
#                 ## class methods ##
#                 $getUniverse() {
#                     return Self::universe;
#                 }
#                 Foreach(i In 1 .. 100 By i%2 == 0) {
#                     Self.suits = "red";
#                 }
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Illegal Escape In String: Blue \\""",185))
    
#     def test86(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String = "Blue";
                
#                 ## class fields ##
#                 Var $universe: Int;
                
#                 ## class methods ##
#                 $getUniverse() {
#                     return Self::universe;
#                 }
#                 Foreach(i In 1 .. 100 By i%2 == 0) {
#                     Self.suits = "red;
#                 }
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,Self,.,suits,=,Unclosed String: red;",186))
        
        
#     def test87(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String = "Blue";
                
#                 ## class fields ##
#                 Val $ratings: Float = 8.9;
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,},<EOF>",187))
        
#     def test88(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String = "Blue";
                
#                 ## class fields ##
#                 Val $ratings: Float = 8.9;
                
#                 ## class methods ##
#                 setSuits() {
#                     if (Self.suits ==. "Blue") {
#                         Self.suits = "Red";
#                     }
#                 }
#             }""",
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,setSuits,(,),{,if,(,Self,.,suits,==.,Blue,),{,Self,.,suits,=,Red,;,},},},<EOF>""",188))  
        
        
#     def test89(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String = "Blue";
                
#                 ## class fields ##
#                 Val $ratings: Float = 8.9;
                
#                 ## class methods ##
#                 setSuits(suits: String) {
#                     if (Self.suits ==. suits) {
#                         return True;
#                     }
#                     else {
#                         return False;
#                     }
#                 }
#             }
#             """,
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,setSuits,(,suits,:,String,),{,if,(,Self,.,suits,==.,suits,),{,return,True,;,},else,{,return,False,;,},},},<EOF>""",189)) 
#     def test90(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 ## 
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String = "Blue"; 
#                 ##
                
#                 ## class fields ##
#                 ## Val $ratings: Float = 8.9; ##
                
#             }""",
#             """Class,Spider_verse,{,},<EOF>""",190))   
        
#     def test91(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: Array[String, 15];
#                 Var suits: String = "Blue";
                
#                 ## class fields ##
#                 Val $ratings: Float = 8.9;
#             }
#             class Main{
#                 main() {
#                     Var a: Spider_verse = New Spider_verse();
#                 }
#             }
#             """,
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,},class,Main,{,main,(,),{,Var,a,:,Spider_verse,=,New,Spider_verse,(,),;,},},<EOF>""",191)) 
        
#     def test92(self):
#         """test Class"""
#         self.assertTrue(TestLexer.test(
#             """Class Spider_verse {
#                 ## instance fields ##
#                 Val num: Int = 15;
#                 Var name: String;
#                 Var suits: String;
                
#                 ## class fields ##
#                 Val $ratings: Float = 8.9;
#                 Constructor(name: String; suits: String) {
#                     Self.name: String = "Peter Parker";
#                     Self.suits: String = "Red";
#                 }
#                 Destructor(){
                    
#                 }
#             }
#             """,
#             "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,String,;,Var,suits,:,String,;,Val,$ratings,:,Float,=,8.9,;,Constructor,(,name,:,String,;,suits,:,String,),{,Self,.,name,:,String,=,Peter Parker,;,Self,.,suits,:,String,=,Red,;,},Destructor,(,),{,},},<EOF>",192)) 
        
#     def test93(self):
#         """test multi_array"""
#         self.assertTrue(TestLexer.test(
#             """
#             Var multi_dimension_array: Array[Array[Array[String, 1],2],3]; 
#             """,
#             """Var,multi_dimension_array,:,Array,[,Array,[,Array,[,String,,,1,],,,2,],,,3,],;,<EOF>""",193))
        
#     def test94(self):
#         """test multi_array"""
#         self.assertTrue(TestLexer.test(
#             """
#             Array (
#                 Array("Volvo", "22", "18"),
#                 Array("Saab", "5", "2"),
#                 Array("Land Rover", "17", "15")
#             ) 
#             """,
#             "Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>",194))
        
#     def test95(self):
#         """test block"""
#         self.assertTrue(TestLexer.test(
#             """
#             {
#                 Var r, s: Int;
#                 r = 2.0;
#                 Var a, b: Array[Int, 5];
#                 s = r * r * Self.myPI;
#                 a[0] = s;
#             }
#             """,
#             "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>",195))
        
#     def test96(self):
#         """test block"""
#         self.assertTrue(TestLexer.test(
#             """
#             gcd(a: Int, b: Int) {
#                 If (b == 0) {
#                     return a;
#                 }
#                 return gcd(b, a % b);
#             }
#             """,
#             "gcd,(,a,:,Int,,,b,:,Int,),{,If,(,b,==,0,),{,return,a,;,},return,gcd,(,b,,,a,%,b,),;,},<EOF>",196))
        
#     def test96(self):
#         """test block"""
#         self.assertTrue(TestLexer.test(
#             """
#             gcd(a: Int, b: Int) {
#                 If (b == 0) {
#                     return a;
#                 }
#                 return gcd(b, a % b);
#             }
#             """,
#             "gcd,(,a,:,Int,,,b,:,Int,),{,If,(,b,==,0,),{,return,a,;,},return,gcd,(,b,,,a,%,b,),;,},<EOF>",196))
        
#     def test97(self):
#         """test block"""
#         self.assertTrue(TestLexer.test(
#             """
#             binarySearch(arr: Array[Int, 10], l: Int, r: Int, x: Int) 
#             { 
#                 If (r >= l) { 
#                     mid: Int = l + (r - l) / 2;  
#                     If (arr[mid] == x) {
#                         return mid;
#                     }
#                     If (arr[mid] > x) {
#                         return binarySearch(arr, l, mid - 1, x);
#                     }
#                     return binarySearch(arr, mid + 1, r, x); 
#                 } 
#                 return -1; 
#             } 
#             """,
#             "binarySearch,(,arr,:,Array,[,Int,,,10,],,,l,:,Int,,,r,:,Int,,,x,:,Int,),{,If,(,r,>=,l,),{,mid,:,Int,=,l,+,(,r,-,l,),/,2,;,If,(,arr,[,mid,],==,x,),{,return,mid,;,},If,(,arr,[,mid,],>,x,),{,return,binarySearch,(,arr,,,l,,,mid,-,1,,,x,),;,},return,binarySearch,(,arr,,,mid,+,1,,,r,,,x,),;,},return,-,1,;,},<EOF>",197))
        
#     def test98(self):
#         """test block"""
#         self.assertTrue(TestLexer.test(
#             """
#             factorial(n: Int)
#             {
#                 If (n == 0) {
#                     return 1;
#                 }
#                 return n * factorial(n - 1);
#             } 
#             """,
#             "factorial,(,n,:,Int,),{,If,(,n,==,0,),{,return,1,;,},return,n,*,factorial,(,n,-,1,),;,},<EOF>",198))
        
#     def test99(self):
#         """test block"""
#         self.assertTrue(TestLexer.test(
#             """
#             Fibonacci(n: Int)
#             {
#                 If (n == 1 || n == 2)
#                     return 1;
#                 return Fibonacci(n - 1) + Fibonacci(n - 2);
#             }
#             """,
#             "Fibonacci,(,n,:,Int,),{,If,(,n,==,1,||,n,==,2,),return,1,;,return,Fibonacci,(,n,-,1,),+,Fibonacci,(,n,-,2,),;,},<EOF>",199))
        
#     def test100(self):
#         """test block"""
#         self.assertTrue(TestLexer.test(
#             """
#             SumRecursion(n: Int) {
#                 ##
#                     sum = 1 + ... + n
#                 ##
#                 if (n == 0) {
#                     return 0;
#                 }
#                 return n + SumRecursion(n - 1);
#             }
#             """,
#             "SumRecursion,(,n,:,Int,),{,if,(,n,==,0,),{,return,0,;,},return,n,+,SumRecursion,(,n,-,1,),;,},<EOF>",200))

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    ######## ID ############
    def test1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc ABC aBc AbC","abc,ABC,aBc,AbC,<EOF>",101))
        
    def test2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$count $COUNT $CounT $cOUNt","$count,$COUNT,$CounT,$cOUNt,<EOF>",102))
        
    def test3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_init_ _INIT_ __init__","_init_,_INIT_,__init__,<EOF>",103))
        
    def test4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_","_,<EOF>",104))
        
    def test5(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.test("getNam@","getNam,Error Token @",105))   
        
    def test6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$D96 D96 D_96 D_96_ ____D96___","$D96,D96,D_96,D_96_,____D96___,<EOF>",106)) 
        
    def test7(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.test("$$","Error Token $",107))
        
    def test8(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.test("a a a e10 , . e10 # $e","a,a,a,e10,,,.,e10,Error Token #",108))
        
    ########### HEX ############
    def test9(self):
        """test HEX"""
        self.assertTrue(TestLexer.test("0x0 0x00 0xABCDEF 0X123456789ABCDEF","0x0,0x0,0,0xABCDEF,0X123456789ABCDEF,<EOF>",109))
        
    def test9(self):
        """test HEX"""
        self.assertTrue(TestLexer.test("0x1_2_3 0x_123 0X12_3_ 0X_1_2_3 0X1__23 0X1__2__3","0x123,0,x_123,0X123,_,0,X_1_2_3,0X1,__23,0X1,__2__3,<EOF>",109))
        
    def test10(self):
        """test HEX"""
        self.assertTrue(TestLexer.test("0x000000000 0xACZED","0x0,00,00,00,00,0xAC,ZED,<EOF>",110))
    
    def test11(self):
        """test HEX"""
        self.assertTrue(TestLexer.test("0x2_5BA_427","0x25BA427,<EOF>",111))
        
    def test12(self):
        """test HEX"""
        self.assertTrue(TestLexer.test("0X1230A","0X1230A,<EOF>",112))
        
    def test13(self):
        """test HEX"""
        self.assertTrue(TestLexer.test("0xabc","0,xabc,<EOF>",113))
       
    ########### OCT ############     
    def test14(self):
        """test OCT"""
        self.assertTrue(TestLexer.test("007","00,7,<EOF>",114))
        
    def test15(self):
        """test OCT"""
        self.assertTrue(TestLexer.test("00_7 01_2 09_3","00,_7,012,0,93,<EOF>",115))
        
    def test16(self):
        """test OCT"""
        self.assertTrue(TestLexer.test("0_0 01_2_3 01__23","0,_0,0123,01,__23,<EOF>",116))
        
    def test17(self):
        """test OCT"""
        self.assertTrue(TestLexer.test("00000000","00,00,00,00,<EOF>",117))
        
    def test18(self):
        """test OCT"""
        self.assertTrue(TestLexer.test("00_","00,_,<EOF>",118))
        
    def test19(self):
        """test OCT"""
        self.assertTrue(TestLexer.test("01_1_8__2","011,_8__2,<EOF>",119))
     
    ########### BIN ############    
    def test20(self):
        """test BIN"""
        self.assertTrue(TestLexer.test("0b0 0B0 0b00","0b0,0B0,0b0,0,<EOF>",120))
       
    def test21(self):
        """test BIN"""
        self.assertTrue(TestLexer.test("0b1001001 0b010011 0B111_111_111_22","0b1001001,0b0,10011,0B111111111,_22,<EOF>",121))
        
    def test22(self):
        """test BIN"""
        self.assertTrue(TestLexer.test("0B_111_000 0b111_ 0b11__11","0,B_111_000,0b111,_,0b11,__11,<EOF>",122))
        
    def test23(self):
        """test BIN"""
        self.assertTrue(TestLexer.test("0b0b1","0b0,b1,<EOF>",123))
        
    def test24(self):
        """test BIN"""
        self.assertTrue(TestLexer.test("0b1b1","0b1,b1,<EOF>",124))
        
    def test25(self):
        """test BIN"""
        self.assertTrue(TestLexer.test("0B1_1_0_0","0B1100,<EOF>",125))
    
    ########### DECIMAL ############    
    def test26(self):
        """test DECIMAL"""
        self.assertTrue(TestLexer.test("123456789 ","123456789,<EOF>",126))
        
    def test27(self):
        """test DECIMAL"""
        self.assertTrue(TestLexer.test("1_2_3_4_5_6_7_8_9","123456789,<EOF>",127))
        
    def test28(self):
        """test DECIMAL"""
        self.assertTrue(TestLexer.test("0 000 12000000 9990000","0,00,0,12000000,9990000,<EOF>",128))
        
    def test29(self):
        """test DECIMAL"""
        self.assertTrue(TestLexer.test("1_2_3_","123,_,<EOF>",129))
        
    def test30(self):
        """test DECIMAL"""
        self.assertTrue(TestLexer.test("_12_3_","_12_3_,<EOF>",130))
        
    def test31(self):
        """test DECIMAL"""
        self.assertTrue(TestLexer.test("12390011234_2222","123900112342222,<EOF>",131))
        
    ########### FLOAT ############    
    def test32(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("1.1234e1 0.1234e0","1.1234e1,0.1234e0,<EOF>",132))
        
    def test33(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("123.1234e12 1_23.1234e12 1_2_3.1234e12","123.1234e12,123.1234e12,123.1234e12,<EOF>",133))
        
    def test34(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("123.1234_5e12 123.1_2_3_4e12 123.1_2_3_4e1_2","123.1234,_5e12,123.1,_2_3_4e12,123.1,_2_3_4e1_2,<EOF>",134))
        
    def test35(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("00.123 10.123 10.00000000000 10.000000001 0.0000000000","00,.,123,10.123,10.00000000000,10.000000001,0.0000000000,<EOF>",135))
        
    def test36(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("0. 1. 2. 10. 99.","0.,1.,2.,10.,99.,<EOF>",136))
        
    def test37(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("1e2 1e0 12e12 12e000001","1e2,1e0,12e12,12e000001,<EOF>",137))
        
    def test38(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(".12e10 .00000e0 .4000004e006",".12e10,.00000e0,.4000004e006,<EOF>",138))
        
    def test39(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(".4 .3",".,4,.,3,<EOF>",139))
    
    ########### BOOLEAN ############    
    def test40(self):
        """test BOOLEAN"""
        self.assertTrue(TestLexer.test("True False","True,False,<EOF>",140))
    
    ########### STRING ############     
    def test41(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "abc" ""","abc,<EOF>",141))
        
    def test42(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "Xin chao cac ban '" ""","""Unclosed String: Xin chao cac ban '" """,142))
        
    def test43(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "Xin chao cac ban '"" ""","""Xin chao cac ban '",<EOF>""",143))
        
    def test44(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "Xin chao cac ban '"cac ban khoe khong?'" " ""","""Xin chao cac ban '"cac ban khoe khong?'" ,<EOF>""",144))
        
    def test45(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "PPL\\b-HCMUTK19" ""","""PPL\\b-HCMUTK19,<EOF>""",145))
        
    def test46(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "PPL\\t-HCMUTK19" ""","""PPL\\t-HCMUTK19,<EOF>""",146))
        
    def test47(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "PPL\\\\-HCMUTK19" ""","""PPL\\\\-HCMUTK19,<EOF>""",147))
        
    def test48(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "PPL\'-HCMUTK19" ""","""PPL\'-HCMUTK19,<EOF>""",148))
        
    def test49(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "PPL\n-HCMUTK19" ""","""Unclosed String: PPL""",149))
        
    def test50(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "PPL\r-HCMUTK19" ""","""Unclosed String: PPL""",150))
    
    def test51(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "PPL\f-HCMUTK19" ""","""Unclosed String: PPL""",151))
        
    def test52(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "aa\\h" ""","""Illegal Escape In String: aa\\h""",152))
        
    def test53(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "aa\\\h" ""","""aa\\\h,<EOF>""",153))
        
    def test54(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "aa\z" ""","""Illegal Escape In String: aa\z""",154))    
    
    def test55(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "aa\t ""","""Illegal Escape In String: aa\t""",155))    
    
    def test56(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "" """,""",<EOF>""",156))
        
    def test57(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "abc\\\\ ""","""Unclosed String: abc\\\\ """,157))
        
    def test58(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "abc\\n ""","""Unclosed String: abc\\n """,158))    
        
    def test59(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "abc\\r ""","""Unclosed String: abc\\r """,159))
        
    def test60(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(""" "abc\f" ""","""Unclosed String: abc""",160))     
        
    ########### KEYWORD ###########   
    def test61(self):
        """test KEYWORD"""
        self.assertTrue(TestLexer.test(
            "Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New By Self Then",
            "Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,By,Self,Then,<EOF>",161)) 
        
    ########### VAR VAL #########
    def test62(self):
        """test VAR"""
        self.assertTrue(TestLexer.test(
            "Var her_phone: Int= 0B110_001_000_010_001_000_100_110_100_111",
            "Var,her_phone,:,Int,=,0B110001000010001000100110100111,<EOF>",162))
        
    def test63(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val her_bf: String= "Jeff" """,
            "Val,her_bf,:,String,=,Jeff,<EOF>",163)) 
        
    def test64(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val her_pet: Array[Int,10]""",
            "Val,her_pet,:,Array,[,Int,,,10,],<EOF>",164))     
        
    def test65(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val her_dad: String= " """,
            "Val,her_dad,:,String,=,Unclosed String:  ",165))  
        
    def test66(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val isMale: Boolean= True """,
            "Val,isMale,:,Boolean,=,True,<EOF>",166)) 
    
    ######## ARRAY TYPE ############   
    def test67(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array(1,2,3,4)""",
            "Array,(,1,,,2,,,3,,,4,),<EOF>",167))   
        
    def test68(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array("PPL","HCMUT","K19")""",
            "Array,(,PPL,,,HCMUT,,,K19,),<EOF>",168))     
        
    def test69(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array(Array("PPL","HCMUT","K19"), Array("PPL","HCMUT","K19"), Array("PPL","HCMUT","K19"))""",
            "Array,(,Array,(,PPL,,,HCMUT,,,K19,),,,Array,(,PPL,,,HCMUT,,,K19,),,,Array,(,PPL,,,HCMUT,,,K19,),),<EOF>",169))
        
    def test70(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Int, 0x2]""",
            "Array,[,Int,,,0x2,],<EOF>",170))
    
    def test71(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Float,10], 10]""",
            "Array,[,Array,[,Float,,,10,],,,10,],<EOF>",171))
        
    def test72(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[Float,10],2], 10]""",
            "Array,[,Array,[,Array,[,Float,,,10,],,,2,],,,10,],<EOF>",172))    
    
    ######## ERROR TOKEN ############
    def test73(self):
        """test ERROR_TOKEN"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[@,10],2], 10]""",
            "Array,[,Array,[,Array,[,Error Token @",173)) 
    
    def test74(self):
        """test ERROR_TOKEN"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[~,10],2], 10]""",
            "Array,[,Array,[,Array,[,Error Token ~",174))
    
    def test75(self):
        """test ERROR_TOKEN"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[?,10],2], 10]""",
            "Array,[,Array,[,Array,[,Error Token ?",175))
        
    def test76(self):
        """test ERROR_TOKEN"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[&,10],2], 10]""",
            "Array,[,Array,[,Array,[,Error Token &",176))
        
    ######## UNCLOSE STRING ############
    def test77(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(
            """Class CSE{
                    Val K18, K19= "Hello", "Good ;
            }""",
            "Class,CSE,{,Val,K18,,,K19,=,Hello,,,Unclosed String: Good ;",177))
        
    def test78(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(
            """Class CSE{
                    Val K18, K19= "Hello", "Good\\\\ ;
            }""",
            "Class,CSE,{,Val,K18,,,K19,=,Hello,,,Unclosed String: Good\\\\ ;",178)) 
        
    def test79(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(
            """Class CSE : DT{
                    Val K18, K19= "Hello", "Good\n" ;
            }""",
            "Class,CSE,:,DT,{,Val,K18,,,K19,=,Hello,,,Unclosed String: Good",179))       
    
    def test80(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(
            """Class CSE : DT{
                    Val K18, K19= "Hello", "Go\rod" ;
            }""",
            "Class,CSE,:,DT,{,Val,K18,,,K19,=,Hello,,,Unclosed String: Go",180))
        
    ######### other testcase ############ 
    def test81(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class PPL {
                    Val sv: Int = 100;
                    Var $total_lost: Int;
                    $getSVlost(){
                        return Self::total_lost;
                    }
            }""",
            "Class,PPL,{,Val,sv,:,Int,=,100,;,Var,$total_lost,:,Int,;,$getSVlost,(,),{,return,Self,::,total_lost,;,},},<EOF>",181))

    def test81(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class PPL {
                    ## Xin chao cac ban :3 cac ban dung de y toi minh ##
                    Val sv: Int = 100;
            }""",
            "Class,PPL,{,Val,sv,:,Int,=,100,;,},<EOF>",181))
        
    def test82(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class PPL {
                    ## Xin chao cac ban :3 cac ban dung de y toi minh ##
                    Val sv: Int = 100;
                    Foreach(i In 1 .. 100 By i%2 == 0){
                        self.sv;
                    }
            }""",
            "Class,PPL,{,Val,sv,:,Int,=,100,;,Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,self,.,sv,;,},},<EOF>",182)) 
        
    def test83(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class PPL {
                    ## Xin chao cac ban @ ~~~~ @ cac ban dung de y toi minh ##
                    Val sv: Int = 100;
                    Foreach(i In 1 .. 100 By i%2 == 0){
                        self.sv;
                    }
            }""",
            "Class,PPL,{,Val,sv,:,Int,=,100,;,Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,self,.,sv,;,},},<EOF>",183))  
        
    def test84(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class PPL {
                    ## Xin chao cac ban @ ~~~~ @ cac ban dung de y toi minh ##
                    Val sv: Int = 100;
                    Foreach(i In 1 .. 100 By i%2 == 0){
                        self.sv;
                    }
            }""",
            "Class,PPL,{,Val,sv,:,Int,=,100,;,Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,self,.,sv,;,},},<EOF>",184))      
    
    def test85(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class PPL {
                    ## Xin chao cac ban @ ~~~~ @ cac ban dung de y toi minh ##
                    Val sv: String = "Kzatsa \\";
                    Foreach(i In 1 .. 100 By i%2 == 0){
                        self.sv;
                    }
            }""",
            """Class,PPL,{,Val,sv,:,String,=,Illegal Escape In String: Kzatsa \\""",185))
    
    def test86(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class VanTho {
                    ## Xin chao cac ban @ ~~~~ @ cac ban dung de y toi minh ##
                    Val cau1: String = "Nhung dua tre roi cung di xa nha \\;
                    Foreach(i In 1 .. 100 By i%2 == 0){
                        self.cau1;
                    }
            }""",
            """Class,VanTho,{,Val,cau1,:,String,=,Unclosed String: Nhung dua tre roi cung di xa nha \;""",186))
        
        
    def test87(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class A {
                    ## Xin chao cac ban @ ~~~~ @ cac ban dung de y toi minh ##
                    Var a: Int= 1;
                    Var $b: Float= 0.0000;
                    Var k: String= "";
            }""",
            """Class,A,{,Var,a,:,Int,=,1,;,Var,$b,:,Float,=,0.0000,;,Var,k,:,String,=,,;,},<EOF>""",187))
        
    def test88(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class A {
                    ## Xin chao cac ban @ ~~~~ @ Minh la PPL ##
                    Val str1: String = "PPL-K19:";
                    Var arr1: Array[Float, 12];
                    $vantho1(){
                        if(str1 ==. "PPL-K19:"){
                            self.arr1[1]= 0.0002;
                        }
                    }
            }""",
            """Class,A,{,Val,str1,:,String,=,PPL-K19:,;,Var,arr1,:,Array,[,Float,,,12,],;,$vantho1,(,),{,if,(,str1,==.,PPL-K19:,),{,self,.,arr1,[,1,],=,0.0002,;,},},},<EOF>""",188))  
        
        
    def test89(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class A {
                    ## Xin chao cac ban @ ~~~~ @ Minh la PPL ##
                    Val str1: String = "PPL-K19:";
                    Var arr1: Array[Float, 12];
                    $vantho1(){
                        if(str1 ==. "PPL-K19:"){
                            self.arr1[1]= 0.0002;
                        }
                    }
                }
                Class B{
                    Var $ID: String= "Hieu";
                    Var $static_ID: String= "1913341";
                    Val slogan: String= "PPL for ever";
                    isMyID(self: String){
                        if(Self::$ID == self){
                            return True;
                        }
                        else{
                            return False;
                        }
                    }
                }
            """,
            """Class,A,{,Val,str1,:,String,=,PPL-K19:,;,Var,arr1,:,Array,[,Float,,,12,],;,$vantho1,(,),{,if,(,str1,==.,PPL-K19:,),{,self,.,arr1,[,1,],=,0.0002,;,},},},Class,B,{,Var,$ID,:,String,=,Hieu,;,Var,$static_ID,:,String,=,1913341,;,Val,slogan,:,String,=,PPL for ever,;,isMyID,(,self,:,String,),{,if,(,Self,::,$ID,==,self,),{,return,True,;,},else,{,return,False,;,},},},<EOF>""",189)) 
        
    def test90(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """Class A {
                    ## Xin chao cac ban @ ~~~~ @ cac ban dung de y toi minh ##
                    ## Var a: Int= 1; ##
                    ## Var $b: Float= 0.0000; ##
                    ## Var k: String= ""; ##
            }""",
            """Class,A,{,},<EOF>""",190))   
        
    def test91(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """ Class A {
                    ## Xin chao cac ban @ ~~~~ @ cac ban dung de y toi minh ##
                    ## Var a: Int= 1; ##
                    ## Var $b: Float= 0.0000; ##
                    ## Var k: String= ""; ##
                class Program{
                    main(){
                        Var a: A= New A();
                    }
                }
            }""",
            """Class,A,{,class,Program,{,main,(,),{,Var,a,:,A,=,New,A,(,),;,},},},<EOF>""",191)) 
        
    def test92(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """ Class Shape{
                    Var $shapes: Int=0;
                }
                Class Square: Shape{
                    Var type: String= "square";
                    Var cd, cr: Int;
                    Constructor(cd: Int; cr: Int){
                        Self.cd: Int=10;
                        Self.cr: Int=15;
                    }
                    Destructor(){
                        
                    }
                }
            """,
            """Class,Shape,{,Var,$shapes,:,Int,=,0,;,},Class,Square,:,Shape,{,Var,type,:,String,=,square,;,Var,cd,,,cr,:,Int,;,Constructor,(,cd,:,Int,;,cr,:,Int,),{,Self,.,cd,:,Int,=,10,;,Self,.,cr,:,Int,=,15,;,},Destructor,(,),{,},},<EOF>""",192)) 
        
    def test93(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var multi_arr: Array[Array[Array[String. 2],3],4]; 
            """,
            """Var,multi_arr,:,Array,[,Array,[,Array,[,String,.,2,],,,3,],,,4,],;,<EOF>""",193))
        
    def test94(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var error_str: String= "hello world\\"; 
            """,
            """Var,error_str,:,String,=,Illegal Escape In String: hello world\\""",194))
        
    def test95(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var error_str: String= "hello world\\ 
            """,
            """Var,error_str,:,String,=,Unclosed String: hello world\\ """,195))
        
    def test96(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var error_str: String= "hello world\t \k ahihi" 
            """,
            """Var,error_str,:,String,=,Illegal Escape In String: hello world\t""",196))
        
    def test97(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var error_str: String= "hello world ahihi";
            Val $ID: Float= 19_5.111~15; 
            """,
            """Var,error_str,:,String,=,hello world ahihi,;,Val,$ID,:,Float,=,195.111,Error Token ~""",197))
        
    def test98(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var _str1, _str2: String= "","";
            """,
            """Var,_str1,,,_str2,:,String,=,,,,,;,<EOF>""",198))
        
    def test99(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var _str1, _str2: String= "",";
            """,
            """Var,_str1,,,_str2,:,String,=,,,,Unclosed String: ;""",199))
        
    def test100(self):
        """test OTHER_CASE"""
        self.assertTrue(TestLexer.test(
            """
            Var _str1, _str2: String= "'" ";
            """,
            """Var,_str1,,,_str2,:,String,=,'" ,;,<EOF>""",200))