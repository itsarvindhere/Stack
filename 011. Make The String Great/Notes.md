# PROBLEM STATEMENT

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

 - 0 <= i <= s.length - 2
 - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.


To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

# EXAMPLE

    Input: s = "leEeetcode"
    Output: "leetcode"

Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

# APPROACH

Same Problem as -> Remove Adjacent Duplicates in a String.

The only difference here is that we have to check the "case" here. So a duplicate in this problem means,

    1. If a character is in lowercase, then the same character is present in next position but in uppercase
    2. If a character is in uppercase, then the same character is present in next position but in lowercase

So, to check the case and then compare, we can use "swapcase()" method in Python.

So if we pass a lowercase character to this method, it will give us the uppercase version of it. And vice versa. And in this way, we can compare two adjacent characters.