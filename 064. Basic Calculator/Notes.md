# PROBLEM STATEMENT

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# EXAMPLE

    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

# APPROACH

Just go through the expression, get the sum of values inside parenthesis and keep adding that sum with values in stack.

Eventually, the stack will have only one value at the end which will be the result of the expression.
