# PROBLEM STATEMENT

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

# EXAMPLE

    Input: s = "aababbab"
    Output: 2

Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

# APPROACH

It is given that the string can be balanced, only if there are no pairs like -> "ba" in the string.

And that's the only thing which will make the string invalid. Hence, what we can do is, whenever we come across a situation where the previous character was a "b" but the current character is an "a", we know we have to make one deletion here.

So, we can simply use a stack to keep track of all the previous "b" and whenever we come across an "a", we can then check whether we have a "b" in the stack. If yes, it means, one deletion has to be made. So, we can delete the "b" in the stack in that case, signifying one delete operation.

And this goes on for all the upcoming "b" and "a".
