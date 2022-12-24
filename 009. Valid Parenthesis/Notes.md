# PROBLEM STATEMENT

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

 - Open brackets must be closed by the same type of brackets.
 - Open brackets must be closed in the correct order.
 - Every close bracket has a corresponding open bracket of the same type.

# EXAMPLE

    Input: s = "()[]{}"
    Output: true

# APPROACH

We will use a Stack here to keep the opening brackets such that, as soon as we find a closing bracket, we can quickly check the top of stack to see if there is a matching opening or not. If not, then this is not a valid string at all.

It is also possible that we have a string like "]]]]" In this case, there is no opening bracket at all so the stack will always be empty. So, as soon as we come across a closing bracket and the stack is empty, then also we know the string is not valid.

The only time string is valid is when all the opening brackets have been matched with their correct closing brackets. This means, in that case, stack will be empty at the end.