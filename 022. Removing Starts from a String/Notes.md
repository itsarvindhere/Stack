# PROBLEM STATEMENT

You are given a string s, which contains stars *.

In one operation, you can:

 - Choose a star in s.
 - Remove the closest non-star character to its left, as well as remove the star itself.
  
Return the string after all stars have been removed.

Note:

 - The input will be generated such that the operation is always possible.
 - It can be shown that the resulting string will always be unique.


# EXAMPLE

    Input: s = "leet**cod*e"
    Output: "lecoe"

Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

# APPROACH

Since when we get a star, we want to remove the previous character, the easiest way to do this is to use a stack. 

Because using a stack, we can quickly get rid of the left character by simply popping the top element.

    If it is a star, pop from the top.
    If it is an alphabet, push to the top.