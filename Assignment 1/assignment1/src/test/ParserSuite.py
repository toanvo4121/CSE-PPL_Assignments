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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 235))
      
   def test36(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 236))
      
   def test37(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 237))
      
   def test38(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 238))
      
   def test39(self):
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 239))   
      
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 240))
      
   def test41(self):
      input="""
         Class TestError{
            Val $Cuong: Float = 10.2;
            Var Hiu: Int = $Ton;
         }
      """
      expected = "Error on line 4 col 27: $Ton"
      self.assertTrue(TestParser.test(input, expected, 241))
      
   def test42(self):
      input="""
         Class TestError {
            Var error_arr: Array[Int, 0];
         }
      """
      expected = "Error on line 3 col 38: 0"
      self.assertTrue(TestParser.test(input, expected, 242))
      
   def test43(self):
      input="""
         Class TestError {
            Var error_arr: Array[Float, 0x0];
         }
      """
      expected = "Error on line 3 col 40: 0x0"
      self.assertTrue(TestParser.test(input, expected, 243))
      
   def test44(self):
      input="""
         Class testStaticParamError {
            $main($error_param: Int) {
               System.out.println("Error");
            }
         }
         """
      expected = "Error on line 3 col 18: $error_param"
      self.assertTrue(TestParser.test(input, expected, 244))
      
   def test45(self):
      input="""
         Class testCalFunc {
            main(testParam: Int) {
               print(testParam);
               System.out.println("Error");
            }
         }
      """
      expected = "Error on line 4 col 20: ("
      self.assertTrue(TestParser.test(input, expected, 245))
      
   def test46(self):
      input="""
         Class testReturnError {
            main(testparam: String) {
               System.out.println("Error");
               Return testParam = "error";
            }
         }
      """
      expected = "Error on line 5 col 32: ="
      self.assertTrue(TestParser.test(input, expected, 246))
      
   def test47(self):
      input="""
         Class testReturnError {
            main(testparam: String) {
               System.out.println("Error");
               return;
            }
         }
      """
      expected = "Error on line 4 col 42: ;"
      self.assertTrue(TestParser.test(input, expected, 247))
      
   def test48(self):
      input="""
         Class testReturnError {
            main(testparam: String) {
               System.out.println("Error");
               Return;
            }
         }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 248))
      
   def test49(self):
      input="""
         Class testKeywordError {
            main(testparam: String) {
               System.out.println("Error");
               Return String.error(testParam);
            }
         }
      """
      expected = "Error on line 5 col 22: String"
      self.assertTrue(TestParser.test(input, expected, 249))
      
   def test50(self):
      input="""
         Class testKeywordError {
            main(testparam: String) {
               System.out.println("Error");
               Foreach (i In 1 .. 10 By 1) {
                  If (i % 2 == 0) {
                     Break();
                  }
               }
               Return;
            }
         }
      """
      expected = "Error on line 7 col 26: ("
      self.assertTrue(TestParser.test(input, expected, 250))
      
   def test51(self):
      input="""
         Class testForError {
            main(testparam: String) {
               System.out.println("Error");
               Foreach (i In 1 .. 10 By 1)
                  If (i % 2 == 0) {
                     Break();
                  }
               Return;
            }
         }
      """
      expected = "Error on line 6 col 18: If"
      self.assertTrue(TestParser.test(input, expected, 251))
      
   def test52(self):
      input="""
         Class testForError {
            main(testparam: String) {
               System.out.println("Error");
               Foreach (i in 1 .. 10 By 1) {
                  If (i % 2 == 0) {
                     Break;
                  }
               }
               Return;
            }
         }
      """
      expected = "Error on line 5 col 26: in"
      self.assertTrue(TestParser.test(input, expected, 252))

   def test53(self):
      input="""
         Class testForError {
            main(testparam: String) {
               System.out.println("Error");
               Foreach (i In 1 .. 10 By) {
                  If (i % 2 == 0) {
                     Break;
                  }
               }
               Return;
            }
         }
      """
      expected = "Error on line 5 col 39: )"
      self.assertTrue(TestParser.test(input, expected, 253))
      
   def test54(self):
      input="""
         Class testVarError {
            main(testparam: String) {
               Var var_1, var_2, var_3: Int = 0, 0XA_BCD_EF, 4121, 2001;
               Return;
            }
         }
      """
      expected = "Error on line 4 col 65: ,"
      self.assertTrue(TestParser.test(input, expected, 254))
      
   def test55(self):
      input="""
         Class testVarError {
            main(testparam: String) {
               Var var_1, var_2, var_3, var_4: Int = 0, 0XA_BCD_EF, 4121;
               Return;
            }
         }
      """
      expected = "Error on line 4 col 72: ;"
      self.assertTrue(TestParser.test(input, expected, 255))
   
   def test56(self):
      input="""
         Class testCommaError {
            main(testparam: String) {
               Var var_1, var_2, var_3: Int = 0, 0XA_BCD_EF, 4121;;
               Var var_4: String = "foo";
               Return;
            }
         }
      """
      expected = "Error on line 4 col 66: ;"
      self.assertTrue(TestParser.test(input, expected, 256))
      
   def test57(self):
      input="""
         Class testIfError {
            main(testparam: String) {
               System.out.println("Error");
               Foreach (i In 1 .. 10 By 1) {
                  if (i % 2 == 0) {
                     Break;
                  }
               }
               Return;
            }
         }
      """
      expected = "Error on line 6 col 21: ("
      self.assertTrue(TestParser.test(input, expected, 257))
      
   def test58(self):
      input="""
         Class testIfError {
            main(testparam: String) {
               System.out.println("Error");
               Foreach (i In 1 .. 10 By 1) {
                  If (i % 2 == 0)
                     Break;
               }
               Return;
            }
         }
      """
      expected = "Error on line 7 col 21: Break"
      self.assertTrue(TestParser.test(input, expected, 258))
      
   def test59(self):
      input="""
         Class testNewError {
            main(testparam: String) {
               System.out.println("Error");
               Var Peter_4: Spider_verse = New Spider_verse;
               Return;
            }
         }
      """
      expected = "Error on line 4 col 42: ;"
      self.assertTrue(TestParser.test(input, expected, 259))
      
   def test60(self):
      input="""
         Class testNewError {
            main(testparam: String) {
               System.out.println("Error");
               Var Peter_4: Spider_verse = new Spider_verse();
               Return;
            }
         }
      """
      expected = "Error on line 4 col 42: ;"
      self.assertTrue(TestParser.test(input, expected, 260))
      
   def test61(self):
      input="""
         Class testParamError {
            main(testparam_1: String, testparam_2: Int) {
               System.out.println("Error");
               Return;
            }
         }
      """
      expected = "Error on line 3 col 36: ,"
      self.assertTrue(TestParser.test(input, expected, 261))
      
   def test62(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 262))
      
   def test63(self):
      input="""
         Class testReturnError {
            main(testparam_1: String; testparam_2: Int) {
               System.out.println("Error");
               Return *;
            }
         }
      """
      expected = "Error on line 5 col 22: *"
      self.assertTrue(TestParser.test(input, expected, 263))
      
   def test64(self):
      input="""
         Class testReturnError {
            main(testparam_1: String; testparam_2: Int) {
               System.out.println("Error");
               Return [2, 5, 90];
            }
         }
      """
      expected = "Error on line 5 col 22: ["
      self.assertTrue(TestParser.test(input, expected, 264))
      
   def test65(self):
      input="""
         Class testErrorOperators {
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
                  Return Self.binarySearch(arr, mid ++ 1, r, x); 
               } 
               Return -1; 
            } 
         }
      """
      expected = "Error on line 13 col 53: +"
      self.assertTrue(TestParser.test(input, expected, 265))
      
   def test66(self):
      input="""
         Class testErrorOperators {
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
                     j++;
                  }
                  arr[j+1] = temp;
               }
            }
         }
      """
      expected = "Error on line 16 col 22: +"
      self.assertTrue(TestParser.test(input, expected, 266))
      
   def test67(self):
      input="""
         Class testErrorParenthesis {
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
      """
      expected = "Error on line 21 col 6: <EOF>"
      self.assertTrue(TestParser.test(input, expected, 267))
      
   def test68(self):
      input="""
         Class testErrorParenthesis {
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
            
            main() {
               Self.insertionSort(arr, left, right;
               Return "Error";
            }
         }
      """
      expected = "Error on line 23 col 50: ;"
      self.assertTrue(TestParser.test(input, expected, 268))
      
   def test69(self):
      input = """
         Class testErrorParam {
            main(args : Array[Int,2]) {
               System.out.println(Hello Peter);
            }
         }"""
      expected = """Error on line 4 col 40: Peter"""
      self.assertTrue(TestParser.test(input,expected,269))
      
   def test70(self):
      input="""
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
               
               If (Peter_1.getName() ==. Peter_2.getName() && Peter_1.getSuits() ==. Peter_2.getSuits()) {
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
      expected = "Error on line 34 col 81: ==."
      self.assertTrue(TestParser.test(input, expected, 270))
      
   def test71(self):
      input="""
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
               
               If (Peter_1.getName() ==. Peter_2.getName() || Peter_1.getSuits() ==. Peter_2.getSuits()) {
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
      expected = "Error on line 34 col 81: ==."
      self.assertTrue(TestParser.test(input, expected, 271))
      
   def test72(self):
      input="""
         Class testErrorArgument {
            main(args : Array[Int,2]) {
               System.out.println(args[1] || args[2]);
            }
         }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 272))
   
   def test73(self):
      input="""
         Class testErrorArgument {
            main(args : Array[Int,2]) {
               System.out.println(args[1] && args[2]);
            }
         }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 273))
      
   def test74(self):
      input="""
         Class TestReturn {
            $main() {
               Return;
               Return (4 + 3) * (2 - (16 % 3));
               Return New Spider_verse();
               Return New BinaryTree(root);
            }
         }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 274))
      
   def test75(self):
      input="""
         Class EmptyClass {
            
         }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 275))
      
      
   def test76(self):
      input="""
         Class testNestedClass {
            Class ErrorClass {
               
            } 
            
            main() {
               
            }
         }
      """
      expected = "Error on line 3 col 12: Class"
      self.assertTrue(TestParser.test(input, expected, 276))
      
      
   def test77(self):
      input="""
         Class TestErrorArray {
            Var arr : Array[4, 12];
         }
      """
      expected = "Error on line 3 col 28: 4"
      self.assertTrue(TestParser.test(input, expected, 277))
      
      
   def test78(self):
      input="""
         Class TestErrorExprOutsideMethod {
            If (i % 2 == 0) {
               System.out.println(i + " is an even number);
            }
         }
      """
      expected = "Error on line 3 col 12: If"
      self.assertTrue(TestParser.test(input, expected, 278))
      
   def test79(self):
      input="""
         Class TestErrorArray {
            Var arr : Array[Spider_verse, 15];
         }
      """
      expected = "Error on line 3 col 28: Spider_verse"
      self.assertTrue(TestParser.test(input, expected, 279))
      
   def test80(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 280))
      
   def test81(self):
      input="""
         Class Spider_verse {
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
      """
      expected = "Error on line 11 col 9: class"
      self.assertTrue(TestParser.test(input, expected, 281))
      
   def test82(self):
      input="""
         Class Spider_verse {
            ## instance fields ##
            Val num: Int = 15;
            Var name: Array[String, 15];
            Var suits: String = "Blue";
            
            ## class fields ##
            Var $universe: Int;
            
            ## class methods ##
            $getUniverse() {
               Foreach(i In 1 .. 100 By i%2 == 0) {
                  Self.suits = "red";
               }
               Return Self::universe;
            }
            
         }
      """
      expected = "Error on line 16 col 26: ::"
      self.assertTrue(TestParser.test(input, expected, 282))
      
   def test83(self):
      input="""
         Var errorVar: Float = 0.0000000E0000000;
      """
      expected = "Error on line 2 col 9: Var"
      self.assertTrue(TestParser.test(input, expected, 283))
      
   def test84(self):
      input="""
         Class testCommaError {
            main(testparam: String) {
               Var var_1, var_2, var_3: Int = 0, 0XA_BCD_EF, 4121
               Var var_4: String = "foo";
               Return;
            }
         }
      """
      expected = "Error on line 5 col 15: Var"
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
      expected = "Error on line 7 col 22: ("
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
      expected = "Error on line 7 col 15: $Method1"
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
      expected = "Error on line 7 col 20: $Method1"
      self.assertTrue(TestParser.test(input, expected, 287))
      
   def test88(self):
      input="""
         Class Test{
            Var arr : Array[Int, 1];
            Var idx1: Int = arr[0+1];
         }
      """
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 288))
      
   def test89(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 289))
      
   def test90(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 290))
      
   def test91(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 291))
      
   def test92(self):
      input="""
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
      self.assertTrue(TestParser.test(input, expected, 292))
      
   def test93(self):
      input="""
         Class TestError {
            
         };
      """
      expected = "Error on line 4 col 10: ;"
      self.assertTrue(TestParser.test(input, expected, 293))
      
   def test94(self):
      input="""
         ## Day la test so 94 !!!!! ##
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 294))
      
   def test95(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 295))
      
   def test96(self):
      input=""" 
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 296))
      
   def test97(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 297))
      
   def test98(self):
      input="""
         Var a: Int= 10000000;
      """
      expected = "Error on line 2 col 9: Var"
      self.assertTrue(TestParser.test(input, expected, 298))
      
   def test99(self):
      input="""
         Class A{
            
         };
      """
      expected = "Error on line 4 col 10: ;"
      self.assertTrue(TestParser.test(input, expected, 299))
      
   def test100(self):
      input="""
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
      expected = "successful"
      self.assertTrue(TestParser.test(input, expected, 300))