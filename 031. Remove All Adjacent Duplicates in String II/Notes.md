# PROBLEM STATEMENT

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

# EXAMPLE

    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"

Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

# APPROACH

Since we are given the value "k" in this problem, we have to keep track of how many times an element is appearing consecutively. For that, instead of pushing just the element in stack, we can push a pair -> [element, count].

Now, if we come across the element again which is currently at the top of stack, then it means we can increment its count.

And if the count becomes equal to k, it means this element is appearing consecutively k times so it needs to be removed and hence we will pop it.

At the end, the stack will have only those elements that need to be there in the final string.

