# PROBLEM STATEMENT

The factorial of a positive integer n is the product of all positive integers less than or equal to n.

 - For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.

 - For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.

However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.

Given an integer n, return the clumsy factorial of n.

# EXAMPLE

    Input: n = 4
    Output: 7
    Explanation: 7 = 4 * 3 / 2 + 1

# APPROACH

Since the problem says -> "These operations are still applied using the usual order of operations of arithmetic." It means, we have to first perform all the multiplication and divisions and only after that we can do the addition and substraction.

So, the best way would be to divide our expression such that we solve the multiplication and division part separately and once that is done, we just need to add the other values. 

That's why, in the code below, when we have to multiply or divide, we simply do that with the value at top of stack. We do not push a new value to stack in that case.

But if we have to subtract or add, we will push a new element to the stack (negative if we have to subtract). In this way, at the end, all that's left is to add all the stack values once we are done with the loop.

Here is an example to understand it more clearly.

	Suppose we have 10.
	
	We know its expression will be -> 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
	
	So, if we solve the multiplication and division first, we will get
	
	11 + 7 - 7 + 3 - 2
	
	We can write it as 
	
	11 + 7 + (-7) + 3 + (-2)
	
	Did you get it?
	
	That's the whole idea here. 
