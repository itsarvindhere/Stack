# PROBLEM STATEMENT

Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

 - Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.

Return true if s is a valid string, otherwise, return false.

# EXAMPLE

    Input: s = "aabcbc"
    Output: true

    Explanation:
    "" -> "abc" -> "aabcbc"

    Thus, "aabcbc" is valid.

# APPROACH

We want to find whether "s" is valid or not. And it is given that to create "s", we can only use "abc" as one unit.

So it simply means, if we remove all the "abc" combinations from "s", we should get an empty string at the end. Only then "s" would be valid.

And well, that's the whole idea of the stack approach. As soon as we get an "abc" combination, we will remove it.

And so, in the end, the stack must be empty for a valid "s".
