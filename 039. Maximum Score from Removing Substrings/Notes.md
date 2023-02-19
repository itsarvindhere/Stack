# PROBLEM STATEMENT

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

 - Remove substring "ab" and gain x points.
   - For example, when removing "ab" from "cabxbae" it becomes "cxbae".
 - Remove substring "ba" and gain y points.
   - For example, when removing "ba" from "cabxbae" it becomes "cabxe".

Return the maximum points you can gain after applying the above operations on s.

# EXAMPLE

    Input: s = "cdbcbbaaabab", x = 4, y = 5
    Output: 19

Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
  
Total score = 5 + 4 + 5 + 5 = 19.

# STACK APPROACH - O(N) SPACE & O(N) Time

Because we want the maximize the points, the best way is to first remove all the pairs for which we will get higher score.

This means, if x > y, then removing "ab" pairs will give us a higher score. So we must first remove all the "ab" pairs in the input string.
Similarly, if x <= y, then removing "ba" pairs will give us a higher score. So we must first remove all the "ba" pairs in the input string.

And so, it is a greedy approach where we are looking for the pairs that have a higher value.

Once we are done with the above step, then the string that we will be left with may have some pairs left which we need to count. Do note that if "x > y" then our string after the above steps may have some "ba" pairs left, since we already took care of all the "ab" pairs. And vice versa for "x <= y" case.

Here, to efficiently track the pairs, we will make use of a stack. Because addition and removal to a stack is an O(1) operation. And for test cases such as "aabb", we know that once we remove middle pair "ab", we get "ab" again so we have to count that as well. This is something we can efficiently do with a stack.