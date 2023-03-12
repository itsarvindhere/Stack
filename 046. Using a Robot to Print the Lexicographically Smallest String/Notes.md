# PROBLEM STATEMENT

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

 - Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
 - Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
  
Return the lexicographically smallest string that can be written on the paper.

 # EXAMPLE

    Input: s = "zza"
    Output: "azz"

Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

# APPROACH 1 - USING A DICTIONARY

One thing that we can understand from the examples is that, we can only move any character from the end of "t" to the paper, if we are sure that there is no smaller character after it in "s".

And that's the whole idea of using a dictionary.

We can keep a count of each character in the string "s" such that at any time, we can check whether there are any smaller characters on the right of any particular character in "s". If not, we can safely move that character to the paper. Otherwise, it makes sense to hold that character in "t" and first push the smaller character to paper which is on the right.

So this is a greedy approach where at any point, we want to make sure current character is the smallest among all the characters on the right side. This will ensure that the final output is the Lexicographically smallest string.

# APPROACH #2 - PRECOMPUTE SMALLEST CHARACTER ON RIGHT OF EACH CHARACTER

To improve the code, we can pre compute the smallest character on the right side of each character.

For Example, take "bac"
	
	If we take smallest on right, our array will be like -> ["a", "c", "z"]
	
	It simply means, the smallest on right of "b" is "a". 
	
	The smallest on the right of "a" is "c" (since c is the only character on right of "a") 
	
	And since c is the last character, for it, the smallest on right is set as "z".
	
	Now, we iterate over our string "bac" and in each iteration, we push the current string to the stack "t"
	
	So first, we push "b". t becomes ["b"]
	
	Now, before we move on to next character, 
	we will check if we can safely write this character or any characters before on the paper.
	
	And as we saw in first approach, we can do so only if we are sure that there are no smaller characters than it on right side.
	
	And here, we will make use of our pre-computed data. 
	
	We can only move current character to paper if the smallest character on its right is >= to it. 
	Or basically, if there is no smaller character on right.