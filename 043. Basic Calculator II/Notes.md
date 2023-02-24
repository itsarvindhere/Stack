# PROBLEM STATEMENT

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# EXAMPLE

    s = "3+2*2"
    Output: 7

# APPROACH

The main idea of both the approaches is the same.

Whenever we have to evaluate an expression, we first process all the divison and multiplications.

Only after that we move over to addition and subtraction.