# PROBLEM STATEMENT

A parentheses string is valid if and only if:

 - It is the empty string,
 - It can be written as AB (A concatenated with B), where A and B are valid strings, or
 - It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

Return the minimum number of moves required to make s valid.

# EXAMPLE

Input: s = "())"
Output: 1
