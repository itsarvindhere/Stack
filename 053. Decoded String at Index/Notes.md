# PROBLEM STATEMENT

You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

 - If the character read is a letter, that letter is written onto the tape.
 - If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
  
Given an integer k, return the kth letter (1-indexed) in the decoded string.

# EXAMPLE

    Input: s = "leet2code3", k = 10
    Output: "o"

Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

# CONSTRAINTS

 - 2 <= s.length <= 100
 - s consists of lowercase English letters and digits 2 through 9.
 - s starts with a letter.
 - 1 <= k <= 109
 - It is guaranteed that k is less than or equal to the length of the decoded string.
 - The decoded string is guaranteed to have less than 263 letters.

# APPROACH

It is important to note the constraints in this problem. If you look at the constraints, then the decoded string can have up to 2^63 letters which is too large. This means, we cannot try to decode the encoded string first because that will exceed the memory limit.

So, first thing to note is, we are not going to decode the string at all. 

So, what can we do then? If we do not decode, can we still find the length of the decoded string?

The answer is yes.

    Take an example ->  s = "leet2code3"

    Here, Let's take each index and try to see by what value length will increase in a decoded string.

    At index = 0, we have "l". Since it is a letter, the length will increase by 1 only.
    Same will be the case for "e", "e" and "t".

    So if we keep the lengths at each index in a stack or a list, we will get -> 

    [1,2,3,4]

    At index = 4 in "leet2code3", we have "2". This is not a letter. It is a digit.
    And according to the problem, if we have a digit, 
    then we have to repeat whatever string we have so far "digit - 1" times.

    It means, since the string that we got so far is of length = 4,
	the new string we will now get after we take the digit "2" in consideration will be of length -> 4 * 2 => 8

    So, list becomes [1,2,3,4,8]

    And finally, we will get a list as -> [1,2,3,4,8,9,10,11,12,36]


    So, now, for each index, we know how much it will contribute to the length of the decoded string.


Okay. So how will this help in finding the "Kth" letter in decoded string?

    Just think about this.

    Suppose, K = 20

    Just looking at the list itself, it is pretty obvious that the 20th character will lie between "12" and "36"th length right?

    And the numbers between "12" and "36" are missing in list because the string of length "12" was repeated "3" times. That's why the next length is "12 * 3 = 36".

    So it means, the 20th character is the same as the 20 % 12 => 8th character. 

    If this still does not make sense. Take an example.

    Suppose, we have "abc4" and k = 7

    So decoded version will be -> "abcabcabcabc"

    Here we can see that 7th letter is "a".

    This also means, the 7th letter in "abc4" is same as "7 % 3" => 1st lettter in "abc4". 
	
	And first letter in "abc4" is "a".  
	
	Because "abc" is repeated 4 times which means, the 4th letter in "abc4" will be "a"  since after "c", we will again start from "a". 
	
	Similarly, the 7th letter in "abc4" will also be "a".

    So that's the whole point.

    Coming back to our example of s = "leet2code3" and k = 20.

    List is [1,2,3,4,8,9,10,11,12,36]

    So, when we loop in reverse, we first get "36". the 20th character cannot be at this length so we continue.

    We get "12". We can be sure that "20"th character is definitely after this length. 

    So, it means, string of length "12" is repeated some number of times and the 20th character will be among the characters that are present in this string of length 12.

    You might have done problems where we have a list of certain length, let's say "x". 
	And it is given that this is a circular kind of list such that if we are at last index, the next index is the 0th index.

    So, in those problems, if we are asked to find the value at an index, lets say "k" that is greater than length of the list,
	then instead of looping over the list again and again till we get "kth" index, we can make use of the modulus operator
	to bring the index in the range of (0, x - 1). The same is the case in this problem.

    Since we, at this point, know that there is a string of length "12" and it is repeated "x" times, and we have to find the "20th" letter, 
	we can use the modulus operator to bring the value of "k" <= 12. 

    In this way, we can then find the required letter in this string of length = 12.

    Here if we do k % 12, we get "20 % 12" => 8. 

    And now, this problem is now reduced to finding the "8th" letter in the decoded string.

    This time, we have the length = 8 in the list already. So does that mean we found the 8th character? Not necessarily.

    Here, List is [1,2,3,4,8,9,10,11,12,36]
     s = "leet2code3

    the index at which length is 8 in this list is the index = 4.

    But at index = 4 in the input string, we have a digit, not a letter.

    And we cannot return a digit as output. Digit just represents repeatitions.

    This means, we also need to take care of the cases when we found the required index but at that index, we have a digit.

    Here, what does 8 mean now?

    It just means, find the 8th character when the string "leet2" is decoded.

    And so again, the same process continues here.

    We continue going backwards and we see the value = 4 in the list.

    8 % 4 => 0.

    This value 4 in the list is at index = 3. And at index = 3 we have the letter "t"

    And since this is a letter and not a digit, we finally got our answer.


The 20th character in s = "leet2code3" is "t".
