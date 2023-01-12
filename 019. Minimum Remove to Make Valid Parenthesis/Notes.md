# PROBLEM STATEMENT

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

 - It is the empty string, contains only lowercase characters, or
 - It can be written as AB (A concatenated with B), where A and B are valid strings, or
 - It can be written as (A), where A is a valid string.

# EXAMPLE

    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"

Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


# APPROACH

Well, here we have yet another problem related to Balancing the parenthesis. And again, we can make use of "Stack" here because we want to keep track of what was the previous parenthesis we encountered so that we can see whether we can pair two parenthesis or not.

Basically, in this problem, we will keep matching the parenthesis and in the stack, we have to keep the indices of the parenthesis. Why? Because when the loop ends, if there are any indices left in the stack, they will be those indices which had parenthesis that were not paired with other parenthesis.

In other words, those are the parenthesis we want to remove.

And to remove them, the simplest way is to replace them with an empty string. We can do that by converting the input string to a list, replace the parenthesis to remove by empty string, and then convert this list back to the string version and return it.