# PROBLEM STATEMENT

Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

 - CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
 - void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
 - int pop() Pops and returns the top of the stack or -1 if the stack is empty.
 - void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

# APPROACH

Since in Python, we can use a list to use it as a stack, when we want to increment bottom "k" values, it simply means just increment first "k" values in the list. And that's pretty straightforward.

One thing to make sure of is "k" should be less than or equal to the length of stack. If it is more than length, it means there are less than k elements in the stack. And in that case, we will increment all elements of the stack.

