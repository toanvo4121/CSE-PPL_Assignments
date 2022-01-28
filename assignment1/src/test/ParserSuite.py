# import unittest
# from TestUtils import TestParser

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 203))

#     def test4(self):
#         input = """
#             Class Program {
#                 Var $a: Int = 5;
#                 main() {
#                     Val a_b : Float = 7.35e-45;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 204))           

#     def test5(self):
#         input = """
#         	Class Main {
#   				$main($a:Int) {
#     				System_out.println(Hello_World);
#   				}
# 			}"""
#         expect = "Error on line 3 col 12: $a"
#         self.assertTrue(TestParser.test(input,expect,205))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,206))

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,207))

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,208))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,209))

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 210))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 211))
    
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 212))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 213))
    
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,214))
        
        
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
#         expect = "Error on line 9 col 22: Int"
#         self.assertTrue(TestParser.test(input,expect,215))
        
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
#         expect = "Error on line 15 col 36: =="
#         self.assertTrue(TestParser.test(input,expect,216))
        
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
#         expect = "Error on line 10 col 37: ,"
#         self.assertTrue(TestParser.test(input,expect,217))

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,218))

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
#         expect = "Error on line 8 col 16: Var"
#         self.assertTrue(TestParser.test(input,expect,219))
        
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
#         expect = "Error on line 9 col 44: )"
#         self.assertTrue(TestParser.test(input,expect,220))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,221))
        
        
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
#         expect = "Error on line 17 col 29: String"
#         self.assertTrue(TestParser.test(input,expect,222))

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
#         expect = "Error on line 14 col 32: ("
#         self.assertTrue(TestParser.test(input,expect,223))
        
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
#         expect = "Error on line 7 col 27: ["
#         self.assertTrue(TestParser.test(input,expect,224))
        
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
#         expect = "Error on line 9 col 23: Continue"
#         self.assertTrue(TestParser.test(input,expect,225))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,226))
        
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
#         expect = "Error on line 3 col 23: ::"
#         self.assertTrue(TestParser.test(input,expect,227))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,228)) 
        
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
#         expect = "Error on line 9 col 31: ("
#         self.assertTrue(TestParser.test(input,expect,229))
        
#     def test30(self):
#         input = """
#         Class Holi2 {
#             Tree(input : String) {  
#                 nodeQueue.add(root);
#                 Return root = 3;
#             }
#         }"""
#         expect = "Error on line 5 col 28: ="
#         self.assertTrue(TestParser.test(input,expect,230))
        
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
#         expect = "Error on line 7 col 54: =="
#         self.assertTrue(TestParser.test(input,expect,231))
        
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
#         expect = "Error on line 7 col 58: =="
#         self.assertTrue(TestParser.test(input,expect,232))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,233))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,234))

#     def test35(self):
#         input = """
#         Class Main {
#             main(Hol: String) {
#                 Var input : Scanner  = New Scanner (System.in);
#                 System.out.print(Inpu);
#                 Var num1, num2 : Int  = input.nextInt(), input.nextInt() , 37;
#                 System.out.print(Input);
#                 Var sum : Int  = num1 + num2;
#                 System.out.println(sum);
#             }
#         }"""
#         expect = "Error on line 6 col 73: ,"
#         self.assertTrue(TestParser.test(input,expect,235))
        
#     def test36(self):
#         input = """
#         Class Main {
#             main(Hol: String) {
#                 Var num2 : Int  = input.nextInt();
#                 System.out.println();
#             }
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,236))
        
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
#         expect = "Error on line 20 col 25: =="
#         self.assertTrue(TestParser.test(input,expect,237))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,238))
    
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
#         expect = "Error on line 5 col 16: If"
#         self.assertTrue(TestParser.test(input,expect,239))
        
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
#         expect = "Error on line 8 col 22: ("
#         self.assertTrue(TestParser.test(input,expect,240))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,241))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,242))
        
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
#         expect = "Error on line 8 col 37: ("
#         self.assertTrue(TestParser.test(input,expect,243))
        
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
#         expect = "Error on line 6 col 39: Scanner"
#         self.assertTrue(TestParser.test(input,expect,244))
        
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
#         expect = "Error on line 4 col 35: <="
#         self.assertTrue(TestParser.test(input,expect,245))


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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,246))
        
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
#         expect = "Error on line 3 col 29: ,"
#         self.assertTrue(TestParser.test(input,expect,247))
        
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
#         expect = "Error on line 5 col 42: ("
#         self.assertTrue(TestParser.test(input,expect,248))
        
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
#         expect = "Error on line 19 col 23: Math"
#         self.assertTrue(TestParser.test(input,expect,249))

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,250))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,251))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,252))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,253))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,254))

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
#         expect = "Error on line 5 col 68: ;"
#         self.assertTrue(TestParser.test(input,expect,255))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,256))
        
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
#         expect = "Error on line 8 col 20: !="
#         self.assertTrue(TestParser.test(input,expect,257))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,258))
        
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
#         expect = "Error on line 5 col 40: Continue"
#         self.assertTrue(TestParser.test(input,expect,259))
        
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
#         expect = "Error on line 4 col 24: in"
#         self.assertTrue(TestParser.test(input,expect,260))
        
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
#         expect = "Error on line 9 col 41: ("
#         self.assertTrue(TestParser.test(input,expect,261))
        
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
#         expect = "Error on line 13 col 48: =="
#         self.assertTrue(TestParser.test(input,expect,262))


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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,263))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,264))
        
#     def test65(self):
#         input = """
#         Class Test65 {
#             main(Bran : Float){
#                 System.out.println(main_string.substring(0, 7) + word + main_string.substring(6));
# 	        }       
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,265))

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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,266))
        
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
#         expect = "Error on line 7 col 20: System"
#         self.assertTrue(TestParser.test(input,expect,267))
        
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
#         expect = "Error on line 6 col 16: Else"
#         self.assertTrue(TestParser.test(input,expect,268)) 
        
#     def test69(self):
#         """Simple program"""
#         input = """
#         class Test69 {
#             Bro69(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, -20, 0), Array(5, -50, 10), Array(array1[2], array2[2], array1[2]);	 
#             }
#         }
# """
#         expect = "Error on line 2 col 8: class"
#         self.assertTrue(TestParser.test(input,expect,269))
        
#     def test70(self):
#         """Simple program"""
#         input = """
#         Class Test70 {
#             Bro70(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, -20, 0), Array(5, -50, 10), Array(array1[1], array2[2], array1[2]);	 
#             }
#         }
# """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,270))
        
#     def test71(self):
#         input = """
#         Class Test71 {
#             Bro71(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, 20, 0), Array(5, 50, 10), Array(array1[2], array2[2], array1[2]);	 
#             }
#         }
# """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,271))
        
#     def test72(self):
#         input = """
#         Class Test72 {
#             Bro71(Bro : Int){
#                 Var array1,array2,array_new : Array[Int,3] = Array(50, 20, 0), Array(5, 50, 10), Array(0,2,2);	   
#             }   
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,272))

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
#         expect = "Error on line 6 col 62: ;"
#         self.assertTrue(TestParser.test(input,expect,273))
        
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
#         expect = "Error on line 12 col 13: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,274))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,275))
        
#     def test76(self):
#         """test stmt  """
#         input = """
#             Class Main {
#                $main(args : Array[Int,2]) {
#                   out.println(Hello bae);
#                }
#             }"""
#         expect = """Error on line 4 col 36: bae"""
#         self.assertTrue(TestParser.test(input,expect,276))
        
#     def test77(self):
#         input = """
#             Class Main2 {
#                main(args : Array[Int,2]) {
#                   out.println(Hello + bae);
#                }
#             }"""
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect,277))
        
#     def test78(self):
#         input = """
#             Class Main2 {
#                main(args : Array[Int,2]) {
#                   out.println();
#                }
#             }"""
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect,278))

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
#         expect ="""successful"""
#         self.assertTrue(TestParser.test(input,expect,279))
        
#     def test80(self):
#         input = """
#             Class Program {
#                main(args : Array[Int,2]) {
#                   out.println(numbers);
#                   Var first, second :Int = 10, 20;
#                   out.println(first ++ second);

#                ## add two numbers ##
#                   Var sum : Int = +;
#                   out.println( sum);
#                }
#             }"""
#         expect ="""Error on line 6 col 37: +"""
#         self.assertTrue(TestParser.test(input,expect,280))
        
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
#         expect ="""Error on line 11 col 23: ;"""
#         self.assertTrue(TestParser.test(input,expect,281))


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
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect,282))
        
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
#         expect = """Error on line 6 col 34: &&"""
#         self.assertTrue(TestParser.test(input,expect,283))

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
#         expect = """Error on line 6 col 34: ||"""
#         self.assertTrue(TestParser.test(input,expect,284))
        
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
#         expect ="""successful"""
#         self.assertTrue(TestParser.test(input,expect,285))
        
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
#         expect ="""Error on line 3 col 44: &&"""
#         self.assertTrue(TestParser.test(input,expect,286))

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
#         expect ="""Error on line 10 col 13: <EOF>"""
#         self.assertTrue(TestParser.test(input,expect,287))

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
#         expect ="""successful"""
#         self.assertTrue(TestParser.test(input,expect,288))

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
#         expect ="""Error on line 6 col 46: ["""
#         self.assertTrue(TestParser.test(input,expect,289))
        
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
#         expect ="""Error on line 3 col 27: ,"""
#         self.assertTrue(TestParser.test(input,expect,290))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 291))

#     def test92(self):
#         input="""
#             Class TestArr{
#                Var arr1 : Array[String, 1];
#                Var arr2 : Array[Int, 1];
#                Var arr4 : Array[Boolean, 1];
#                Var arr5 : Array[Array[Float,1], 4];
#             }
#       """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 292))
        
      
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
#         expect = "Error on line 6 col 40: >"
#         self.assertTrue(TestParser.test(input, expect, 33))
        
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
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 294))

#     def test95(self):
#         input="""
#             Class Testhehe{
#                Var _: Array[Int, 1];
#                Var $1: Array[Array[Int, 10], 10];
#                Var $_1: Array[Array[Array[Int, 10], 10], 10];
#             }
#       """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 295))

#     def test96(self):
#         input="""
#             Class Test {
#                Var xyz : Int = 3+7-15*7/96;
#                $Test(a,b,c: Float) {
#                   out.println(test);
#                }
#             }"""
        
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 296))

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
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 297))

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
        
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 298))

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
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 299))

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
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 300))

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
      "successful", 213))
      
   def test14(self):
      input = """
         Class Program{
            main(){
               Var expr: Int= 1 * 2;
               Var expr1: Float= 1. * 3.123;
               Var expr2: Float= 1 / 2.1;
               Var expr3: Float= 1 % 2.1;
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 214))
         
   def test15(self):
      input = """
         Class Program{
            main(){
               Var a:Boolean= True;
               Var b,c:Boolean= False, True;
               If((b == c) == a){
                  
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 215))  
      
   def test16(self):
      input = """
         Class Program{
            main(){
               Var a:Boolean= True;
               Var b,c:Boolean= False, True;
               Var d: Boolean= b&&c&&a;
               If(d){
                  Var e: Boolean= d&&a||c&&c+d;
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 216))
      
   def test17(self):
      input = """
         Class Program{
            main(){
               Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
               Foreach (i In 1 .. 5){
                  Out.Print(arr[i]);
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 217))   
      
   def test18(self):
      input = """
         Class Program{
            main(){
               Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
               Var multi_arr: Array[Array[Float, 5],5];
               Foreach (i In 1 .. 5){
                  multi_arr[i][i]= arr[i];
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 218))
   
   def test19(self):
      input = """
         Class Program{
            main(){
               Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
               Var multi_arr: Array[Array[Float, 5],5];
               Foreach (i In 1 .. 5){
                  Foreach(j In 1 .. 5){
                     multi_arr[i][j] = arr[j];
                  }
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 219))
      
   def test20(self):
      input = """
         Class Program{
            main(){
               Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
               Var multi_arr: Array[Array[Float, 5],5];
               Foreach (i In 1 .. 5){
                  Foreach(j In 1 .. 5){
                     multi_arr[i][j] = arr[j];
                  }
                  If(i == 3){
                     Break;
                  }
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 220))    
      
   def test20(self):
      input = """
         Class Program{
            main(){
               Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
               Var multi_arr: Array[Array[Float, 5],5];
               Foreach (i In 1 .. 5){
                  If(i != 3){
                     Continue;
                  }
                  Foreach(j In 1 .. 5){
                     multi_arr[i][j] = arr[j];
                  }
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 220))
      
   def test21(self):
      input = """
         Class Program{
            main(){
               Var arr: Array[Float, 5]= Array(1. , 2. , 3. , 4. , 5.);
               Var multi_arr: Array[Array[Array[Float, 5], 5],5];
               Foreach (i In 1 .. 5){
                  Foreach(j In 2 .. 6 By j-1){
                     Foreach(z In 3 .. 7 By z-2){
                        multi_arr[i][j][z] = arr[z];
                     }
                  }
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 221))
      
   def test22(self):
      input = """
         Class Program{
            main(){
               Val str1: String= "H";
               Val str2: String= "e";
               Val str3: String= "l";
               Val str4: String= "o";
               Val str5: String= "W";
               Val str6: String= "r";
               Val str7: String= "d";
               Val str8: String= str1 +. str2;
               Val str9: String= str8 +. str3;
               Val str10: String= str9 +. str3;
               Val str11: String= str10 +. str4;
               Val str12: String= str11 +. str5;
               Val HelloWorld: String= ((((((((str1 +. str2) +. str3) +. str3) +. str4) +. str5) +. str4) +. str3) +. str6) +. str7; 
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 222))   
      
   def test23(self):
      input = """
         Class Program{
            main(){
               Var a: Int= 3;
               Var b: Int= 5;
               Var c: Boolean= a>b;
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 223))
      
   def test24(self):
      input = """
         Class Program{
            main(){
               Var a: Int= 3;
               Var b: Int= 5;
               Var c: Boolean= a>b;
               Var d: Boolean= ((c==True) != False) == ((a<=3) == (b>=2));
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 224))
      
   def test25(self):
      input = """
         Class Program{
            main(){
               Var a: Int= 3;
               Var b: Int= 5;
               Var c: Boolean= a>b;
               Var d: Boolean= ((c==True) != False) == (((a<=3) != (b>=2)) && ((10<3) || (9>10)));
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 225))
      
   def test26(self):
      input = """
         Class Program{
            main(){
               Var a: Int= 10;
               Var b: Int= 2;
               Var sum: Float= a+b+10.+5.+5.e10-69.72;
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 226))
      
   def test27(self):
      input = """
         Class Program{
            main(){
               Var a: Int= 10;
               Var b: Int= 2;
               Var sum: Float= (((a % 5)/b)*b)*(b+2);
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 227))
      
   def test28(self):
      input = """
         Class Program{
            main(){
               Var a: Boolean= False;
               Var b: Boolean= !a;
               Var c: Boolean= !!a;
               Var d: Boolean= !!(a||b&&c);
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 228))
      
   def test29(self):
      input = """
         Class Program{
            main(){
               Var a: Float= .e10;
               Var b: Float= -a;
               Var c: Float= --a;
               Var d: Float= -(a+-c);
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 229))
      
   def test30(self):
      input = """
         Class Program{
            main(){
               Var arr: Array[String, 100];
               Var arr_1: Array[String, 100];
               Foreach(i In 1 .. 100 By i<=10){
                  arr[i]= i*10 + i%100;
               }
               Foreach(i In 1 .. 10){
                  arr_1[i]= (arr[i] +. arr[i*10]) +. arr[i*10%100];
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 230))
      
   def test31(self):
      input = """
         Class Expr{
            Var BExp: BinExp;
            Constructor(op1: Int; op: String; op2: Int){
               Self.BExp= New BinExp(op1, op, op2);
            }
         }
         Class BinExp{
            Var op1: Int;
            Var op: String;
            Var op2: Int;
            Constructor(op1: Int; op: String; op2:Int){
               Self.op1= op1;
               Self.op= op;
               Self.op2= op2;
            }
         }
         Class Program{
            main(){
               Var expr: Exp= New Exp(1,"+",2);
               Var lhv_expr: Int= expr.BExp.op1;
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 231))
      
   def test32(self):
      input = """
         Class Expr{
            Var BExp: BinExp;
            Constructor(op1: Int; op: String; op2: Int){
               Self.BExp= New BinExp(op1, op, op2);
            }
         }
         Class BinExp{
            Var op1: Int;
            Var op: String;
            Var op2: Int;
            Constructor(op1: Int; op: String; op2:Int){
               Self.op1= op1;
               Self.op= op;
               Self.op2= op2;
            }
         }
         Class Program{
            main(){
               Var expr: Exp= New Exp(1,"+",2);
               Var lhv_expr: Int= expr.BExp.op1;
               Var rhv_expr: Int= expr.BExp.op2;
               If(expr.BExp.op ==. "+"){
                  Out.Print(lhv_expr + rhv_expr);
               }
               Elseif(expr.BExp.op ==. "-"){
                  Out.Print(lhv_expr - rhv_expr);
               }
               Elseif(expr.BExp.op ==. "*"){
                  Out.Print(lhv_expr * rhv_expr);
               }
               Elseif(expr.BExp.op ==. "/"){
                  Out.Print(lhv_expr / rhv_expr);
               }
               Else{
                  Out.Print("Error!");
               }
            }
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 232))
      
   def test33(self):
      input = """
         Class Ex{
            Var a: Int;
            Var a,b: Int;
            Var a,b,c,d,e,f: Int;
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 233))
      
   def test34(self):
      input = """
         Class Ex{
            Var a: Int= 1;
            Var a,b: Int= 1,2;
            Var a,b,c,d,e,f: Int= 1,2,3,4,5,6;
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 234))
      
   def test35(self):
      input = """
         Class Ex{
            Var a: Int= 1+2*3;
            Var a,b: Int= 1/2,2*3;
            Var a,b,c,d,e,f: Int= 1+2,2-1,3*5,4*6,5/5,6%3;
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 235))
      
   def test36(self):
      input = """
         Class Ex{
            Var a: YS= New YS("Hasagi!");
            Var total_missQ, total_time_dead: Int= a.total_missQ, a.total_missQ+10;
         }
         """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 236))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 237))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 238))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 239))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 240))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 241))
      
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 242))
   
   def test43(self):
      input="""
            Class River{
               
            }
            Class Sea: River{
               
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 243))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 244))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 245))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 246))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 247))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 248))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 249))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 250))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 251))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 252))

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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 253))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 254))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 255))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 255))
   
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 256))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 257))
      
   def test58(self):
      input="""
            Class Test{
               Var _: Array[Int, 10];
               Var __: Array[Array[Int, 10], 10];
               Var ___: Array[Array[Array[Int, 10], 10], 10];
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 258))
      
   def test59(self):
      input="""
            Class Test{
               Var $1: Float;
               Var $2: Float= 10.;
               Var $3, $4: Float= 10., 2.;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 259))
      
   def test60(self):
      input="""
            Class Test{
               Var $1: Float;
               Var $2: Float= 10.;
               Var $3, $4: Float= 10., 2.;
               Var $5, $6: Float= .10e10, .e0;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 260))
      
   def test61(self):
      input="""
            Class Test{
               Var $5, $6: Float= 3.10e10, 3.0e0;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 261))
      
   def test62(self):
      input="""
            Class Test{
               ## Xin chao cac ban ! ##
               ## Day la comment ! ##
               ## Chinh vi the nen dung co bat minh ##
               ## Minh cam on :3 ! ##
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 262))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 263))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 264))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 265))
      
   def test66(self):
      input="""
            Class Test{
               Val qq: Int= 10;
               Val bt: Float=15.;
               Var res: Float= bt%qq*bt-qq+dd;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 266))
      
   def test67(self):
      input="""
            Class Test{
               Val qq: Int= 10;
               Val bt: Float=15.;
               Var res: Float= bt%qq*bt-qq+dd;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 267))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 268))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 269))
      
   def test70(self):
      input="""
            Class Test{
               Val qq: Int= 10;
               Val bt: Float=15.;
               Var res: Float= (((bt%qq)*bt)-qq)+dd;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 270))
      
   def test71(self):
      input="""
            Class Test{
               Var a: Int;
               a=10;
            }
      """
      expect = "Error on line 4 col 16: ="
      self.assertTrue(TestParser.test(input, expect, 271))
      
   def test72(self):
      input="""
            Class Test{
               Var a: Int;
               Var c: Int= a;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 272))
      
   def test72(self):
      input="""
            Class Test{
               Var a: Int;
               Var c: Int= a;
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 272))
   
   def test73(self):
      input="""
            Class Test{
               Var $a: Int= 10;
               Var c: Int= $a;
            }
      """
      expect = "Error on line 4 col 27: $a"
      self.assertTrue(TestParser.test(input, expect, 273))
      
   def test74(self):
      input="""
            Class Test{
               Var arr : Array[String, 0];
            }
      """
      expect = "Error on line 3 col 39: 0"
      self.assertTrue(TestParser.test(input, expect, 274))
      
   def test75(self):
      input="""
            Class Test{
               Var arr : Array[String, 0x0];
            }
      """
      expect = "Error on line 3 col 39: 0x0"
      self.assertTrue(TestParser.test(input, expect, 275))
      
      
   def test76(self):
      input="""
            Class Test{
               Var arr : Array[String, 0X0];
            }
      """
      expect = "Error on line 3 col 39: 0X0"
      self.assertTrue(TestParser.test(input, expect, 276))
      
      
   def test77(self):
      input="""
            Class Test{
               Var arr : Array[String, 0b0];
            }
      """
      expect = "Error on line 3 col 39: 0b0"
      self.assertTrue(TestParser.test(input, expect, 277))
      
      
   def test78(self):
      input="""
            Class Test{
               Var arr : Array[String, 0B0];
            }
      """
      expect = "Error on line 3 col 39: 0B0"
      self.assertTrue(TestParser.test(input, expect, 278))
      
   def test79(self):
      input="""
            Class Test{
               Var arr : Array[String, 00];
            }
      """
      expect = "Error on line 3 col 39: 00"
      self.assertTrue(TestParser.test(input, expect, 279))
      
   def test79(self):
      input="""
            Class Test{
               Var arr : Array[String, 00];
            }
      """
      expect = "Error on line 3 col 39: 00"
      self.assertTrue(TestParser.test(input, expect, 279))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 280))
      
   def test81(self):
      input="""
            Class Test{
               Var arr : Array[Class_A, 1];
            }
      """
      expect = "Error on line 3 col 31: Class_A"
      self.assertTrue(TestParser.test(input, expect, 281))
      
   def test82(self):
      input="""
            Class Test{
               Var arr : Array[1, 1];
            }
      """
      expect = "Error on line 3 col 31: 1"
      self.assertTrue(TestParser.test(input, expect, 282))
      
   def test83(self):
      input="""
            Class Test{
               Var arr : Array[Int, 1];
               Var idx1: Int = arr[1];
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 283))
      
   def test84(self):
      input="""
            Class Test{
               Var arr : Array[Int, 1];
               Var idx1: Int = arr[0+1];
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 284))
      
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
      expect = "Error on line 7 col 25: ("
      self.assertTrue(TestParser.test(input, expect, 285))
      
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
      expect = "Error on line 7 col 18: $Method1"
      self.assertTrue(TestParser.test(input, expect, 286))
      
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
      expect = "Error on line 7 col 23: $Method1"
      self.assertTrue(TestParser.test(input, expect, 287))
      
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
      expect = "Error on line 7 col 24: Method1"
      self.assertTrue(TestParser.test(input, expect, 288))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 289))
      
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
      expect = "Error on line 7 col 35: $static"
      self.assertTrue(TestParser.test(input, expect, 290))
      
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
      expect = "Error on line 7 col 34: ::"
      self.assertTrue(TestParser.test(input, expect, 291))
      
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
      expect = "Error on line 4 col 15: Class"
      self.assertTrue(TestParser.test(input, expect, 292))
      
   def test93(self):
      input="""
            ## Day la test so 93 !!!!! ##
            Class Test{
               Test(){
                  Var int1: Int= 12_2_3_4;
               }
            }
      """
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 293))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 294))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 295))
      
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
      expect = "successful"
      self.assertTrue(TestParser.test(input, expect, 296))
      
   def test97(self):
      input="""
            ## Day la test so 97 !!!!! ##
            Class Test{
               Test(){
                  Var ;
               }
            }
      """
      expect = "Error on line 5 col 22: ;"
      self.assertTrue(TestParser.test(input, expect, 297))
      
   def test98(self):
      input="""
            Var a: Int= 10000000;
      """
      expect = "Error on line 2 col 12: Var"
      self.assertTrue(TestParser.test(input, expect, 298))
      
   def test99(self):
      input="""
            Class A{
               
            };
      """
      expect = "Error on line 4 col 13: ;"
      self.assertTrue(TestParser.test(input, expect, 299))
      
   def test100(self):
      input="""
            Class A{
               Foreach(i In 1 .. 100 By i<=7){
                  Out.Print(i);
               }
            }
      """
      expect = "Error on line 3 col 15: Foreach"
      self.assertTrue(TestParser.test(input, expect, 300))
