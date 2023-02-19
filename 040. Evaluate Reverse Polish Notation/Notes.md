# PROBLEM STATEMENT

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

 - The valid operators are '+', '-', '*', and '/'.
 - Each operand may be an integer or another expression.
 - The division between two integers always truncates toward zero.
 - There will not be any division by zero.
 - The input represents a valid arithmetic expression in a reverse polish notation.
 - The answer and all the intermediate calculations can be represented in a 32-bit integer.

# EXAMPLE

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22

Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 
# STACK APPROACH

Since we want to keep track of what were the previous operands as soon as we get an operator, there cannot be a better option than a Stack.

So, if we get an operand, we will simply push it to the stack (in integer form)

But if we get an operator, we know that there will be at least two operands before it so we will pop both of them, apply the operations and push the result back to the stack.

And when we are done, the stack will have only one element which would be the final result.