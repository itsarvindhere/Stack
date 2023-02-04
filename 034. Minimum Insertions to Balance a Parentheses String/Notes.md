# PROBLEM STATEMENT

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

 - Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
 - Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

 - For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

# EXAMPLE

    Input: s = "(()))"
    Output: 1

Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

# APPROACH

ince it is given that for an opening bracket, we need two closing brackets to form a pair, we can conclude that there are basically these conditions to check if we get a closing bracket -

1. This closing bracket might have another closing bracket after it, resulting in a "))" which means, there are two conditions - 
	1.1. If we have an opening bracket before that is yet to be paired, then there is **no insertion required**
	1.2. But if we have no opening bracket before, we need to **insert one opening bracket** to make a "())" pair.
	
2. This closing bracket might have no closing bracket after it, resulting in a ")", which means, there are two more conditions - 
	2.1. If we have an opening bracket before that is yet to be paired, then we only have to **insert one closing bracket**.
	2.2. If we have no opening bracket before, then we have to **insert one opening and one closing bracket**.
	
3. This closing bracket might be the last character in the string. In that case - 
	3.1. If we have an opening bracket before that is yet to be paired, then we only have to **insert one closing bracket**.
	3.2. If we have no opening bracket before, then we have to **insert one opening and one closing bracket**.

So with this, one thing we can understand is we need to keep track of the opening brackets. For that, we can either use a stack to keep all the opening brackets, or a simple counter variable. 