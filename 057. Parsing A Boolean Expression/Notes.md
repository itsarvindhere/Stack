# PROBLEM STATEMENT

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

 - 't' that evaluates to true.
 - 'f' that evaluates to false.
 - '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
 - '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
 - '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

# EXAMPLE

    Input: expression = "&(|(f))"
    Output: false

Explanation: 

First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

# APPROACH

This is very similar to the "Reverse Polish Notation" problem because in that problem as well, we have some operators and we have to evaluate an expression. There, we had "+", "-", etc. Here, we have logical operators - "&", "!" and "|".

So, we will use a stack so that we can keep track of the individual expressions between "(" and ")". As soon as we reach a closing bracket ")", we know that in between, there was an expression that needs to be evaluated before we move further.

So, we will then go backwards to figure out what was the expression (in simple words, how many "t" and "f" we had in this expression) and what operation we have to perform on this expression.

And so, finally, we will be left with only one element in the stack. Either "t" or "f".

NOTE that since our expression can have "," as well, we want to skip those. We won't include them in the stack.