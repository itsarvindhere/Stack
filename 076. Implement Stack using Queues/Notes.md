# PROBLEM STATEMENT

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

 - void push(int x) Pushes element x to the top of the stack.
 - int pop() Removes the element on the top of the stack and returns it.
 - int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

 - You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
 - Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


# APPROACH

Yes, we can use a deque in Python and use its built-in methods such as appendLeft to push items to the left side and also pop from left side. But, the problem statement says to use only the standard queue operations.

It means, if we push to the queue, the push should happen only at the rear side or right side.

And if the pop happens, it should happen from the front of the queue or the left side.

So, as we push the rear, we have to rotate the queue such that the item we pushed is now at the left or front side of the queue. 

And so, the next time we pop, we will pop from the left only and we will get the item we most recently pushed.
