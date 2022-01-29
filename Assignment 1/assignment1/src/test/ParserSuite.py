import unittest
from TestUtils import TestParser

# class ParserSuite(unittest.TestCase):
#     def test1(self):
#         input = """
#             Class Program {
#                 main() {
#                     Var a: Array[Int,0xAC1];
#                     Var b: Int = 0b0;
#                     Var a: A= a.b.c;
#                     x[1] = 7 - 3;
#                 }
#             }
#             """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 201))
#     def test2(self):
#         input = """
#             Class Program {
#                 getName() {
#                     Var b: Float = 0.300000e7;
#                 }
#                 main() {
#                     Var a: Int = 5;
#                     Val a_b : Float = 7.35e-45;
#                 }
#             }
#             """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 202))

#     def test3(self):
#         input = """
#             Class Program {
#                 Var $a: Int = 5;
#                 $getName() {
#                     Var b: Float = 0.300000e7;
#                 }
#                 main() {
#                     Val a_b : Float = 7.35e-45;
#                 }
#             }
#             """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 203))

#     def test4(self):
#         input = """
#             Class Program {
#                 Var $a: Int = 5;
#                 main() {
#                     Val a_b : Float = 7.35e-45;
#                 }
#             }
#             """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 204))           

#     def test5(self):
#         input = """
#         	Class Main {
#   				$main($a:Int) {
#     				System_out.println(Hello_World);
#   				}
# 			}"""
#         expected = "Error on line 3 col 12: $a"
#         self.assertTrue(TestParser.test(input,expected,205))
        
#     def test6(self):
#         input = """
#         Class Main {
#     		$main(a : Int) {
#     			Var first, second : Int = 10, 20;
#     			Var sum : Int = first + second;
#     			System_out.println(Enter_two_numbers);
#     			System_out.println(first + second);
#     		## add two numbers ##
#     			System_out.println(The_sum_is + sum);
#   			}
# 		}"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,206))

#     def test7(self):
#         """Simple program"""
#         input = """
#         Class SwapNumbers {
#     		$main(a : Array[String, 5]) {
# 				Var first, second : Int = 1.20, 2.45;
#         	## Value of first is assigned to temporary ##
# 				Var temporary : Int = first;
#         		System_out.println(Before_swap);
#         		System_out.println(First_number + first);
#         		System_out.println(Second_number +  second);
#         	## Value of second is assigned to first ##
#         		first = second;
#         	## Value of temporary (which contains the initial value of first) is assigned to second ##
#         		second = temporary;
#         		System_out.println(After_swap);
#         		System_out.println(Firs_number + first);
#         		System_out.println(Second_number + second);
#     		}
# 		}"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,207))

#     def test8(self):
#         input = """
#         Class EvenOdd {
#         	Test(a : Array[String, 0x57]) {
#              	Var num: Int =  reader.nextInt();
#                 Var reader: Scanner = New Scanner(System.in);
#        			(System.out).print(Enter_a_number);

#         		If(num % 2 == 0) {
#             		System_out.println(num_is_even);
#               	}
#         		Else {
#             		System_out.println(num_is_odd);
# 				}
#    			 }
# 		}"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,208))
        
#     def test9(self):
#         input = """
#         Class test {
#     		$MainTest() {
#       ## make a connection to the file ##
#       			Path.file = Paths.get(input.txt);

#       ## read all lines of the file ##
#       			long.count = Files.count();
#       			System_out.println(Total_Lines + count);
#   			}
# 		}"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,209))

#     def test10(self):
#         input = """
#             Class Program {
#                 getName() {
#                     Var Name: String = Your_name;
#                 }
#                 main() {
#                     If (x >= y) {
#                         Var a: Int = 0xBF;
#                         a = a + y;
#                     }
#                     Elseif (x >= z) {
#                         Var b: Int = 0xFA;
#                         b = b + x;
#                     }
#                     Else {
#                         Self.Huy();
#                     }
#                 }
#             }
            
#              """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 210))
        
#     def test11(self):
#         input = """
#             Class Program {
#                 main(){
#                     Return;
#                 }
#             }
#             Class Rin: Dog {
#                 Var ny: Array[Int,3] = Array(1,3,2) ;
#             }
#             """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 211))
    
#     def test12(self):
#         input = """
#             Class Program {
#                 main(){
#                     A.Bc();
#                     Return x;
#                 }
#             }
#             Class loli {
#                 testloop(a: Int; b: Float) {
#                     Foreach (i In 0 .. 15) {
#                         s = s + a[i];
#                     }
#                 }
#             }
#             """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 212))
        
#     def test13(self):
#         input = """
#             Class Program {
#                 Main(a, b: Int) {
#                     Return (a || b) < c.square(1,2) && 5;
#                 } 
#                 main(){
#                     Return Self.Main(7,9);
#                 }
#             }
#             """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 213))
    
#     def test14(self):
#         """Simple program"""
#         input = """
#         Class FibonacciEx {
#             Fibo(args : String) {
#                 System.out.println(fibonacci);
#                 Foreach (i In 0 .. 10){
#                     System.out.print();
#                 }
#             }
#             fibonacci(n : Int) {
#                 Var f0, f1, f2 : Int = 0,1,1;
 
#                 If (n < 0) {
#                     Return -1;
#                 } 
#                 Elseif ((n == 0) || (n == 1)) {
#                     Return n;
#                 }
#                 Else {
#                     Foreach (i In 2 .. n){
#                         f0 = f1;
#                         f1 = fn;
#                         fn = f0 + f1;
#                     }
#                 }
#                 Return fn;
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,214))
        
        
#     def test15(self):
#         """Simple program"""
#         input = """
#         Class FibonacciEx {
#             Fibo(args : String) {
#                 System.out.println(fibonacci);
#                 Foreach (i In 0 .. 10){
#                     System.out.print();
#                 }
#             }
#             fibonacci(Int n) {
#                 Var f0, f1, f2 : Int = 0,1,1;
 
#                 If (n < 0) {
#                     Return -1;
#                 } 
#                 Elseif ((n == 0) || (n == 1)) {
#                     Return n;
#                 }
#                 Else {
#                     Foreach (i In 2 .. n){
#                         f0 = f1;
#                         f1 = fn;
#                         fn = f0 + f1;
#                     }
#                 }
#                 Return fn;
#             }
#         }"""
#         expected = "Error on line 9 col 22: Int"
#         self.assertTrue(TestParser.test(input,expected,215))
        
#     def test16(self):
#         """Simple program"""
#         input = """
#         Class FibonacciEx {
#             Fibo(args : String) {
#                 System.out.println(fibonacci);
#                 Foreach (i In 0 .. 10){
#                     System.out.print();
#                 }
#             }
#             fibonacci(n : Int) {
#                 Var f0, f1, f2 : Int = 0,1,1;
 
#                 If (n < 0) {
#                     Return -1;
#                 } 
#                 Elseif (n == 0 || n == 1) {
#                     Return n;
#                 }
#                 Else {
#                     Foreach (i In 2 .. n){
#                         f0 = f1;
#                         f1 = fn;
#                         fn = f0 + f1;
#                     }
#                 }
#                 Return fn;
#             }
#         }"""
#         expected = "Error on line 15 col 36: =="
#         self.assertTrue(TestParser.test(input,expected,216))
        
#     def test17(self):
#         """Simple program"""
#         input = """
#         Class FibonacciEx {
#             Fibo(args : String) {
#                 System.out.println(fibonacci);
#                 Foreach (i In 0 .. 10){
#                     System.out.print();
#                 }
#             }
#             fibonacci(n : Int) {
#                 Var f0, f1: Int = 0,1,1;
#                 If (n < 0) {
#                     Return -1;
#                 } 
#                 Elseif (n == 0 || n == 1) {
#                     Return n;
#                 }
#                 Else {
#                     Foreach (i In 2 .. n){
#                         f0 = f1;
#                         f1 = fn;
#                         fn = f0 + f1;
#                     }
#                 }
#                 Return fn;
#             }
#         }"""
#         expected = "Error on line 10 col 37: ,"
#         self.assertTrue(TestParser.test(input,expected,217))

#     def test18(self):
#         input = """
#         Class HoliHalo{
#            stringToListNode(input : String) {
#             ## Now convert that list into linked list ##
#                 Var Root : ListNode  = New ListNode(0);
#                 Var ptr : ListNode  = Root;
#             ## Generate array from the input ##
#                 Var nodeValues : Array[Int,2] = stringTo.IntegerArray(input);
#                 Foreach (i In item .. cal){
#                     ptr.next = New ListNode(item);
#                     ptr = ptr.next;
#                 }
#                 Return Root.next;
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,218))

#     def test19(self):
#         input = """
#         Class HoliHalo{
#            stringToListNode(input : String) {
#             ## Now convert that list into linked list ##
#                 Var Root : ListNode  = New ListNode(0);
#                 Var ptr : ListNode  = Root
#             ## Generate array from the input ##
#                 Var nodeValues : Array[Int,2] = stringTo.IntegerArray(input);
#                 Foreach (i In item .. cal){
#                     ptr.next = New ListNode(item);
#                     ptr = ptr.next;
#                 }
#                 Return Root.next;
#             }
#         }"""
#         expected = "Error on line 8 col 16: Var"
#         self.assertTrue(TestParser.test(input,expected,219))
        
#     def test20(self):
#         input = """
#         Class HoliHalo{
#            stringToListNode(input : String) {
#             ## Now convert that list into linked list ##
#                 Var Root : ListNode  = New ListNode(0);
#                 Var ptr : ListNode  = Root;
#             ## Generate array from the input ##
#                 Var nodeValues : Array[Int,2] = stringTo.IntegerArray(input);
#                 Foreach (i In item .. cal By){
#                     ptr.next = New ListNode(item);
#                     ptr = ptr.next;
#                 }
#                 Return Root.next;
#             }
#         }"""
#         expected = "Error on line 9 col 44: )"
#         self.assertTrue(TestParser.test(input,expected,220))
        
#     def test21(self):
#         input = """
#         Class HaloHoli{
#             treeNodeToString( root : String ) {
#                 Var output : Int  = a;
#                 Var nodeQueue : LinkedList = New LinkedList();
#                 If (root == Null) {
#                     Return ;
#                 }
#                 nodeQueue.add(root);
#                 If(!nodeQueue.isEmpty()){
#                     Var node : TreeNode = nodeQueue.remove();
#                     If(node == Null){
#                         output = Null;
#                         Continue;
#                     }
    
#                     output = Str.valueOf(node.val);
#                     nodeQueue.add(node.left);
#                     nodeQueue.add(node.right);
#                 }
#                 Return output;
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,221))
        
        
#     def test22(self):
#         input = """
#         Class HaloHoli{
#             treeNodeToString( root : String ) {
#                 Var output : Int  = a;
#                 Var nodeQueue : LinkedList = New LinkedList();
#                 If (root == Null) {
#                     Return ;
#                 }
#                 nodeQueue.add(root);
#                 If(!nodeQueue.isEmpty()){
#                     Var node : TreeNode = nodeQueue.remove();
#                     If(node == Null){
#                         output = Null;
#                         Continue;
#                     }
    
#                     output = String.valueOf(node.val) ;
#                     nodeQueue.add(node.left);
#                     nodeQueue.add(node.right);
#                 }
#                 Return output;
#             }
#         }"""
#         expected = "Error on line 17 col 29: String"
#         self.assertTrue(TestParser.test(input,expected,222))

#     def test23(self):
#         input = """
#         Class HaloHoli{
#             treeNodeToString( root : String ) {
#                 Var output : Int  = a;
#                 Var nodeQueue : LinkedList = New LinkedList();
#                 If (root == Null) {
#                     Return;
#                 }
#                 nodeQueue.add(root);
#                 If(!nodeQueue.isEmpty()){
#                     Var node : TreeNode = nodeQueue.remove();
#                     If(node == Null){
#                         output =Null;
#                         Continue();
#                     }
    
#                     output = Str.valueOf(node.val) ;
#                     nodeQueue.add(node.left);
#                     nodeQueue.add(node.right);
#                 }
#                 Return output;
#             }
#         }"""
#         expected = "Error on line 14 col 32: ("
#         self.assertTrue(TestParser.test(input,expected,223))
        
#     def test24(self):
#         input = """
#         Class HaloHoli{
#             treeNodeToString( root : String ) {
#                 Var output : Int  = a;
#                 Var nodeQueue : LinkedList = New LinkedList();
#                 If (root == Null) {
#                     Return [];
#                 }
#                 Return output;
#             }
#         }"""
#         expected = "Error on line 7 col 27: ["
#         self.assertTrue(TestParser.test(input,expected,224))
        
#     def test25(self):
#         input = """
#         Class HaloHoli{
#             treeNodeToString( root : String ) {
#                 Var output : Int  = a;
#                 Var nodeQueue : LinkedList = New LinkedList();
#                 If (root == Null) {
#                     Return;
#                 }
#                 Return Continue;
#             }
#         }"""
#         expected = "Error on line 9 col 23: Continue"
#         self.assertTrue(TestParser.test(input,expected,225))
        
#     def test26(self):
#         """Simple program"""
#         input = """
#         Class Holi2 {
#             Tree(input : String) {  
#                 Var item : String = parts[1];
#                 Var root : TreeNode = New TreeNode(Integer.parseInt(item));
#                 Var nodeQueue : QueueTreeNode= New LinkedList();
#                 Var index : Int = 1;
#                 input = input.trim();
#                 If(input.length() == 0) {
#                     Return Null;
#                 }
#                 nodeQueue.add(root);
#                 If(!nodeQueue.isEmpty()){
#                     node = nodeQueue.remove();
#                     If (index == parts.length){
#                         Break;
#                     }
#                     item = parts[index+1];
#                     index = index +1;
#                     If (3!=2) {
#                         leftNumber = Integer.parseInt(item);
#                         Var node_left : TreeNode = New TreeNode(leftNumber);
#                         nodeQueue.add(node.left);
#                     }
    
#                     If(index == parts.length) {
#                         Break;
#                     }
#                 }
#                 Return root;
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,226))
        
#     def test27(self):
#         input = """
#         Class Holi2 {
#             Tree(input :: String) {  
#                 Var item : String = parts[1];
#                 Var root : TreeNode = New TreeNode(Integer.parseInt(item));
#                 Var nodeQueue : QueueTreeNode= New LinkedList();
#                 Var index : Int = 1;
#                 input = input.trim();
#                 If(input.length() == 0) {
#                     Return Null;
#                 }
#                 nodeQueue.add(root);
#                 If(!nodeQueue.isEmpty()){
#                     node = nodeQueue.remove();
#                     If (index == parts.length){
#                         Break;
#                     }
#                     item = parts[index+1];
#                     index = index +1;
#                     If (3!=2) {
#                         leftNumber = Integer.parseInt(item);
#                         Var node.left : TreeNode = New TreeNode(leftNumber);
#                         nodeQueue.add(node.left);
#                     }
    
#                     If(index == parts.length) {
#                         Break;
#                     }
#                 }
#                 Return root;
#             }
#         }"""
#         expected = "Error on line 3 col 23: ::"
#         self.assertTrue(TestParser.test(input,expected,227))
        
#     def test28(self):
#         input = """
#         Class Holi2 {
#             Tree(input : String) {  
#                 Var item : String = parts[1];
#                 Var root : TreeNode = New TreeNode(Integer.parseInt(item));
#                 Var nodeQueue : QueueTreeNode= New LinkedList();
#                 input = input.trim();
#                 If(input.length() == 0) {
#                     Return 3+7 == 0;
#                 }
#                 nodeQueue.add(root);
#                 Return root;
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,228)) 
        
#     def test29(self):
#         input = """
#         Class Holi2 {
#             Tree(input : String) {  
#                 Var item : String = parts[1];
#                 Var root : TreeNode = New TreeNode(Integer.parseInt(item));
#                 Var nodeQueue : QueueTreeNode= New LinkedList();
#                 input = input.trim();
#                 If(input.length() == 0) {
#                     Return 3+7 (== 0);
#                 }
#                 nodeQueue.add(root);
#                 Return root;
#             }
#         }"""
#         expected = "Error on line 9 col 31: ("
#         self.assertTrue(TestParser.test(input,expected,229))
        
#     def test30(self):
#         input = """
#         Class Holi2 {
#             Tree(input : String) {  
#                 nodeQueue.add(root);
#                 Return root = 3;
#             }
#         }"""
#         expected = "Error on line 5 col 28: ="
#         self.assertTrue(TestParser.test(input,expected,230))
        
#     def test31(self):
#         input = """
#         Class Main {
#             main(args : String) {
#                 Var n1,n2 : Int = 72, 120;
#                 Var lcm : Int = n1 + n2;
#                 If(1 == 1) {
#                     If( lcm  %  n1 == 0 && lcm  %  n2 == 0 ) {
#                     System.out.printf(n1, n2, lcm);
#                     Break;
#                     }
#                 lcm = lcm + 1;
#                 }
#             }
#         }"""
#         expected = "Error on line 7 col 54: =="
#         self.assertTrue(TestParser.test(input,expected,231))
        
#     def test32(self):
#         input = """
#         Class Main {
#             main(args : String) {
#                 Var n1,n2 : Int = 72, 120;
#                 Var lcm : Int = n1 + n2;
#                 If(1 == 1) {
#                     If( (lcm  %  n1) == 0 && (lcm  %  n2) == 0 ) {
#                     System.out.printf(n1, n2, lcm);
#                     Break;
#                     }
#                 lcm = lcm + 1;
#                 }
#             }
#         }"""
#         expected = "Error on line 7 col 58: =="
#         self.assertTrue(TestParser.test(input,expected,232))
        
#     def test33(self):
#         input = """
#         Class Main {
#             main(args : String) {
#                 Var n1,n2 : Int = 72, 120;
#                 Var lcm : Int = n1 + n2;
#                 If(1 == 1) {
#                     If( ((lcm  %  n1) == 0) && ((lcm  %  n2) == 0) ) {
#                     System.out.printf(n1, n2, lcm);
#                     Break;
#                     }
#                 lcm = lcm + 1;
#                 }
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,233))
        
#     def test34(self):
#         input = """
#         Class Main {
#             main(Hol: String) {
#                 Var input : Scanner  = New Scanner (System.in);
#                 System.out.print(Input);
#                 Var num1 : Int  = input.nextInt();
#                 System.out.print(Input);
#                 Var num2 : Int  = input.nextInt();
#                 Var sum : Int  = num1 + num2;
#                 System.out.println();
#                 System.out.println(sum);
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,234))

#     def test35(self):
#         input = """
#         Class Main {
#             main(Hol: String) {
#                 Var input : Scanner  = New Scanner (System.in);
#                 System.print(input);
#                 Var num1, num2, num3 : Int  = input.nextInt(), input.nextInt();
#                 System.out.print(Input);
#                 Var sum : Int  = num1 + num2;
#                 System.out.println(sum);
#             }
#         }"""
#         expected = "Error on line 6 col 73: ,"
#         self.assertTrue(TestParser.test(input,expected,235))
        
#     def test36(self):
#         input = """
#         Class Main {
#             main(Hol: String) {
#                 Var num2 : Int  = input.nextInt();
#                 System.out.println();
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,236))
        
#     def test37(self):
#         """Simple program"""
#         input = """
#         Class Main {
#             main(args : Int) {
#                 Var year : Int = 1996;
#                 Var leap : Boolean = False;
#                 If ((year % 4) == 0){
#                     If ((year % 100) == 0) {
#                         If ((year % 400) == 0) {
#                             leap = True;
#                         }
#                         Else { 
#                             leap = False;
#                         }
#                     }
#                     Else{
#                         leap = True;
#                     }
#                 } 
#                 Else{
#                     leap == False;
#                 }
#                 If(leap){ 
#                     System.out.println(leap_year);
#                 } 
#                 Else{
#                     System.out.println(not_leap_year);
#                 }       
#             }
#         }"""
#         expected = "Error on line 20 col 25: =="
#         self.assertTrue(TestParser.test(input,expected,237))
        
#     def test38(self):
#         """Simple program"""
#         input = """
#         Class Main {
#             main(args : Int) {
#                 Var year : Int = 19.96;
#                 Var leap : Boolean = False;
#                 If (((year % 4) == 0)){
#                     If ((year % 100) == 0) {
#                         If ((year % 400) == 0) {
#                             leap = True;
#                         }
#                         Else { 
#                             leap = False;
#                         }
#                     }
#                     Else{
#                         leap = True;
#                     }
#                 } 
#                 Else{
#                     leap = false;
#                 }
#                 If(leap){ 
#                     System.out.println(leap_year);
#                 } 
#                 Else{
#                     System.out.println(not_leap_year);
#                 }    
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,238))
    
#     def test39(self):
#         input = """
#         Class Posi_Negative{
#             main(arg : Int) {
#                 Var number : Float = 658.32e10
#                 If(number < 0.0){
#                     System.out.println(negative);
#                 }
#                 ElseIf ( number > 0.0){
#                     System.out.println(positive);
#                 }
#                 Else{
#                     System.out.println(0);
#                 }
#             }
#         }"""
#         expected = "Error on line 5 col 16: If"
#         self.assertTrue(TestParser.test(input,expected,239))
        
#     def test40(self):
#         input = """
#         Class Posi_Negative{
#             main(arg : Int) {
#                 Var number : Float = 658.32e10;
#                 If(number < 0.0){
#                     System.out.println(negative);
#                 }
#                 ElseIf(number > 0.0){
#                     System.out.println(positive);
#                 }
#                 Else{
#                     System.out.println(0);
#                 }
#             }
#         }"""
#         expected = "Error on line 8 col 22: ("
#         self.assertTrue(TestParser.test(input,expected,240))
        
#     def test41(self):
#         input = """
#         Class Posi_Negative{
#             main(arg : Int) {
#                 Var number : Float = 658.32e10;
#                 If(number < 0.0){
#                     System.out.println(negative);
#                 }
#                 Elseif(number > 0.0){
#                     System.out.println(positive);
#                 }
#                 Else{
#                     System.out.println(0);
#                 }
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,241))
        
#     def test42(self):
#         input = """
#         Class Exercise27 {
#             main(args : String){
#                 Var octal_num, hex_num : String;
#                 Var decnum : Int;
#                 Var in : Scanner = New Scanner(System.in);
#                 System.out.print(Input);
#                 hex_num = Self.toHexString(decnum);
#                 System.out.print(hex_num);
#             }
#     }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,242))
        
#     def test43(self):
#         input = """
#         Class Exercise27 {
#             main(args : String){
#                 Var octal_num, hex_num : String;
#                 Var decnum : Int;
#                 Var in : Scanner = New Scanner(System.in);
#                 System.out.print(Input);
#                 hex_num = toHexString(decnum);
#                 System.out.print(hex_num);
#             }
#     }"""
#         expected = "Error on line 8 col 37: ("
#         self.assertTrue(TestParser.test(input,expected,243))
        
#     def test44(self):
#         input = """
#         Class Exercise27 {
#             main(args : String){
#                 Var octal_num, hex_num : String;
#                 Var decnum : Int;
#                 Var in : Scanner = new Scanner(System.in);
#                 System.out.print(Input.qq(), ababa);
#                 hex_num = toHexString(decnum);
#                 System.out.print(hex_num);
#             }
#     }"""
#         expected = "Error on line 6 col 39: Scanner"
#         self.assertTrue(TestParser.test(input,expected,244))
        
#     def test45(self):
#         input = """
#         Class Alphabet {
#             main(args : Float) {
#                 If( (c >= "a" && c <= "z") || (c >= "A" && c <= "Z")){
#                     System.out.println(alphabet);
#                 }
#                 Else{
#                     System.out.println(alphabet);
#                 }
#             }
#         }"""
#         expected = "Error on line 4 col 35: <="
#         self.assertTrue(TestParser.test(input,expected,245))


#     def test46(self):
#         input = """
#         Class Alphabet {
#             main(args : Float) {
#                 If( ((c >= "a") && (c <= "z")) || ((c >= "A") && (c <= "Z"))){
#                     System.out.println(alphabet);
#                 }
#                 Else{
#                     System.out.println(alphabet);
#                 }
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,246))
        
#     def test47(self):
#         input = """
#         Class Alphabet {
#             main(args : Float, :Int) {
#                 If( ((c >= "a") && (c <= "z")) || ((c >= "A") && (c <= "Z"))){
#                     System.out.println(alphabet);
#                 }
#                 Else{
#                     System.out.println(alphabet);
#                 }
#             }
#         }"""
#         expected = "Error on line 3 col 29: ,"
#         self.assertTrue(TestParser.test(input,expected,247))
        
#     def test48(self):
#         input = """
#         Class StandardDeviation {
#             main(args : Float) {
#                 Var numArray : Array[Int,10] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
#                 Var SD : Int = calculateSD(numArray);
#                 System.out.format(SD);
#             }

#             calculateSD(A : Int){
#                 Var sum, standardDeviation : Int = 0.0, 0.0;
#                 Var length, mean : Int = numArray.length, sum/length;
#                 Foreach(i In item .. cal){
#                     sum = num + 1;
#                 }

#                 Foreach(i In item .. cal){
#                     standardDeviation = standardDeviation + Math.pow(num - mean, 2);
#                 }
#                 return Math.sqrt(standardDeviation/length);
#              }
#         }"""
#         expected = "Error on line 5 col 42: ("
#         self.assertTrue(TestParser.test(input,expected,248))
        
#     def test49(self):
#         input = """
#         Class StandardDeviation {
#             main(args : Float) {
#                 Var numArray : Array[Int,10] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
#                 Var SD : Int = calculateSD;
#                 System.out.format(SD);
#             }

#             calculateSD(A : Int){
#                 Var sum, standardDeviation : Int = 0.0, 0.0;
#                 Var length, mean : Int = numArray.length, sum/length;
#                 Foreach(i In item .. cal){
#                     sum = num + 1;
#                 }

#                 Foreach(i In item .. cal){
#                     standardDeviation = standardDeviation + Math.pow(num - mean, 2);
#                 }
#                 return Math.sqrt(standardDeviation/length);
#              }
#         }"""
#         expected = "Error on line 19 col 23: Math"
#         self.assertTrue(TestParser.test(input,expected,249))

#     def test50(self):
#         input = """
#         Class StandardDeviation {
#             main(args : Float) {
#                 Var numArray : Array[Int,10] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
#                 Var SD : Int = calculateSD;
#                 System.out.format(SD);
#             }

#             calculateSD(A : Int){
#                 Var sum, standardDeviation : Int = 0.0, 0.0;
#                 Var length, mean : Int = numArray.length, sum/length;
#                 Foreach(i In item .. cal){
#                     sum = num + 1;
#                 }

#                 Foreach(i In item .. cal){
#                     standardDeviation = standardDeviation + Math.pow(num - mean, 2);
#                 }
#                 Return Math.sqrt(standardDeviation/length);
#              }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,250))
        
#     def test51(self):
#         input = """
#             Class Brray {
#                 Sannan(baka : Int) {
#                     Var array : Array[Int,5] = Array(1, 2, 3, 4, 5);
#                     Foreach(element In 1 .. 4) {
#                         System.out.println(array[element]);
#                     }
#                 }
#             }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,251))
        
#     def test52(self):
#         input = """
#             Class Crray {
#                 Sannan(baka : Int) {
#                     Var array : Array[Int,5] = Array(1, 2, 3, 4, 5);
#                     Foreach(element In 1 .. 4 By 7-7 == 3) {
#                         System.out.println(array[element]);
#                     }
#                 }
#             }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,252))
        
#     def test53(self):
#         input = """
#             Class Crray {
#                 Sannan(baka : Int) {
#                     Var array : Array[Int,5] = Array(1, 2, 3, 4, 5);
#                     Foreach(element In 1 .. 4 By 7-7 == 3 - 5) {
#                         System.out.println(array[element]);
#                     }
#                 }
#             }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,253))
        
#     def test54(self):
#         input = """
#         Class Main {
#             Main(args : Int){
#                 Var animals : LinkedList = New LinkedList();
#                 Var middle : String;
#                 middle = animals.get(animals.size()/2);
#                 animals.add(Dog);
#                 animals.addFirst(Cat);
#                 animals.addLast(Horse);
#                 System.out.println(animals);
#                 System.out.println(middle);
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,254))

#     def test55(self):
#         input = """
#         Class Main {
#             Main(args : Int){
#                 Var animals : LinkedList = New LinkedList();
#                 Var middle : String = animals.get(animals.size()/2);;
#                 animals.add(Dog);
#                 animals.addFirst(Cat);
#                 animals.addLast(Horse);
#                 System.out.println(animals);
#                 System.out.println(middle);
#             }
#         }"""
#         expected = "Error on line 5 col 68: ;"
#         self.assertTrue(TestParser.test(input,expected,255))
        
#     def test56(self):
#         input = """
#         Class Main {
#             Main(args : Int){
#                 Var animals : LinkedList = New LinkedList();
#                 Var middle : String = animals.get(animals.size()/2);
#                 animals.add(Dog);
#                 animals.addFirst(Cat);
#                 animals.addLast(Horse);
#                 System.out.println(animals);
#                 System.out.println(middle);
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,256))
        
#     def test57(self):
#         input = """
#         Class Test57{
#             Brand(SD : Int) {
# 		        Var amount : Int = 0;
# 		Foreach( i In 1 .. 4 ){
# 			Foreach( j In 1 .. 4 ){
# 				Foreach( k In 1 .. 4 ){
# 					If(k != i && k != j && i != j){
# 						amount = amount + 1;
# 						System.out.println(i + j + k);
# 					}
# 				}
# 			}
# 		}
# 		System.out.println(amount);
# 	}
# }
# """
#         expected = "Error on line 8 col 20: !="
#         self.assertTrue(TestParser.test(input,expected,257))
        
#     def test58(self):
#         input = """
#         Class Test58{
#             Brand(SD : Int) {
# 		        Var amount : Int = 0;
#                 Foreach( i In 1 .. 4 ){
#                     Foreach( j In 1 .. 4 ){
#                         Foreach( k In 1 .. 4 ){
#                             If((k != i) && (k != j) && (i != j)){
#                                 amount = amount + 1;
#                                 System.out.println(i + j + k);
#                             }
#                         }
#                     }
#                 }
#                 System.out.println(amount);
#             }
#         }
# """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,258))
        
#     def test59(self):
#         input = """
#         Class Test59{
#             Brand(SD : Int) {
# 		        Var amount : Int = 0;
#                 Foreach( i In 1 .. 4 By Continue){
#                     Foreach( j In 1 .. 4 ){
#                         Break;
#                         Foreach( k In 1 .. 4 ){
#                             If((k != i) && (k != j) && (i != j)){
#                                 amount = amount + 1;
#                                 System.out.println(i + j + k);
#                             }
#                         }
#                     }
#                 }
#                 System.out.println(amount);
#             }
#         }
#         """
#         expected = "Error on line 5 col 40: Continue"
#         self.assertTrue(TestParser.test(input,expected,259))
        
#     def test60(self):
#         input = """
#         Class Test60 {
#             Mane (OPO : Int){
#                 Scanner in = new Scanner(System.in);
#                 Var x,y,z : Int = in.nextInt(),in.nextInt(),in.nextInt();
#                 System.out.print(first);
#                 System.out.print(second);
#                 System.out.print(third);
#                 System.out.print(sumoftwo(x, y, z));
#             }
            
#             sumoftwo(q,w,e : Int){	
#                 Return ((p + q) == r || (q + r) == p || (r + p) == q);	
#             }
#         }"""
#         expected = "Error on line 4 col 24: in"
#         self.assertTrue(TestParser.test(input,expected,260))
        
#     def test61(self):
#         input = """
#         Class Test61 {
#             Mane (OPO : Int){
#                 Var in : Scanner  = New Scanner(System.in);
#                 Var x,y,z : Int = in.nextInt(),in.nextInt(),in.nextInt();
#                 System.out.print(first);
#                 System.out.print(second);
#                 System.out.print(third);
#                 System.out.print(sumoftwo(x,y,z),v);
#             }
            
#             sumoftwo(q,w,e : Int){	
#                 Return ((p + q) == r || (q + r) == p || (r + p) == q);	
#             }
#         }"""
#         expected = "Error on line 9 col 41: ("
#         self.assertTrue(TestParser.test(input,expected,261))
        
#     def test62(self):
#         input = """
#         Class Test62 {
#             Mane (OPO : Int){
#                 Var in : Scanner  = New Scanner(System.in);
#                 Var x,y,z : Int = in.nextInt(),in.nextInt(),in.nextInt();
#                 System.out.print(first);
#                 System.out.print(second);
#                 System.out.print(third);
#                 System.out.print(sumoftwo,v);
#             }
            
#             sumoftwo(q,w,e : Int){	
#                 Return ((p + q) == r || (q + r) == p || (r + p) == q);	
#             }
#         }"""
#         expected = "Error on line 13 col 48: =="
#         self.assertTrue(TestParser.test(input,expected,262))


#     def test63(self):
#         input = """
#         Class Test63 {
#             Mane (OPO : Int){
#                 Var in : Scanner  = New Scanner(System.in);
#                 Var x,y,z : Int = in.nextInt(),in.nextInt(),in.nextInt();
#                 System.out.print(first);
#                 System.out.print(second);
#                 System.out.print(third);
#                 System.out.print(sumoftwo,v);
#             }
            
#             sumoftwo(q,w,e : Int){	
#                 Return (((p + q) == r) || ((q + r) == p) || ((r + p) == q));	
#             }
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,263))
        
#     def test64(self):
#         input = """
#         Class Test64{
#             Soka(Bku : Int){	
#                 Var in : Scanner  = New Scanner(System.in);
#                 Var line : String = in.nextLine();
#                 System.out.print(Input);
#                 line = line.toLowerCase();
#                 System.out.println(line); 
#             }			
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,264))
        
#     def test65(self):
#         input = """
#         Class Test65 {
#             main(Bran : Float){
#                 System.out.println(main_string.substring(0, 7) + word + main_string.substring(6));
# 	        }       
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,265))

#     def test66(self):
#         input = """
#         Class Test66 {
#             Bakazoro(Luffy : Int){
#                 Var str1 : String ;
#                 Var len : Int = str1.length() - 1;  
#                 If(len >= 3){
#                     System.out.println( str1.substring(0, 3));
#                 }
#                 Elseif(len == 1){
#                     System.out.println( (str1.charAt(0)));
#                 }
#                 Else {
#                     System.out.println();
#                 }
#             }
#         }
# """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,266))
        
#     def test67(self):
#         input = """
#         Class Test67 {
#             Bakazoro(Luffy : Int){
#                 Var str1 : String ;
#                 Var len : Int = str1.length() - 1;  
#                 If(len >= 3)
#                     System.out.println( str1.substring(0, 3));
                
#                 Elseif(len == 1){
#                     System.out.println( (str1.charAt(0)));
#                 }
#                 Else {
#                     System.out.println();
#                 }
#             }
#         }
# """
#         expected = "Error on line 7 col 20: System"
#         self.assertTrue(TestParser.test(input,expected,267))
        
#     def test68(self):
#         input = """
#         Class Test68 {
#             Bakazoro(Luffy : Int){
#                 Var str1 : String ;
#                 Var len : Int = str1.length() - 1;  
#                 Else {
#                     System.out.println();
#                 }
#             }
#         }
# """
#         expected = "Error on line 6 col 16: Else"
#         self.assertTrue(TestParser.test(input,expected,268)) 
        
#     def test69(self):
#         """Simple program"""
#         input = """
#         class Test69 {
#             Bro69(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, -20, 0), Array(5, -50, 10), Array(array1[2], array2[2], array1[2]);	 
#             }
#         }
# """
#         expected = "Error on line 2 col 8: class"
#         self.assertTrue(TestParser.test(input,expected,269))
        
#     def test70(self):
#         """Simple program"""
#         input = """
#         Class Test70 {
#             Bro70(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, -20, 0), Array(5, -50, 10), Array(array1[1], array2[2], array1[2]);	 
#             }
#         }
# """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,270))
        
#     def test71(self):
#         input = """
#         Class Test71 {
#             Bro71(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, 20, 0), Array(5, 50, 10), Array(array1[2], array2[2], array1[2]);	 
#             }
#         }
# """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,271))
        
#     def test72(self):
#         input = """
#         Class Test72 {
#             Bro71(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, 20, 0), Array(5, 50, 10), Array(0,2,2);	   
#             }   
#         }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,272))

#     def test73(self):
#         input = """ 
#         Class Test73 {
#             main(Bro : Int){	
#                 Var result : String;
#                 Var left_array, right_array: Array[Int,4] = Array(), Array(1, 4, 5, 2);
#                 System.out.println(Arrays.toString(left_array);  
#                 System.out.println(Arrays.toString(right_array); 
#                 Foreach(i In 0 .. left_array.length ){
#                     Var num1, num2 : Int = left_array[i], right_array[i];
#                     result = result + Integer.toString(num1 * num2); 
#                 }   			
#             }"""
#         expected = "Error on line 6 col 62: ;"
#         self.assertTrue(TestParser.test(input,expected,273))
        
#     def test74(self):
#         input = """ 
#         Class Test74 {
#             main(Bro : Int){	
#                 Var result : String;
#                 Var left_array, right_array: Array[Int,4] = Array(), Array(1, 4, 5, 2);
#                 System.out.println(Arrays.toString(left_array));  
#                 System.out.println(Arrays.toString(right_array)); 
#                 Foreach(i In 0 .. left_array.length ){
#                     Var num1, num2 : Int = left_array[i], right_array[i];
#                     result = result + Integer.toString(num1 * num2); 
#                 }   			
#             }"""
#         expected = "Error on line 12 col 13: <EOF>"
#         self.assertTrue(TestParser.test(input,expected,274))
        
#     def test75(self):
#         input = """ 
#         Class Test75 {
#             main(Bro : Int){	
#                 Var result : String;
#                 Var left_array, right_array: Array[Int,4] = Array(), Array(1, 4, 5, 2);
#                 System.out.println(Arrays.toString(left_array));  
#                 System.out.println(Arrays.toString(right_array)); 
#                 Foreach(i In 0 .. left_array.length ){
#                     Var num1, num2 : Int = left_array[i], right_array[i];
#                     result = result + Integer.toString(num1 * num2); 
#                 }
#                 }   			
#             }"""
#         expected = "successful"
#         self.assertTrue(TestParser.test(input,expected,275))
        
#     def test76(self):
#         """test stmt  """
#         input = """
#             Class Main {
#                $main(args : Array[Int,2]) {
#                   out.println(Hello bae);
#                }
#             }"""
#         expected = """Error on line 4 col 36: bae"""
#         self.assertTrue(TestParser.test(input,expected,276))
        
#     def test77(self):
#         input = """
#             Class Main2 {
#                main(args : Array[Int,2]) {
#                   out.println(Hello + bae);
#                }
#             }"""
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input,expected,277))
        
#     def test78(self):
#         input = """
#             Class Main2 {
#                main(args : Array[Int,2]) {
#                   out.println();
#                }
#             }"""
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input,expected,278))

#     def test79(self):
#         input = """
#             Class Program {
#                main(args : Array[Int,2]) {
#                   out.println(numbers);
#                   Var first:Int = 10;
#                   Var second :Int = 20;
#                   out.println(first + second);

#                ## add two numbers ##
#                   Var sum : Int = first + second;
#                   out.println( sum);
#                }
#             }"""
#         expected ="""successful"""
#         self.assertTrue(TestParser.test(input,expected,279))
        
#     def test80(self):
#         input = """
#             Class Program {
#                main(args : Array[Int,2]) {
#                   out.println(numbers);
#                   Var first, second :Int = 10, 20;
#                   out.println(first ++ second);

#                ## add two numbers ##
#                   Var sum : Int = first + second;
#                   out.println( sum);
#                }
#             }"""
#         expected ="""Error on line 6 col 37: +"""
#         self.assertTrue(TestParser.test(input,expected,280))
        
#     def test81(self):
#         input = """
#             Class Program {
#                main(args : Array[Int,2]) {
#                   out.println(numbers);
#                   Var first, second :Int = 10, 20;
#                   out.println(first + second);

#                ## add two numbers ##
#                   Var sum : Int = first + second;
#                   out.println(sum);
#                   Self.;
#                }
#             }"""
#         expected ="""Error on line 11 col 23: ;"""
#         self.assertTrue(TestParser.test(input,expected,281))


#     def test82(self):
#         input = """
#         Class SwapNumbers {
#            $Swap(args : Array[Int,2]) {
#                Var first, second : Float = 1.20,2.45;
#                out.println(Before_swap);
#                out.println(first);
#                out.println(second);

#                Var temporary : Float = first;
#                first = second;

#         ## Value of temporary (which contains the initial value of first) is assigned to second##
#                second = temporary;
#                out.println(After);
#                out.println(first);
#                out.println(second);
#             }
#          }"""
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input,expected,282))
        
#     def test83(self):
#         input = """
#         Class SwapNumbers {
#            $Swap(args : Array[Int,2]) {
#                Var first, second : Float = 1.20,2.45;
#                out.println(Before_swap);
#                out.println(first) && out.println(second);

#                Var temporary : Float = first;
#                first = second;

#         ## Value of temporary (which contains the initial value of first) is assigned to second##
#                second = temporary;
#                out.println(After);
#                out.println(first);
#                out.println(second);
#             }
#          }"""
#         expected = """Error on line 6 col 34: &&"""
#         self.assertTrue(TestParser.test(input,expected,283))

#     def test84(self):
#         input = """
#         Class SwapNumbers {
#            $Swap(args : Array[Int,2]) {
#                Var first, second : Float = 1.20,2.45;
#                out.println(Before_swap);
#                out.println(first) || out.println(second);

#                Var temporary : Float = first;
#                first = second;

#         ## Value of temporary (which contains the initial value of first) is assigned to second##
#                second = temporary;
#                out.println(After);
#                out.println(first);
#                out.println(second);
#             }
#          }"""
#         expected = """Error on line 6 col 34: ||"""
#         self.assertTrue(TestParser.test(input,expected,284))
        
#     def test85(self):
#         input =  """
#             Class EvenOdd {
#                $Evenodd(args : Array[Int,2] ; a,b: Float) {
#                   Var reader : Scanner = New Scanner(in);
#                   out.print(Enter);
#                   Var num : Int = reader.nextInt();
#                   If(num % 2 == 0){
#                      out.println(even);
#                      }
#                   Else{
#                   out.println(odd);}
#                }
#             }"""
#         expected ="""successful"""
#         self.assertTrue(TestParser.test(input,expected,285))
        
#     def test86(self):
#         input =  """
#             Class EvenOdd {
#                $Evenodd(args : Array[Int,2] && a,b: Float) {
#                   Var reader : Scanner = New Scanner(in);
#                   out.print(Enter);
#                   Var num : Int = reader.nextInt();
#                   If(num % 2 == 0){
#                      out.println(even);
#                      }
#                   Else{
#                   out.println(odd);}
#                }
#             }"""
#         expected ="""Error on line 3 col 44: &&"""
#         self.assertTrue(TestParser.test(input,expected,286))

#     def test87(self):
#         input =  """
#             Class EvenOdd {
#                $Evenodd(args : Array[Int,2] ; a,b: Float) {
#                   Var reader : Scanner = New Scanner(in);
#                   out.print(Enter);
#                   Var num : Int = reader.nextInt();
#                   If(num % 2 == 0 || 1){
#                      out.println(even);
#                      }
#             }"""
#         expected ="""Error on line 10 col 13: <EOF>"""
#         self.assertTrue(TestParser.test(input,expected,287))

#     def test88(self):
#         input =  """
#         Class test {
#             main(a,b: Float) {
#                Var r, s: Int;
#                r = 2.0;
#                Var a, b: Array[Int, 5];
#                s = r * r * Self.myPI;
#                a[1] = s;
#             }
#          }"""
#         expected ="""successful"""
#         self.assertTrue(TestParser.test(input,expected,288))

#     def test89(self):
#         input =  """
#         Class test {
#             main(a,b: Float) {
#                Var r, s: Int;
#                r = 2.0 + -3;
#                Var a, b: Array[Int, 5] = Array[];
#                s = r * r * Self.myPI;
#                a[1] = s;
#             }
#          }"""
#         expected ="""Error on line 6 col 46: ["""
#         self.assertTrue(TestParser.test(input,expected,289))
        
#     def test90(self):
#         input =  """
#         Class test {
#             main(a,b: Float, Int) {
#                Var r, s: Int;
#                r = 2.0 * 13.e1;
#                Var a, b: Array[Int, 5];
#                s = r * r * Self.myPI;
#                a[1] = s;
#             }
#          }"""
#         expected ="""Error on line 3 col 27: ,"""
#         self.assertTrue(TestParser.test(input,expected,290))
        
#     def test91(self):
#         input="""
#             Class Yasuo{
               
#             }
#             Class Hasagi: Yasuo{
#                Hasagi(Q : Int){
#                    Self.Hattung();
#                }
#             }
#       """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 291))

#     def test92(self):
#         input="""
#             Class TestArr{
#                Var arr1 : Array[String, 1];
#                Var arr2 : Array[Int, 1];
#                Var arr4 : Array[Boolean, 1];
#                Var arr5 : Array[Array[Float,1], 4];
#             }
#       """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 292))
        
      
#     def test93(self):
#         input = """
#          Class Program{
#             main(){
#                Var a: Float = 3.2869745;
#                Var b: Int= 5;
#                Var c: Boolean= (a>b)==13>7;
#             }
#          }
#          """
#         expected = "Error on line 6 col 40: >"
#         self.assertTrue(TestParser.test(input, expected, 33))
        
#     def test94(self):
#         input="""
#             Class Abba{
#                $Retrld(){
#                    Self.Nothing();
#                }
#             }
#             Class Baad{
#                Print(){
#                   Var a: Int = A::$Retrld();
#                }
#             }
#       """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 294))

#     def test95(self):
#         input="""
#             Class Testhehe{
#                Var _: Array[Int, 1];
#                Var $1: Array[Array[Int, 10], 10];
#                Var $_1: Array[Array[Array[Int, 10], 10], 10];
#             }
#       """
#         expected = "successful"
#         self.assertTrue(TestParser.test(input, expected, 295))

#     def test96(self):
#         input="""
#             Class Test {
#                Var xyz : Int = 3+7-15*7/96;
#                $Test(a,b,c: Float) {
#                   out.println(test);
#                }
#             }"""
        
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input, expected, 296))

#     def test97(self):
#         input="""
#             Class Brain {
#                $My_brain() {
#             ## create an input stream ##
#                   Var input : Array[Int,4] = Array(1, 2, 3, 4);
#                   Var stream : InputStream = New InputStream(input);
#                   out.println(stream);
#             ## convert the input stream to byte array ##
#                   Var array : Array[Int,4] = stream.readAllBytes();
#                   out.println("Byte Array: " + Arrays.toString(array));
#                   stream.close();
#                }
#             }"""
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input, expected, 297))

#     def test98(self):
#         """test stmt  """
#         input="""
#             Class Main {
#                $main() {
#             ## create an input stream##
#                Var input : Array[Int,4] = Array(1, 2, 3, 4);
#                Var stream : InputStream = New InputStream(input);
#                out.println(stream);

#             ## create an output stream ##
#                Var output : ByteArrayOutputStream = New ByteArrayOutputStream();
#             ## create a byte array to store input stream ##
#                Var i: Int;
               
#              ## read all data from input stream to array ##
#                If ((i == stream.read(array, 0, array.length)) != -1) {
#                ## write all data from array to output ##
#                   output.write(array, 0, i);
#                }
#             ## convert the input stream to byte array ##
#                   Var array : Array[Int,4] = stream.readAllBytes();
#                   out.println( Arrays.toString(array));
#                   stream.close();
#                 }
#             }"""
        
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input, expected, 298))

#     def test99(self):
#         """test stmt  """
#         input="""
#             Class pattern {
#                $moi(a,bc,daw: Boolean) {  
#                   Var i,j : Int;
#                   Var n : Int =7;  
#                   out.println(Right);  
#                Foreach(i In 500 .. 700 By 2) {  
#                   Foreach(J In 500 .. 700 By 2) {  
#                      out.print();  
#                   }  
#                   out.println(aw);  
#                }  
#             } 
#             }"""
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input, expected, 299))

#     def test100(self):
#         input="""
#          Class DeleteMid {  
#          ##Represent a node of the doubly linked list##
#          }
         
#          Class Node{  
#             Var data:Int;
#             Var previous,next :Node;    
      
#             Constructor(datas:Int) {  
#                   Self.data = data;  
#             }  
#          }  
      
#          Class My{
#             Var size:Int = 0; 
#          ##Represent the head and tail of the doubly linked list  ##
#             Var head, tail :Node;    
            
#          ##addNode() will add a node to the list  ##
#             addNode(data:Int) {
#             ## Create a new node ##
#             Var newNode : Node = New Node(data);  
      
#             ##If list is empty  ##
#             If(head == null) {  
#                   ##Both head and tail will point to newNode  ##
#                      head =  newNode;  
#                      tail =  newNode; 
#                   ##head's previous will point to null## 
#                      head.previous = null;  
#                   ##tail's next will point to null, as it is the last node of the list  ##
#                      tail.next = null;  
#             }  
#             Else {  
#                   ##newNode will be added after tail such that tail's next will point to newNode  ##
#                      tail.next = newNode;  
#                   ##newNode's previous will point to tail  ##
#                      newNode.previous = tail;  
#                   ##newNode will become new tail  ##
#                      tail = newNode;  
#                   ##As it is last node, tail's next will point to null  ##
#                      tail.next = null;  
#             }  
#             ##Size will count the number of nodes present in the list ## 
#             size = size + 1;  
#          }  
      
#          ##deleteFromMid() will delete a node from middle of the list ## 
#          deleteFromMid() {  
#             ##Checks whether list is empty  ##
#             If(head == null) {  
#                   Return;  
#             }  
#             Else {  
#                   ##current will point to head  ##
#                   Var current : Node = head;
      
#                   ##Store the mid position of the list  ##
#                   Var mid: Int = (size+1)/2 ; 
      
#                   ##Iterate through list till current points to mid position  ##              
#                   Foreach(i In i .. mid By qq) {  
#                      current = current.next;   
#                   }   
      
#                   ##If middle node is head of the list  ##
#                   If(current == head) {  
#                      head = current.next;  
#                   }  
#                   ##If middle node is tail of the list  ##
#                   Elseif(current == tail) {  
#                      tail = tail.previous;  
#                   }  
#                   Else {  
#                      current.previous.next = current.next;  
#                      current.next.previous = current.previous;  
#                   }  
#                   ##Delete the middle node  ##
#                   current = null;  
#             }  
#             size = size - 1;   
#          }  
#         Bla(){
#             ##Node current will point to head  ##
#             Var current : Node = head;  
#             If(head == Null) {  
#                   out.println(empty);  
#                   Return;  
#             }  
#             If(current != Null) {  
#                   ##Prints each node by incrementing the pointer.  ##
#                   out.print(current.data );  
#                   current = current.next;  
#             }  
#             out.println();  
#          }  
      
#          main() {  
#             Var dList : DeleteMid = New DeleteMid();   
#             ##Add nodes to the list##  
#             dList.addNode(1);  
#             dList.addNode(2);  
#             dList.addNode(3);  
      
#             ##Printing original list  ##
#             out.println(Original_List);  
#             dList.display();  
#             If(dList.head != Null) {  
#                   dList.deleteFromMid();  
#                   ##Printing updated list  ##
#                   out.println(Updated_List);  
#                   dList.display();  
#             }  
#          }  
#       }   """
#         expected = """successful"""
#         self.assertTrue(TestParser.test(input, expected, 300))

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

   def test1(self):
      self.assertTrue(TestParser.test(
      """
      Class  Spider_man {
         Var Peter_1: Tobey = (a::$b).c;
      }
      """,
      "successful", 201))
   def test2(self):
      self.assertTrue(TestParser.test(
      """
      Class Spider_verse {
         Val Suits: String;
         Var name: String;
         Val num: Int;
      }
      """,
      "successful", 202))
   def test3(self):
      self.assertTrue(TestParser.test(
      """
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
      """,
      "successful", 203))
   def test4(self): 
      self.assertTrue(TestParser.test(
      """
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
      """,
      "successful", 204))
   
   def test5(self):
      self.assertTrue(TestParser.test(
      """
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
      """, 
      "successful", 205))
      
   def test6(self):
      self.assertTrue(TestParser.test(
      """
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
      """, 
      "successful", 206))
      
   def test7(self):
      self.assertTrue(TestParser.test(
      """
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
      """, 
      "successful", 207))
      
   def test8(self):
      self.assertTrue(TestParser.test(
      """
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
      """, 
      "successful", 208))
   
   def test9(self):
      self.assertTrue(TestParser.test(
      """
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
      """, 
      "successful", 209))   
   
   def test10(self):
      self.assertTrue(TestParser.test(
      """
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
      """, 
      "successful", 210))
      
   def test11(self):
      self.assertTrue(TestParser.test(
      """
      Class TestEmptyClass {
         
      }
      """,
      "successful", 211))
      
   def test12(self):
      self.assertTrue(TestParser.test(
      """
      Class Base {
         Var testFloat: Float = 0.00000E000000;
      }
      Class Derived {
         Var testObj: Base;
      }
      """,
      "successful", 212))

   def test13(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 213))
      
   def test14(self):
      self.assertTrue(TestParser.test(
      """
      Class testMathExpressions {
         main() {
            Val PI: Float = 3.1415924;
            Var radius: Float = 4.12;
            Var perimeter: Float = Self.PI * 2 * Self.radius;
            Var area: Float = Self.radius * Self.radius * Self.PI;
            Var test: Float = ((10 + 2) * 4 - 5) / 6; 
         }
      }
      """,
      "successful", 214))
         
   def test15(self):
      input = """
         Class testVar {
            test() {
               Val testArr: Array[Int, 0x4_12F_A216];
               Var testBool: Boolean;
               Val testString: String = "String to test";
            }
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 215))  
      
   def test16(self):
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
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 216))
        
   def test17(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 217))
      
   def test18(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 218))
      
   def test19(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 219))   
      
   def test20(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 220))
   
   def test21(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 221))
      
   def test22(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 222))
      
   def test23(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 223))
      
   def test24(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 224))    
      
   def test25(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 225)) 
      
   def test26(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 226))
      
   def test27(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 227))
      
   def test28(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 228))
      
   def test29(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 229))
      
   def test30(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 230))
      
   def test30(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 230))
      
   def test31(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 231))
      
   def test32(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 232))
      
   def test33(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 233))
      
   def test34(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 234))
      
   def test35(self):
      input = """
         Class testAlgorithms {
            Val $RUN: Int = 32;

            insertionSort(arr: Array[Int, 100]; left: Int; right: Int)
            {
               Foreach (i In (left + 1) .. right By 1)
               {
                  Var temp: Int = arr[i];
                  Var j: Int = i - 1;
                  while (j In (i - 1) .. left By -1) {
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
                  insertionSort(arr, i, Algorithms.min((i + Self::RUN - 1), (n - 1)));
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 235))
      
   # def test20(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
   #             Var multi_arr: Array[Array[Float, 5],5];
   #             Foreach (i In 1 .. 5){
   #                If(i != 3){
   #                   Continue;
   #                }
   #                Foreach(j In 1 .. 5){
   #                   multi_arr[i][j] = arr[j];
   #                }
   #             }
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 220))
      
   # def test21(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
   #             Var multi_arr: Array[Array[Array[Float, 5], 5],5];
   #             Foreach (i In 1 .. 5){
   #                Foreach(j In 2 .. 6 By j-1){
   #                   Foreach(z In 3 .. 7 By z-2){
   #                      multi_arr[i][j][z] = arr[z];
   #                   }
   #                }
   #             }
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 221))
      
   # def test22(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Val str1: String= "H";
   #             Val str2: String= "e";
   #             Val str3: String= "l";
   #             Val str4: String= "o";
   #             Val str5: String= "W";
   #             Val str6: String= "r";
   #             Val str7: String= "d";
   #             Val str8: String= str1 +. str2;
   #             Val str9: String= str8 +. str3;
   #             Val str10: String= str9 +. str3;
   #             Val str11: String= str10 +. str4;
   #             Val str12: String= str11 +. str5;
   #             Val HelloWorld: String= ((((((((str1 +. str2) +. str3) +. str3) +. str4) +. str5) +. str4) +. str3) +. str6) +. str7; 
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 222))   
      
   # def test23(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var a: Int= 3;
   #             Var b: Int= 5;
   #             Var c: Boolean= a>b;
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 223))
      
   # def test24(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var a: Int= 3;
   #             Var b: Int= 5;
   #             Var c: Boolean= a>b;
   #             Var d: Boolean= ((c==True) != False) == ((a<=3) == (b>=2));
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 224))
      
   # def test25(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var a: Int= 3;
   #             Var b: Int= 5;
   #             Var c: Boolean= a>b;
   #             Var d: Boolean= ((c==True) != False) == (((a<=3) != (b>=2)) && ((10<3) || (9>10)));
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 225))
      
   # def test26(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var a: Int= 10;
   #             Var b: Int= 2;
   #             Var sum: Float= a+b+10.+5.+5.e10-69.72;
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 226))
      
   # def test27(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var a: Int= 10;
   #             Var b: Int= 2;
   #             Var sum: Float= (((a % 5)/b)*b)*(b+2);
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 227))
      
   # def test28(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var a: Boolean= False;
   #             Var b: Boolean= !a;
   #             Var c: Boolean= !!a;
   #             Var d: Boolean= !!(a||b&&c);
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 228))
      
   # def test29(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var a: Float= .e10;
   #             Var b: Float= -a;
   #             Var c: Float= --a;
   #             Var d: Float= -(a+-c);
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 229))
      
   # def test30(self):
   #    input = """
   #       Class Program{
   #          main(){
   #             Var arr: Array[String, 100];
   #             Var arr_1: Array[String, 100];
   #             Foreach(i In 1 .. 100 By i<=10){
   #                arr[i]= i*10 + i%100;
   #             }
   #             Foreach(i In 1 .. 10){
   #                arr_1[i]= (arr[i] +. arr[i*10]) +. arr[i*10%100];
   #             }
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 230))
      
   # def test31(self):
   #    input = """
   #       Class Expr{
   #          Var BExp: BinExp;
   #          Constructor(op1: Int; op: String; op2: Int){
   #             Self.BExp= New BinExp(op1, op, op2);
   #          }
   #       }
   #       Class BinExp{
   #          Var op1: Int;
   #          Var op: String;
   #          Var op2: Int;
   #          Constructor(op1: Int; op: String; op2:Int){
   #             Self.op1= op1;
   #             Self.op= op;
   #             Self.op2= op2;
   #          }
   #       }
   #       Class Program{
   #          main(){
   #             Var expr: Exp= New Exp(1,"+",2);
   #             Var lhv_expr: Int= expr.BExp.op1;
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 231))
      
   # def test32(self):
   #    input = """
   #       Class Expr{
   #          Var BExp: BinExp;
   #          Constructor(op1: Int; op: String; op2: Int){
   #             Self.BExp= New BinExp(op1, op, op2);
   #          }
   #       }
   #       Class BinExp{
   #          Var op1: Int;
   #          Var op: String;
   #          Var op2: Int;
   #          Constructor(op1: Int; op: String; op2:Int){
   #             Self.op1= op1;
   #             Self.op= op;
   #             Self.op2= op2;
   #          }
   #       }
   #       Class Program{
   #          main(){
   #             Var expr: Exp= New Exp(1,"+",2);
   #             Var lhv_expr: Int= expr.BExp.op1;
   #             Var rhv_expr: Int= expr.BExp.op2;
   #             If(expr.BExp.op ==. "+"){
   #                Out.Print(lhv_expr + rhv_expr);
   #             }
   #             Elseif(expr.BExp.op ==. "-"){
   #                Out.Print(lhv_expr - rhv_expr);
   #             }
   #             Elseif(expr.BExp.op ==. "*"){
   #                Out.Print(lhv_expr * rhv_expr);
   #             }
   #             Elseif(expr.BExp.op ==. "/"){
   #                Out.Print(lhv_expr / rhv_expr);
   #             }
   #             Else{
   #                Out.Print("Error!");
   #             }
   #          }
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 232))
      
   # def test33(self):
   #    input = """
   #       Class Ex{
   #          Var a: Int;
   #          Var a,b: Int;
   #          Var a,b,c,d,e,f: Int;
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 233))
      
   # def test34(self):
   #    input = """
   #       Class Ex{
   #          Var a: Int= 1;
   #          Var a,b: Int= 1,2;
   #          Var a,b,c,d,e,f: Int= 1,2,3,4,5,6;
   #       }
   #       """
   #    expected = "successful"
   #    self.assertTrue(TestParser.test(input, expected, 234))
      
   def test35(self):
      input = """
         Class Ex{
            Var a: Int= 1+2*3;
            Var a,b: Int= 1/2,2*3;
            Var a,b,c,d,e,f: Int= 1+2,2-1,3*5,4*6,5/5,6%3;
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 235))
      
   def test36(self):
      input = """
         Class Ex{
            Var a: YS= New YS("Hasagi!");
            Var total_missQ, total_time_dead: Int= a.total_missQ, a.total_missQ+10;
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 236))
      
   def test37(self):
      input = """
         Class minion{
            Var attk: Int= 1;
         }
         Class Soldier{
            Var slave: minion= New minion();
         }
         Class King{
            Var slaves: Soldier= New Soldier();
         }
         Class Program{
            main(){
               Var K1: King= New King();
               K1_soldier= K1.slaves;
               K1_soldier_slave= K1.slaves.slave;
            }
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 237))
      
   def test38(self):
      input = """
         Class minion{
            Var $gender: String= "Female";
            Var attk: Int= 1;
         }
         Class Soldier{
            Var $gender: String= "Female";
            Var slave: minion= New minion();
         }
         Class King{
            Var slaves: Soldier= New Soldier();
         }
         Class Program{
            main(){
               Var K1: King= New King();
               Var K1_soldier_gender, K1_soldier_slave_gender: String;
               K1_soldier_gender= Soldier::$gender;
               K1_soldier_slave_gender= minion::$gender;
            }
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 238))
      
   def test39(self):
      input = """
         Class Maid{
            Var $gender: String= "Female";
            Var ID: Int;
            Var name: String;
            Constructor(ID: Int; name: String){
               Self.ID= ID;
               Self.name= name;
            }
         }
         Class Master{
            Var total_maids: Int= 0;
            Var maids: Array[Int, 1000];
            Constructor(total_maids: Int){
               If(total_maids > 1000){
                  Out.Print("Build more houses!");
               }
               Else{
                  Self.total_maids= total_maids;
               }
            }
            AddMaid2House(maid: Maid){
               Self.total_maids= total_maids + 1;
               Self.maids[Self.total_maids]= maid.ID;
            }
         }
         Class Program{
            main(){
               
            }
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 239))
      
   def test40(self):
      input = """
         Class Maid{
            Var $gender: String= "Female";
            Var ID: Int;
            Var name: String;
            Constructor(ID: Int; name: String){
               Self.ID= ID;
               Self.name= name;
            }
            getMaidName(){
               Return Self.name;
            }
         }
         Class Master{
            Var total_maids: Int= 0;
            Var maids: Array[Int, 1000];
            Constructor(total_maids: Int){
               If(total_maids > 1000){
                  Out.Print("Build more houses!");
               }
               Else{
                  Self.total_maids= total_maids;
               }
            }
            AddMaid2House(maid: Maid){
               Self.total_maids= total_maids + 1;
               Self.maids[Self.total_maids]= maid.ID;
            }
            PrintMaidsID(){
               Foreach(i In 1 .. Self.total_maids){
                  Out.Print(Self.maids[i]);
               }
            }
         }
         Class Program{
            main(){
               
            }
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 240))
      
   def test41(self):
      input = """
         Class CandidateMaids{
            Var ID: Int;
            Var age: Int;
            Var gender: String;
            Var name: String;
            Constructor(ID, age: Int; gender, name: String){
               Self.ID= ID;
               Self.gender= gender;
               Self.name= name;
            }
            getGender(){
               Return Self.gender;
            }
            getAge(){
               Return Self.age;
            }
            getID(){
               Return ID;
            }
         }
         Class Maid{
            Var $gender: String= "Female";
            Var ID: Int;
            Var age: Int;
            Var name: String;
            Constructor(ID: Int; name: String; age: Int){
               Self.ID= ID;
               Self.name= name;
               Self.age= age;
            }
            getMaidName(){
               Return Self.name;
            }
            getMaidAge(){
               Return Self.age;
            }
            getMaidID(){
               Return Self.ID;
            }
         }
         Class Master{
            Var total_maids: Int= 0;
            Var maids: Array[Int, 1000];
            Constructor(total_maids: Int){
               If(total_maids > 1000){
                  Out.Print("Build more houses!");
               }
               Else{
                  Self.total_maids= total_maids;
               }
            }
            AddMaid2House(ID: Int){
               Self.total_maids= total_maids + 1;
               Self.maids[Self.total_maids]= ID;
            }
            HireMaid(candidate_maid: CandidateMaids){
               If(candidate_maid.getGender ==. "Female"){
                  If(candidate_maid.getAge > 40){
                     Out.Print("You're Out!");
                  }
                  Else{
                     Self.AddMaid2House(candidate_maid.getID());
                     Out.Print("You're IN!");
                  }
               }
            }
            PrintMaidsID(){
               Foreach(i In 1 .. Self.total_maids){
                  Out.Print(Self.maids[i]);
               }
            }
         }
         Class Program{
            main(){
               
            }
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 241))
      
      
   def test42(self):
      input = """
         Class CandidateMaids{
            Var ID: Int;
            Var age: Int;
            Var gender: String;
            Var name: String;
            Constructor(ID, age: Int; gender, name: String){
               Self.ID= ID;
               Self.gender= gender;
               Self.name= name;
            }
            getGender(){
               Return Self.gender;
            }
            getAge(){
               Return Self.age;
            }
            getID(){
               Return ID;
            }
         }
         Class Maid{
            Var $gender: String= "Female";
            Var ID: Int;
            Var age: Int;
            Var name: String;
            Constructor(ID: Int; name: String; age: Int){
               Self.ID= ID;
               Self.name= name;
               Self.age= age;
            }
            getMaidName(){
               Return Self.name;
            }
            getMaidAge(){
               Return Self.age;
            }
            getMaidID(){
               Return Self.ID;
            }
         }
         Class Master{
            Var total_maids: Int= 0;
            Var maids: Array[Int, 1000];
            Constructor(total_maids: Int){
               If(total_maids > 1000){
                  Out.Print("Build more houses!");
               }
               Else{
                  Self.total_maids= total_maids;
               }
            }
            AddMaid2House(ID: Int){
               Self.total_maids= total_maids + 1;
               Self.maids[Self.total_maids]= ID;
            }
            HireMaid(candidate_maid: CandidateMaids){
               If(candidate_maid.getGender ==. "Female"){
                  If(candidate_maid.getAge > 40){
                     Out.Print("You're Out!");
                  }
                  Else{
                     Self.AddMaid2House(candidate_maid.getID());
                     Out.Print("You're IN!");
                  }
               }
            }
            PrintMaidsID(){
               Foreach(i In 1 .. Self.total_maids){
                  Out.Print(Self.maids[i]);
               }
            }
         }
         Class Program{
            main(){
               Var Hieu: Master= New Master(0);
               Var Nikonise: CandidateMaids= New CandidateMaids("1913341", 19, "Female", "Lauren Nikonise");
               Hieu.HireMaid(Nikonise);
            }
         }
         """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 242))
   
   def test43(self):
      input="""
            Class River{
               
            }
            Class Sea: River{
               
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 243))
      
   def test44(self):
      input="""
            Class River{
               Var rivers: Array[String, 100];
            }
            Class Sea{
               Var river: River= New River();
            }
            Class Program{
               main(){
                  Var _sea1: Sea= New Sea();
                  Var _river1_name: String= _sea1.river.rivers[1];
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 244))
      
   def test45(self):
      input="""
            Class Program{
               main(){
                  Var num1: Float= 1.111e10;
                  Var num2: Float= 1.222e10;
                  Val first: Int= 1;
                  Val last: Int= 100000;
                  Var arr: Array[Float, 1000];
                  Foreach(idx In first .. last By idx <= 1000){
                     num1= -num1;
                     num2= -num2;
                     arr[idx] = num1 + num2; 
                  }
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 245))
      
   def test46(self):
      input="""
            Class A{
               Var greeting: String= "Hello World!";
            }
            Class B{
               Var a: A= New A();
            }
            Class Program{
               main(){
                  Var b: B= New B();
                  b.a.greeting= "Deadline is like a wind. Always by my side!";
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 246))
      
   def test47(self):
      input="""
            Class A{
               PrintGreeting(){}
               $PrintHelloWorld(){}
            }
            Class B{
               Print(){
                  A::$PrintHelloWorld();
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 247))
      
   def test48(self):
      input="""
            Class A{
               $RetHelloWorld(){}
            }
            Class B{
               Print(){
                  Var a: String= A::$PrintHelloWorld();
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 248))
      
   def test49(self):
      input="""
            Class A{
               $RetHelloWorld(){}
            }
            Class B{
               Print(){
                  Var a: String= A::$PrintHelloWorld();
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 249))
      
   def test50(self):
      input="""
            Class C{
               Testing_Str(str1, str2, str3, str4: String){
                  str1= "Xin chao";
                  str2= "Cac bann";
                  str3= "Dung de";
                  str4= "y toi minh";
                  Var str: String= (str1 +. str2) +. (str3 +. str4);
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 250))
      
   def test51(self):
      input="""
            Class C{
               Testing_Str(str1, str2, str3, str4: String){
                  str1= "Xin chao";
                  str2= "Cac bann";
                  str3= "Dung de";
                  str4= "y toi minh";
                  Var str: String= ((str1 +. str2) +. str3) +. str4;
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 251))
      
   def test52(self):
      input="""
            Class C{
               Testing_Str(str1, str2, str3, str4: String){
                  str1= "Xin chao";
                  str2= "Cac bann";
                  str3= "Dung de";
                  str4= "y toi minh";
                  Var str: String= str1 +. (str2 +. (str3 +. str4));
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 252))

   def test53(self):
      input="""
            Class C{
               Testing_Boolean(str1, str2, str3, str4: String){
                  Var bool1: Boolean= True;
                  Var bool2: Boolean= False;
                  Var bool3: Boolean= True;
                  Var bool4: Boolean= False;
                  Var bool5: Boolean= False;
                  Var res: Boolean= !(bool1 == bool2);
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 253))
      
   def test54(self):
      input="""
            Class C{
               Testing_Boolean(str1, str2, str3, str4: String){
                  Var bool1: Boolean= True;
                  Var bool2: Boolean= False;
                  Var bool3: Boolean= True;
                  Var bool4: Boolean= False;
                  Var bool5: Boolean= False;
                  Var res: Boolean= !(!bool1 == !bool2);
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 254))
      
   def test55(self):
      input="""
            Class C{
               Testing_Boolean(str1, str2, str3, str4: String){
                  Var bool1: Boolean= True;
                  Var bool2: Boolean= False;
                  Var bool3: Boolean= True;
                  Var bool4: Boolean= False;
                  Var bool5: Boolean= False;
                  Var res: Boolean= !((!bool1 != bool4) == (!bool2 != bool3));
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 255))
      
   def test55(self):
      input="""
            Class C{
               Testing_Relational(str1, str2, str3, str4: String){
                  Var arr: Array[Int, 10]= Array(1,2,3,4,5,6,7,8,9,0);
                  Foreach(idx In 1 .. 10){
                     If(idx <=7){
                        If((arr[i] == arr[i+1])>arr[i+2]){
                           Return "Hello Worlds!";
                        }
                     }
                  }
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 255))
   
   def test56(self):
      input="""
            Class Test{
               Var _aaa: String;
               Var _bbb: Int;
               Var _ccc: Float;
               Var _ddd: Boolean;
               Var _eee: Array[String, 10];
               Var _fff: Array[Int, 10];
               Var _ggg: Array[Float, 10];
               Var _hhh: Array[Boolean, 10];
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 256))
      
   def test57(self):
      input="""
            Class Test{
               Val _aaa: String;
               Val _bbb: Int;
               Val _ccc: Float;
               Val _ddd: Boolean;
               Val _eee: Array[String, 10];
               Val _fff: Array[Int, 10];
               Val _ggg: Array[Float, 10];
               Val _hhh: Array[Boolean, 10];
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 257))
      
   def test58(self):
      input="""
            Class Test{
               Var _: Array[Int, 10];
               Var __: Array[Array[Int, 10], 10];
               Var ___: Array[Array[Array[Int, 10], 10], 10];
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 258))
      
   def test59(self):
      input="""
            Class Test{
               Var $1: Float;
               Var $2: Float= 10.;
               Var $3, $4: Float= 10., 2.;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 259))
      
   def test60(self):
      input="""
            Class Test{
               Var $1: Float;
               Var $2: Float= 10.;
               Var $3, $4: Float= 10., 2.;
               Var $5, $6: Float= .10e10, .e0;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 260))
      
   def test61(self):
      input="""
            Class Test{
               Var $5, $6: Float= 3.10e10, 3.0e0;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 261))
      
   def test62(self):
      input="""
            Class Test{
               ## Xin chao cac ban ! ##
               ## Day la comment ! ##
               ## Chinh vi the nen dung co bat minh ##
               ## Minh cam on :3 ! ##
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 262))
      
   def test63(self):
      input="""
            Class Test{
               Var attr1: Int;
               Var attr2: Int;
               Test_attr(){
                  Return Self.attr1 + Self.attr2;
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 263))
      
   def test64(self):
      input="""
            Class Test{
               Var attr1: Int;
               Var attr2: Int;
               Test_attr(){
                  Return attr1 + attr2;
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 264))
      
   def test65(self):
      input="""
            Class Test{
               Var attr1: Int;
               Var attr2: Int;
               Print(){
                  Out.Print("Xin chao!");
               }
               Test_method(){
                  Self.Print();
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 265))
      
   def test66(self):
      input="""
            Class Test{
               Val qq: Int= 10;
               Val bt: Float=15.;
               Var res: Float= bt%qq*bt-qq+dd;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 266))
      
   def test67(self):
      input="""
            Class Test{
               Val qq: Int= 10;
               Val bt: Float=15.;
               Var res: Float= bt%qq*bt-qq+dd;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 267))
      
   def test68(self):
      input="""
            Class A{
               Val $static1: Float;
               Val $static2: Int;
            }
            Class Test{
               Var test1: Int= A::$static2;
               Var test2: Float= A::$static1;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 268))
      
   def test69(self):
      input="""
            Class A{
               Val $static1: Int;
               Val $static2: Int;
            }
            Class Test{
               Var test1, test2: Int= A::$static2, A::$static1;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 269))
      
   def test70(self):
      input="""
            Class Test{
               Val qq: Int= 10;
               Val bt: Float=15.;
               Var res: Float= (((bt%qq)*bt)-qq)+dd;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 270))
      
   def test71(self):
      input="""
            Class Test{
               Var a: Int;
               a=10;
            }
      """
      expected = "Error on line 4 col 16: ="
      self.assertTrue(TestParser.test(input, expected, 271))
      
   def test72(self):
      input="""
            Class Test{
               Var a: Int;
               Var c: Int= a;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 272))
      
   def test72(self):
      input="""
            Class Test{
               Var a: Int;
               Var c: Int= a;
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 272))
   
   def test73(self):
      input="""
            Class Test{
               Var $a: Int= 10;
               Var c: Int= $a;
            }
      """
      expected = "Error on line 4 col 27: $a"
      self.assertTrue(TestParser.test(input, expected, 273))
      
   def test74(self):
      input="""
            Class Test{
               Var arr : Array[String, 0];
            }
      """
      expected = "Error on line 3 col 39: 0"
      self.assertTrue(TestParser.test(input, expected, 274))
      
   def test75(self):
      input="""
            Class Test{
               Var arr : Array[String, 0x0];
            }
      """
      expected = "Error on line 3 col 39: 0x0"
      self.assertTrue(TestParser.test(input, expected, 275))
      
      
   def test76(self):
      input="""
            Class Test{
               Var arr : Array[String, 0X0];
            }
      """
      expected = "Error on line 3 col 39: 0X0"
      self.assertTrue(TestParser.test(input, expected, 276))
      
      
   def test77(self):
      input="""
            Class Test{
               Var arr : Array[String, 0b0];
            }
      """
      expected = "Error on line 3 col 39: 0b0"
      self.assertTrue(TestParser.test(input, expected, 277))
      
      
   def test78(self):
      input="""
            Class Test{
               Var arr : Array[String, 0B0];
            }
      """
      expected = "Error on line 3 col 39: 0B0"
      self.assertTrue(TestParser.test(input, expected, 278))
      
   def test79(self):
      input="""
            Class Test{
               Var arr : Array[String, 00];
            }
      """
      expected = "Error on line 3 col 39: 00"
      self.assertTrue(TestParser.test(input, expected, 279))
      
   def test79(self):
      input="""
            Class Test{
               Var arr : Array[String, 00];
            }
      """
      expected = "Error on line 3 col 39: 00"
      self.assertTrue(TestParser.test(input, expected, 279))
      
   def test80(self):
      input="""
            Class Test{
               Var arr : Array[String, 1];
               Var arr : Array[Int, 1];
               Var arr : Array[Float, 1];
               Var arr : Array[Boolean, 1];
               Var arr : Array[Array[Int,1], 1];
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 280))
      
   def test81(self):
      input="""
            Class Test{
               Var arr : Array[Class_A, 1];
            }
      """
      expected = "Error on line 3 col 31: Class_A"
      self.assertTrue(TestParser.test(input, expected, 281))
      
   def test82(self):
      input="""
            Class Test{
               Var arr : Array[1, 1];
            }
      """
      expected = "Error on line 3 col 31: 1"
      self.assertTrue(TestParser.test(input, expected, 282))
      
   def test83(self):
      input="""
            Class Test{
               Var arr : Array[Int, 1];
               Var idx1: Int = arr[1];
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 283))
      
   def test84(self):
      input="""
            Class Test{
               Var arr : Array[Int, 1];
               Var idx1: Int = arr[0+1];
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 284))
      
   def test85(self):
      input="""
            Class Test{
               Method1(){
                  
               }
               Test(){
                  Method1();
               }
            }
      """
      expected = "Error on line 7 col 25: ("
      self.assertTrue(TestParser.test(input, expected, 285))
      
   def test86(self):
      input="""
            Class Test{
               $Method1(){
                  
               }
               Test(){
                  $Method1();
               }
            }
      """
      expected = "Error on line 7 col 18: $Method1"
      self.assertTrue(TestParser.test(input, expected, 286))
      
   def test87(self):
      input="""
            Class Test{
               $Method1(){
                  
               }
               Test(){
                  Self.$Method1();
               }
            }
      """
      expected = "Error on line 7 col 23: $Method1"
      self.assertTrue(TestParser.test(input, expected, 287))
      
   def test88(self):
      input="""
            Class Test{
               Method1(){
                  
               }
               Test(){
                  Self::Method1();
               }
            }
      """
      expected = "Error on line 7 col 22: ::"
      self.assertTrue(TestParser.test(input, expected, 288))
      
   def test89(self):
      input="""
            Class Test{
               Var ins: Int;
               Var $static: Int;
               Test(){
                  Var a: Int= ins;
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 289))
      
   def test90(self):
      input="""
            Class Test{
               Var ins: Int;
               Var $static: Int;
               Test(){
                  Var a: Int= ins;
                  Var b: Int= Self.$static;
               }
            }
      """
      expected = "Error on line 7 col 35: $static"
      self.assertTrue(TestParser.test(input, expected, 290))
      
   def test91(self):
      input="""
            Class Test{
               Var ins: Int;
               Var $static: Int;
               
               Test(){
                  Var a: Int= Self::ins;
                  Var b: Int= Self::$static;
               }
            }
      """
      expected = "Error on line 7 col 34: ::"
      self.assertTrue(TestParser.test(input, expected, 291))
      
   def test92(self):
      input="""
            ## Day la test so 92 !!!!! ##
            Class Test{
               Class test1{
                  
               }
               
               Test(){
                  
               }
            }
      """
      expected = "Error on line 4 col 15: Class"
      self.assertTrue(TestParser.test(input, expected, 292))
      
   def test93(self):
      input="""
            ## Day la test so 93 !!!!! ##
            Class Test{
               Test(){
                  Var int1: Int= 12_2_3_4;
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 293))
      
   def test94(self):
      input="""
            ## Day la test so 94 !!!!! ##
            Class Test{
               Test(){
                  Var float1: Float= 12_2_3_4.;
                  Var float2: Float= 12_2_3_4.00000;
                  Var float3: Float= 12_2_3_4.e0;
                  Var float4: Float= 12_2_3_4.e1100011;
                  Var float5: Float= .09e10;
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 294))
      
   def test95(self):
      input="""
            ## Day la test so 95 !!!!! ##
            Class Test{
               Test(){
                  Var a, b, c, d: Int= 1,2,3,4;
                  Var float1: Array[Array[Array[Array[Float, 1], 1], 1], 10];
                  idx1 = float1[a][b][c][d]; 
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 295))
      
   def test96(self):
      input="""
            ## Day la test so 96 !!!!! ##
            Class Test{
               Test(){
                  Return ;
                  Return 1+2;
                  Return New Test();
                  Return New FloatLit(op1, op, op2);
               }
            }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 296))
      
   def test97(self):
      input="""
            ## Day la test so 97 !!!!! ##
            Class Test{
               Test(){
                  Var ;
               }
            }
      """
      expected = "Error on line 5 col 22: ;"
      self.assertTrue(TestParser.test(input, expected, 297))
      
   def test98(self):
      input="""
            Var a: Int= 10000000;
      """
      expected = "Error on line 2 col 12: Var"
      self.assertTrue(TestParser.test(input, expected, 298))
      
   def test99(self):
      input="""
            Class A{
               
            };
      """
      expected = "Error on line 4 col 13: ;"
      self.assertTrue(TestParser.test(input, expected, 299))
      
   def test100(self):
      input="""
            Class A{
               Foreach(i In 1 .. 100 By i<=7){
                  Out.Print(i);
               }
            }
      """
      expected = "Error on line 3 col 15: Foreach"
      self.assertTrue(TestParser.test(input, expected, 300))
