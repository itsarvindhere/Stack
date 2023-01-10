# PROBLEM STATEMENT

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 
# EXAMPLE

    Input: s = "(ed(et(oc))el)"
    Output: "leetcode"

Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

# APPROACH

We have to reverse each substring between the parenthesis so stack is the best way to approach this problem. 

	Let's take a simple example 
	
	s = "(abcd)"
	
	We know that we want to reverse the string between the opening and closing bracket. 
	
	So, if we simply keep pushing the characters into a stack, until we reach a closing bracket.
	
	Then, our stack will be like -> ['(', 'a', 'b', 'c', 'd']
	
	And as soon as we reach a closing bracket, we want to reverse the string now. 
	
	Which means, pop each character till the last opening bracket and then push back everything in reverse order.
	
	So after doing that, our stack will be like - ['d', 'c', 'b', 'a']
	
And finally, we simply return the string version of this stack. That is, "dcba".

Now, let's take a more complex example with nested brackets/

		s = "(u(love)i)"
		
		Here, we want to first reverse the string between the inner most brackets.
		
		So, if we do the same as we did above, will it still work? Let's see
		
		We keep pushing till we get a closing bracket. So stack will be like - 
		
		stack = ['(', 'u', '(', 'l', 'o', 'v', 'e']
		
		Now, as soon as we reach our first closing bracket, it is definitely the closing bracket of innermost pair right?
		
		So we will now keep popping till we reach opening bracket and then push back everything in reverse.
		
		stack = ['(', 'u', 'e', 'v', 'o', 'l']
		
		And now, we will continue. 
		
		We have a character "i" so we push it to the stack.
		
		stack = ['(', 'u', 'e', 'v', 'o', 'l', 'i']
		
		And we now again get a closing bracket. 
		
		Which means, reverse everything between this bracket and the last opening bracket.
		
		stack = ['i', 'l', 'o', 'v', 'e', 'u']
		
And finally, return the string version of this stack. That is "iloveu".
