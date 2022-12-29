# PROBLEM STATEMENT

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

 - void push(int x) Pushes element x to the back of the queue.
 - int pop() Removes the element from the front of the queue and returns it.
 - int peek() Returns the element at the front of the queue.
 - boolean empty() Returns true if the queue is empty, false otherwise.


Notes:

 - You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
 - Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


# APPROACH

The problem statement itself gives us a big hint by mentioning "Two Stacks".

Since a Queue is a FIFO structure and a stack is a LIFO structure, it means, to convert a Stack into a FIFO structure, we have to reverse it such that the element that we pushed first is at the top of stack after reversing. And since we are allowed to only use stack operations like push, pop, peek etc, to reverse, we have to use a second stack.

In this second stack, we will push the elements of the first stack from top to bottom. In this way, the second stack will always have the top element as the one that was pushed first in first stack.