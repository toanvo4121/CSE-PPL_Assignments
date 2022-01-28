import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test1(self):
        """test KEYWORD"""
        self.assertTrue(TestLexer.test(
            "Val Var Int Float Boolean String Array If Elseif Else True False Foreach In By Break Continue Return Null Class Constructor Destructor New Self",
            "Val,Var,Int,Float,Boolean,String,Array,If,Elseif,Else,True,False,Foreach,In,By,Break,Continue,Return,Null,Class,Constructor,Destructor,New,Self,<EOF>",101))
        
    def test2(self):
        """test Comment"""
        self.assertTrue(TestLexer.test(
            "abc ##This is the comment so \n it shouldn't be compiled## xyz",
            "abc,xyz,<EOF>",102)) 
    
    def test3(self):
        """test Comment"""
        self.assertTrue(TestLexer.test(
            "abc ## Comments is non-greedy so this case it will cause ## error ## xyz",
            "abc,error,Error Token #",103))
    
    def test4(self):
        """test Comment"""
        self.assertTrue(TestLexer.test(
            """ "This is a string so compiler will not skip this part. ## See, it still appears in your string ## uWu" """,
            "This is a string so compiler will not skip this part. ## See, it still appears in your string ## uWu,<EOF>",104))

    def test5(self):
        """test Identifiers"""
        self.assertTrue(TestLexer.test(
            "UwU uWu uWU ____D96___ P_P_L _ _MrDuy__ kHalAChaCKeO",
            "UwU,uWu,uWU,____D96___,P_P_L,_,_MrDuy__,kHalAChaCKeO,<EOF>",105)) 
        
    def test6(self):
        """test Identifiers"""
        self.assertTrue(TestLexer.test(
            "Email toanvo4121@hcmut",
            "Email,toanvo4121,Error Token @",106))
        
    def test7(self):
        """test Static Identifiers"""
        self.assertTrue(TestLexer.test(
            "$xoxo $0 $asap $Lambda $_MrDuy__",
            "$xoxo,$0,$asap,$Lambda,$_MrDuy__,<EOF>",107))
        
    def test8(self):
        """test Static Identifiers"""
        self.assertTrue(TestLexer.test(
            "$$",
            "Error Token $",108))
        
    def test9(self):
        """test INTLIT"""
        self.assertTrue(TestLexer.test(
            "00 0 0x0 0X0 0b0 0B0",
            "00,0,0x0,0X0,0b0,0B0,<EOF>",109))
        
    def test10(self):
        """test INTLIT"""
        self.assertTrue(TestLexer.test(
            "0562_1315_02_464 3122_2_3_215_481_325 0xA_05BC_DE_F_4812 0B1_1_0_0_0101101_101011",
            "0562131502464,312223215481325,0xA05BCDEF4812,0B11000101101101011,<EOF>",110))
        
    def test11(self):
        """test INTLIT"""
        self.assertTrue(TestLexer.test(
            "000x0000000 0xABCDEFTOANVO",
            "00,0x0,00,00,00,0xABCDEF,TOANVO,<EOF>",111))
    
    def test12(self):
        """test INTLIT"""
        self.assertTrue(TestLexer.test(
            "0x41_FA_1D_2CB_1E5 00000000 012_123_56_7_987",
            "0x41FA1D2CB1E5,00,00,00,00,012123567,_987,<EOF>",112))
        
    def test13(self):
        """test INTLIT"""
        self.assertTrue(TestLexer.test(
            "0X1230A 0B10_0_101_10",
            "0X1230A,0B10010110,<EOF>",113))
    
    def test14(self):
        """test INTLIT"""
        self.assertTrue(TestLexer.test(
            "00001_0150_1501_522_ABC_1121 0_x15a5_BaE1_20CdF_ 145_15_1_16_",
            "00,00,101501501522,_ABC_1121,0,_x15a5_BaE1_20CdF_,14515116,_,<EOF>",114))
        
    def test15(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            "5.5146e1 0.2694e15",
            "5.5146e1,0.2694e15,<EOF>",115))
        
    def test16(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            "123.34546e12 1_31_513.0405e12 1_2_3.00534e12",
            "123.34546e12,131513.0405e12,123.00534e12,<EOF>",116))
        
    def test17(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            "12_3.12_34_5e12 123.1_3_7_5e73 2683.1234e1_2",
            "123.12,_34_5e12,123.1,_3_7_5e73,2683.1234e1,_2,<EOF>",117))
        
    def test18(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            "00.792 32.567 21.00000000000 17.000000001 0.000000e0000000000",
            "00,.,792,32.567,21.00000000000,17.000000001,0.000000e0000000000,<EOF>",118))
        
    def test19(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            "0. 1. 2. 10. 99.",
            "0.,1.,2.,10.,99.,<EOF>",119))
        
    def test20(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            "1e2 1e0 12e12 12e000001",
            "1e2,1e0,12e12,12e000001,<EOF>",120))
        
    def test21(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            ".12e10 .00000e0 .4000004e006",
            ".12e10,.00000e0,.4000004e006,<EOF>",121))
        
    def test22(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            ".4 .3",
            ".,4,.,3,<EOF>",122))
        
    def test23(self):
        """test VAR"""
        self.assertTrue(TestLexer.test(
            "Var phoneNumber: Int = 0399_575_679",
            "Var,phoneNumber,:,Int,=,03,99575679,<EOF>",123))
        
    def test24(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val email: String = "toan.vo4121@hcmut.edu.vn" """,
            "Val,email,:,String,=,toan.vo4121@hcmut.edu.vn,<EOF>",124)) 
        
    def test25(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val skills: Array[String,15]""",
            "Val,skills,:,Array,[,String,,,15,],<EOF>",125))     
        
    def test26(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val rel_status: String= " """,
            "Val,rel_status,:,String,=,Unclosed String:  ",126))  
        
    def test27(self):
        """test VAL"""
        self.assertTrue(TestLexer.test(
            """Val isGay: Boolean= False """,
            "Val,isGay,:,Boolean,=,False,<EOF>",127))
        
    def test28(self):
        """test VAR"""
        self.assertTrue(TestLexer.test(
            """Var name: String = "Vo Minh Toan" """,
            "Var,name,:,String,=,Vo Minh Toan,<EOF>",128))
    def test29(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "CO3005 HCMUT-K19 \n - BKHCM" """,
            """Unclosed String: CO3005 HCMUT-K19 """,129))
    
    def test30(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "abc xyz" """,
            "abc xyz,<EOF>",130))
        
    def test31(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Hello '" cac ban khoe khong?" """,
            """Hello '" cac ban khoe khong?,<EOF>""",131))
        
    def test32(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Dieu anh luon giu kin trong tim '" """,
            """Unclosed String: Dieu anh luon giu kin trong tim '" """,132))
        
    def test33(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Hat mua roi bua '"vay trai ' tim hiu quanh '" " """,
            """Hat mua roi bua '"vay trai ' tim hiu quanh '" ,<EOF>""",133))
        
    def test34(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\bcomes great responsibility" """,
            """Great power\bcomes great responsibility,<EOF>""",134))
        
    def test35(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\tcomes great responsibility" """,
            """Great power\tcomes great responsibility,<EOF>""",135))
        
    def test36(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\\\\comes great responsibility" """,
            """Great power\\\\comes great responsibility,<EOF>""",136))
        
    def test37(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\'comes great responsibility" """,
            """Great power\'comes great responsibility,<EOF>""",137))
        
    def test38(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "CO3005 HCMUT-K19 \r - BKHCM" """,
            """Unclosed String: CO3005 HCMUT-K19 """,138))
        
    def test39(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "CO3005 HCMUT-K19 \f - BKHCM" """,
            """Unclosed String: CO3005 HCMUT-K19 """,139))
    
    def test40(self):
        """test VAR"""
        self.assertTrue(TestLexer.test(
            """Var nationality: String = "Vietnam" """,
            "Var,nationality,:,String,=,Vietnam,<EOF>",140))
        
    def test41(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\hcomes great responsibility" """,
            """Illegal Escape In String: Great power\h""",141))
        
    def test42(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\\\hcomes great responsibility" """,
            """Great power\\\hcomes great responsibility,<EOF>""",142))
        
    def test43(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\jcomes great responsibility" """,
            """Illegal Escape In String: Great power\j""",143))    
    
    def test44(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power comes great responsibility """,
            """Unclosed String: Great power comes great responsibility """,144))    
    
    def test45(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "" """,
            """,<EOF>""",145))
        
    def test46(self):
        """test STRING"""
        self.assertTrue(TestLexer.test(
            """ "Great power\\\\ """,
            """Unclosed String: Great power\\\\ """,146))
        
    def test47(self):
        """test String var"""
        self.assertTrue(TestLexer.test(
            """
            Var greetings: String = "hi there\\"; 
            """,
            """Var,greetings,:,String,=,Illegal Escape In String: hi there\\""",147))
        
    def test48(self):
        """test String var"""
        self.assertTrue(TestLexer.test(
            """
            Var greetings: String = "hi there\\ 
            """,
            """Var,greetings,:,String,=,Unclosed String: hi there\\ """,148))
        
    def test49(self):
        """test String var"""
        self.assertTrue(TestLexer.test(
            """
            Var greetings: String = "hi there\t \y test" 
            """,
            """Var,greetings,:,String,=,Illegal Escape In String: hi there	 \y""",149))
        
    def test50(self):
        """test String var"""
        self.assertTrue(TestLexer.test(
            """
            Var greetings: String = "hi there\t test";
            Val $test: Float = 4_12.2001#15; 
            """,
            """Var,greetings,:,String,=,hi there	 test,;,Val,$test,:,Float,=,412.2001,Error Token #""",150))
        
    def test51(self):
        """test String var"""
        self.assertTrue(TestLexer.test(
            """
            Var _str1, _str2: String= "","";
            """,
            """Var,_str1,,,_str2,:,String,=,,,,,;,<EOF>""",151))
        
    def test52(self):
        """test String var"""
        self.assertTrue(TestLexer.test(
            """
            Var _str1, _str2: String= "",";
            """,
            """Var,_str1,,,_str2,:,String,=,,,,Unclosed String: ;""",152))
        
    def test53(self):
        """test String var"""
        self.assertTrue(TestLexer.test(
            """
            Var _str1, _str2: String= "'" ";
            """,
            """Var,_str1,,,_str2,:,String,=,'" ,;,<EOF>""",153))
        
    def test54(self):
        """test something"""
        self.assertTrue(TestLexer.test(
            """
            [12, 24, 36, 48, 60, 72, 84, 96];
            """,
            """[,12,,,24,,,36,,,48,,,60,,,72,,,84,,,96,],;,<EOF>""",154))
        
    def test55(self):
        """test something"""
        self.assertTrue(TestLexer.test(
            """
            [a, b, c, [ab, ac], [bc], [[abc]]];
            """,
            """[,a,,,b,,,c,,,[,ab,,,ac,],,,[,bc,],,,[,[,abc,],],],;,<EOF>""",155))
        
    def test56(self):
        """test float lit"""
        self.assertTrue(TestLexer.test(
            """ 12.0 4e7 2. 0.412E-21 128e+42 """,
            """12.0,4e7,2.,0.412E-21,128e+42,<EOF>""",156))

    def test57(self):
        """test float lit"""
        self.assertTrue(TestLexer.test(
            """ 12.0 4e7 2.. 0.412E-21 128e+42 """,
            """12.0,4e7,2.,.,0.412E-21,128e+42,<EOF>""",157))

    def test58(self):
        """test float lit"""
        self.assertTrue(TestLexer.test(
            """ 12.0 4e7 2.. .24 0.412E-21 128e+42 """,
            """12.0,4e7,2.,.,.,24,0.412E-21,128e+42,<EOF>""",158))
    
    def test59(self):
        """test float lit"""
        self.assertTrue(TestLexer.test(
            """ 12.0 4e7 2.. .24 2001e 0.412E-21 128e+42 """,
            """12.0,4e7,2.,.,.,24,2001,e,0.412E-21,128e+42,<EOF>""",159))
    
    def test60(self):
        """test comment"""
        self.assertTrue(TestLexer.test(
            """ 
            ##
                This is a
                multi-line
                comment
            ##
            """,
            """<EOF>""",160))
        
    def test61(self):
        """test BOOLEAN"""
        self.assertTrue(TestLexer.test(
            "True False",
            "True,False,<EOF>",161))
        
    def test62(self):
        """test HEX"""
        self.assertTrue(TestLexer.test(
            "0x4_1_2 0x_412 0X41_2_ 0X_4_1_2 0X4__12 0X4__1__2",
            "0x412,0,x_412,0X412,_,0,X_4_1_2,0X4,__12,0X4,__1__2,<EOF>",162))
    
    def test63(self):
        """test OCT"""
        self.assertTrue(TestLexer.test(
            "0_0 04_1_2 04__12",
            "0,_0,0412,04,__12,<EOF>",163))
        
    def test64(self):
        """test BIN"""
        self.assertTrue(TestLexer.test(
            "0B110011100 0b0110011100 0B1_100_1_110_0_22",
            "0B110011100,0b0,110011100,0B110011100,_22,<EOF>",164))
        
    def test65(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(
            "412.1234e12 1_23.1234e12 1_2_3.1234e12",
            "412.1234e12,123.1234e12,123.1234e12,<EOF>",165))
    
    def test66(self):
        input = """ Array("new","word") """
        expected = """Array,(,new,,,word,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expected, 166))
    
    def test67(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array(12,5,36,4121)""",
            "Array,(,12,,,5,,,36,,,4121,),<EOF>",167))   
        
    def test68(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array("Great","Power","Responsibility")""",
            "Array,(,Great,,,Power,,,Responsibility,),<EOF>",168))     
        
    def test69(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array(Array("Great","Power","comes"), Array("with","great","responsibility"), Array("uncle","Ben","said"))""",
            "Array,(,Array,(,Great,,,Power,,,comes,),,,Array,(,with,,,great,,,responsibility,),,,Array,(,uncle,,,Ben,,,said,),),<EOF>",169))
        
    def test70(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Int, 0B101100101]""",
            "Array,[,Int,,,0B101100101,],<EOF>",170))
    
    def test71(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Float,12], 12]""",
            "Array,[,Array,[,Float,,,12,],,,12,],<EOF>",171))
        
    def test72(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[Float,13],9], 25]""",
            "Array,[,Array,[,Array,[,Float,,,13,],,,9,],,,25,],<EOF>",172))    
    
    def test73(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[#,15],6], 7]""",
            "Array,[,Array,[,Array,[,Error Token #",173)) 
    
    def test74(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[&,14],7], 21]""",
            "Array,[,Array,[,Array,[,Error Token &",174))
    
    def test75(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[@,19],45], 75]""",
            "Array,[,Array,[,Array,[,Error Token @",175))
        
    def test76(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Array[Array[Array[^,10],2], 10]""",
            "Array,[,Array,[,Array,[,Error Token ^",176))
        
    def test77(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Class Spidey {
                Val Tobey, Andrew, Tom = "I", "II", "III";
            }""",
            "Class,Spidey,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,II,,,III,;,},<EOF>",177))
        
    def test78(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Class Spidey {
                Val Tobey, Andrew, Tom = "I", "II", "III;
            }""",
            "Class,Spidey,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,II,,,Unclosed String: III;",178)) 
        
    def test79(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Class Peter_Parker : Spiderman {
                Val Tobey, Andrew, Tom = "I", "II", "III\r";
            }""",
            "Class,Peter_Parker,:,Spiderman,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,II,,,Unclosed String: III",179))       
    
    def test80(self):
        """test ARRAY_TYPE"""
        self.assertTrue(TestLexer.test(
            """Class Peter_Parker : Spiderman {
                Val Tobey, Andrew, Tom = "I", "I\nI", "III";
            }""",
            "Class,Peter_Parker,:,Spiderman,{,Val,Tobey,,,Andrew,,,Tom,=,I,,,Unclosed String: I",180))
        
    def test81(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var $universe: Int;
                $getUniverse() {
                    return Self::universe;
                }
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},},<EOF>",181))

    def test82(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                
                ## class fields ##
                Var $universe: Int;
                
                ## class methods ##
                $getUniverse() {
                    return Self::universe;
                }
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},},<EOF>",182))
        
    def test83(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                
                ## class fields ##
                Var $universe: Int;
                
                ## class methods ##
                $getUniverse() {
                    return Self::universe;
                }
                Foreach(i In 1 .. 100 By i%2 == 0) {}
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,},},<EOF>",183))
        
    def test84(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String;
                
                ## class fields ##
                Var $universe: Int;
                
                ## class methods ##
                $getUniverse() {
                    return Self::universe;
                }
                Foreach(i In 1 .. 100 By i%2 == 0) {
                    Self.suits = "red";
                }
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,Self,.,suits,=,red,;,},},<EOF>",184))      
    
    def test85(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String = "Blue \\";
                
                ## class fields ##
                Var $universe: Int;
                
                ## class methods ##
                $getUniverse() {
                    return Self::universe;
                }
                Foreach(i In 1 .. 100 By i%2 == 0) {
                    Self.suits = "red";
                }
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Illegal Escape In String: Blue \\""",185))
    
    def test86(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String = "Blue";
                
                ## class fields ##
                Var $universe: Int;
                
                ## class methods ##
                $getUniverse() {
                    return Self::universe;
                }
                Foreach(i In 1 .. 100 By i%2 == 0) {
                    Self.suits = "red;
                }
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Var,$universe,:,Int,;,$getUniverse,(,),{,return,Self,::,universe,;,},Foreach,(,i,In,1,..,100,By,i,%,2,==,0,),{,Self,.,suits,=,Unclosed String: red;",186))
        
        
    def test87(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String = "Blue";
                
                ## class fields ##
                Val $ratings: Float = 8.9;
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,},<EOF>",187))
        
    def test88(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String = "Blue";
                
                ## class fields ##
                Val $ratings: Float = 8.9;
                
                ## class methods ##
                setSuits() {
                    if (Self.suits ==. "Blue") {
                        Self.suits = "Red";
                    }
                }
            }""",
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,setSuits,(,),{,if,(,Self,.,suits,==.,Blue,),{,Self,.,suits,=,Red,;,},},},<EOF>""",188))  
        
        
    def test89(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String = "Blue";
                
                ## class fields ##
                Val $ratings: Float = 8.9;
                
                ## class methods ##
                setSuits(suits: String) {
                    if (Self.suits ==. suits) {
                        return True;
                    }
                    else {
                        return False;
                    }
                }
            }
            """,
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,setSuits,(,suits,:,String,),{,if,(,Self,.,suits,==.,suits,),{,return,True,;,},else,{,return,False,;,},},},<EOF>""",189)) 
    def test90(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                ## 
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String = "Blue"; 
                ##
                
                ## class fields ##
                ## Val $ratings: Float = 8.9; ##
                
            }""",
            """Class,Spider_verse,{,},<EOF>""",190))   
        
    def test91(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: Array[String, 15];
                Var suits: String = "Blue";
                
                ## class fields ##
                Val $ratings: Float = 8.9;
            }
            class Main{
                main() {
                    Var a: Spider_verse = New Spider_verse();
                }
            }
            """,
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,Array,[,String,,,15,],;,Var,suits,:,String,=,Blue,;,Val,$ratings,:,Float,=,8.9,;,},class,Main,{,main,(,),{,Var,a,:,Spider_verse,=,New,Spider_verse,(,),;,},},<EOF>""",191)) 
        
    def test92(self):
        """test Class"""
        self.assertTrue(TestLexer.test(
            """Class Spider_verse {
                ## instance fields ##
                Val num: Int = 15;
                Var name: String;
                Var suits: String;
                
                ## class fields ##
                Val $ratings: Float = 8.9;
                Constructor(name: String; suits: String) {
                    Self.name: String = "Peter Parker";
                    Self.suits: String = "Red";
                }
                Destructor(){
                    
                }
            }
            """,
            "Class,Spider_verse,{,Val,num,:,Int,=,15,;,Var,name,:,String,;,Var,suits,:,String,;,Val,$ratings,:,Float,=,8.9,;,Constructor,(,name,:,String,;,suits,:,String,),{,Self,.,name,:,String,=,Peter Parker,;,Self,.,suits,:,String,=,Red,;,},Destructor,(,),{,},},<EOF>",192)) 
        
    def test93(self):
        """test multi_array"""
        self.assertTrue(TestLexer.test(
            """
            Var multi_dimension_array: Array[Array[Array[String, 1],2],3]; 
            """,
            """Var,multi_dimension_array,:,Array,[,Array,[,Array,[,String,,,1,],,,2,],,,3,],;,<EOF>""",193))
        
    def test94(self):
        """test multi_array"""
        self.assertTrue(TestLexer.test(
            """
            Array (
                Array("Volvo", "22", "18"),
                Array("Saab", "5", "2"),
                Array("Land Rover", "17", "15")
            ) 
            """,
            "Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>",194))
        
    def test95(self):
        """test block"""
        self.assertTrue(TestLexer.test(
            """
            {
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
            """,
            "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>",195))
        
    def test96(self):
        """test block"""
        self.assertTrue(TestLexer.test(
            """
            gcd(a: Int, b: Int) {
                If (b == 0) {
                    return a;
                }
                return gcd(b, a % b);
            }
            """,
            "gcd,(,a,:,Int,,,b,:,Int,),{,If,(,b,==,0,),{,return,a,;,},return,gcd,(,b,,,a,%,b,),;,},<EOF>",196))
        
    def test96(self):
        """test block"""
        self.assertTrue(TestLexer.test(
            """
            gcd(a: Int, b: Int) {
                If (b == 0) {
                    return a;
                }
                return gcd(b, a % b);
            }
            """,
            "gcd,(,a,:,Int,,,b,:,Int,),{,If,(,b,==,0,),{,return,a,;,},return,gcd,(,b,,,a,%,b,),;,},<EOF>",196))
        
    def test97(self):
        """test block"""
        self.assertTrue(TestLexer.test(
            """
            binarySearch(arr: Array[Int, 10], l: Int, r: Int, x: Int) 
            { 
                If (r >= l) { 
                    mid: Int = l + (r - l) / 2;  
                    If (arr[mid] == x) {
                        return mid;
                    }
                    If (arr[mid] > x) {
                        return binarySearch(arr, l, mid - 1, x);
                    }
                    return binarySearch(arr, mid + 1, r, x); 
                } 
                return -1; 
            } 
            """,
            "binarySearch,(,arr,:,Array,[,Int,,,10,],,,l,:,Int,,,r,:,Int,,,x,:,Int,),{,If,(,r,>=,l,),{,mid,:,Int,=,l,+,(,r,-,l,),/,2,;,If,(,arr,[,mid,],==,x,),{,return,mid,;,},If,(,arr,[,mid,],>,x,),{,return,binarySearch,(,arr,,,l,,,mid,-,1,,,x,),;,},return,binarySearch,(,arr,,,mid,+,1,,,r,,,x,),;,},return,-,1,;,},<EOF>",197))
        
    def test98(self):
        """test block"""
        self.assertTrue(TestLexer.test(
            """
            factorial(n: Int)
            {
                If (n == 0) {
                    return 1;
                }
                return n * factorial(n - 1);
            } 
            """,
            "factorial,(,n,:,Int,),{,If,(,n,==,0,),{,return,1,;,},return,n,*,factorial,(,n,-,1,),;,},<EOF>",198))
        
    def test99(self):
        """test block"""
        self.assertTrue(TestLexer.test(
            """
            Fibonacci(n: Int)
            {
                If (n == 1 || n == 2)
                    return 1;
                return Fibonacci(n - 1) + Fibonacci(n - 2);
            }
            """,
            "Fibonacci,(,n,:,Int,),{,If,(,n,==,1,||,n,==,2,),return,1,;,return,Fibonacci,(,n,-,1,),+,Fibonacci,(,n,-,2,),;,},<EOF>",199))
        
    def test100(self):
        """test block"""
        self.assertTrue(TestLexer.test(
            """
            SumRecursion(n: Int) {
                ##
                    sum = 1 + ... + n
                ##
                if (n == 0) {
                    return 0;
                }
                return n + SumRecursion(n - 1);
            }
            """,
            "SumRecursion,(,n,:,Int,),{,if,(,n,==,0,),{,return,0,;,},return,n,+,SumRecursion,(,n,-,1,),;,},<EOF>",200))