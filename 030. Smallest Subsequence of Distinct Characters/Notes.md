# PROBLEM STATEMENT

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

# EXAMPLE

Input: s = "bcabc"
Output: "abc"

# APPROACH

Since we want the "lexicographically smallest subsequence of s", it means, we want a monotonically increasing subsequence.

We will use a stack to compare the current character with previous characters and check whether the current character should be placed before the characters on top of stack. IF yes, then we have to remove the characters on top.

But we can only remove them if we know that those characters will be found later in the string again. Otherwise, we will not be able to create a subsequence with all the characters in it.

And for that, we use a Dictionary to keep track of what is the last index of each character in the string. So, we can pop from top of stack only if currently, the index at which we are, is less than the last index of the character that we are going to pop from top of stack.