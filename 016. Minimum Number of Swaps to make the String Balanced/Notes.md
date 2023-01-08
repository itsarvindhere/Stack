# PROBLEM STATEMENT

You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

# EXAMPLE

    Input: s = "][]["
    Output: 1

Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".

# APPROACH

Whenever there is a problem around parenthesis and balancing them, "Stack" is the best way to come up with a solution. In this problem, we have to find how many swaps we have to make to make the string balanced. So, if you take a few examples, then you will find that the number of swaps actually depends on how many closing brackets are there for which we could not find a matching opening bracket.

And that's the idea behind both the approaches below.

Just keep track of opening and closing brackets. And at the end, the number of swaps will be -

	Ceil of (Number of Closing Brackets without match / 2)