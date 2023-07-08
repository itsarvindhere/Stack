# PROBLEM STATEMENT

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

# EXAMPLE

    Input: s = ")()())"
    Output: 4

    Explanation: The longest valid parentheses substring is "()()".

# APPROACH

In this problem, we will be given a string that may or may not be a valid parenthesis string. But, it is possible that some part of it might be valid and so, we want to return the length of longest such part/substring which is a valid parenthesis substring.

Before you start solving this problem, it is important to think of what all types of scenarios we may face when we start solving this problem using a stack.

 1. There could be multiple valid substrings one after another e.g. patterns like "()()", "()()()"
 2. There could be a valid substring enclosing one or more valid substrigns e.g. "(())", "(()())"

These are the only two scenarios to take care of.

We will use the stack to keep track of the opening parenthesis such that if any closing parenthesis is found, we can check if we have an opening parenthesis to pair. If we do, then we have a valid parenthesis substring at this point.

Now, we have to check for the above two cases. First, we check whether this substring encloses some previous valid substrings inside it or not. If it does, then that would mean we no longer need to keep those previous substrings in our list (this will be a separate list to keep track of the substrings and their data). 

	For example, we if we have "(())"
	
	Then, before we reach the last closing parenthesis, 
	we would've found one valid parenthesis substring "()"
	
	And so, our substrings list will look like -> [[1,2,2]]
	
	We basically store [start index, end index, length] for each valid substring.
	
	When we reach the last parenthesis, we will match it with the very first opening parenthesis.
	
	So, for this valid substring, the start index is 0, end index is 3 and length is 4
	
	Now we check if it encloses any previously found valid substrings.
	
	For that, we just need to check if any previous substrings starts after index 0 and ends before index 5.
	
	And indeed there is one such substring.
	
	So, we no longer need to keep that data as we found one parent substring that encloses it.
	
Hence, now, the substrings list will become empty and we can now put the data of current substring

So, list will become [[0,3,4]]

It is not always necessary that there is only a single data at the end in the "substrings" list. If there are multiple, we need to take the maximum length out of all and that will be the longest valid parenthesis length.

For the scenario where we may have substrings one after another, We can just check if current substring starts immediately after previous ends. In that case, we can combine lengths of both.