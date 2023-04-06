# PROBLEM STATEMENT

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

 - It is ().
 - It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
 - It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

 - If locked[i] is '1', you cannot change s[i].
 - But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

# EXAMPLE

    Input: s = "))()))", locked = "010100"
    Output: true

Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

# STACK APPROACH

This problem is the same as -> https://leetcode.com/problems/valid-parenthesis-string/

The only difference is that, in that problem, we had stars which we could use as either ")" or "(" or "" to make the string valid.

Here, we are given indices at which we can flip the bracket to make the string valid. That's it.

So, the logic remains the same as that problem. 

Here is my solution for LC 678 -> https://leetcode.com/problems/valid-parenthesis-string/discuss/3347300/Python-Greedy-Approach-using-Stack-or-EXPLAINED

Here, flipping the characters at certain indices is an option that we are given in case we cannot find a bracket to pair the current bracket with. So before we do that, we want to see if for a closing bracket, we have an opening bracket available with us. IF not, only then we will look at the indices at which we can flip the brackets.