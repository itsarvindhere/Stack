# PROBLEM STATEMENT

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

# EXAMPLE

    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true

Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# APPROACH

So, what are we doing? 

	Let's take an example: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
	
Initially, we start with an empty stack. So, it is not hard to think that if it is possible to replicate the operations given in these two lists, then at the end, our stack should still be empty.

So, what we are going to do is, simply take each element and push it on to the stack. And in the same step, if the element to pop (whatever the pointer to "popped" list points at) is the same element that currently sits on top of stack, we will pop it. And this needs to be done in another loop because it is possible that once we pop the top element, the new top element is the one to be popped next. So we will keep popping accordingly.

	Hence, in above example, here is what happens,
	
	Initially, j = 0. Which means, the first element to pop is "4".
	
	We push "1". Stack = [1] 
	We push "2". Stack= [1,2]
	We push "3". Stack = [1,2,3]
	We push "4". Stack = [1,2,3,4]. 
	
	Here we see that top of stack = 4 and element to pop is also 4.
	
	Hence, while this is the case, we will keep popping from this stack.
	So we pop "4" and stack becomes [1,2,3]. New top is "3"
	
	Since the next element to pop is "5" (j = 1), and it is not same as "3", inner Loop terminates.
	
	We move on to next element to push which is "5".
	
	5 is pushed to the stack. Stack becomes [1,2,3,5]
	
	Since "5" is the same element that we have to pop, the inner while loop starts.
	
	5 is popped. Stack becomes [1,2,3] and j = 2. Next element to pop is 3.
	3 is popped. Stack becomes [1,2] and j = 3. Next element to pop is 2.
	2 is popped. Stack becomes [1] and j = 4. Next element to pop is 1.
	1 is popped. Stack becomes empty and While loop terminates.
	
	And so does the outer for loop (since we are already past the last element of "pushed" list)
	
Finally, because the stack is empty after these steps, it means this is a valid scenario and hence, we return True.