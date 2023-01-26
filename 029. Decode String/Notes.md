# PROBLEM STATEMENT

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

# EXAMPLE

    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"


# APPROACH

The code is well commented with each line explained properly.

Anyways, the reason why we decided to use a Deque instead of another list is because if we had used a list, we had to first push all elements in it, then reverse it, and then join it and then get the respective word or number. But if we use a Deque, we can push from left side which is O(1) operation. So this removes the need to reverse.

