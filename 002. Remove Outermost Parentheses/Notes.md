# PROBLEM STATEMENT

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# EXAMPLE

    Input: s = "(()())(())"
    Output: "()()()"

Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# APPROACH

The main idea is that, each part from which we remove the outer parenthesis, should be a balanced string with same number of opening brackets as closing brackets. And so, we have to keep track of opening and closing brackets in our output string. 

I also track the number of brackets we removed so far as to easily figure out whether the current opening bracket has to be removed or not.

In case we have a closing bracket, we can simply check if there is an imbalance. If yet, then that means it belongs to the output string, not among the removed brackets.