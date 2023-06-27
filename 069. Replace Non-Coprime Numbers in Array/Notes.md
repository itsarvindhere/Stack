# PROBLEM STATEMENT

You are given an array of integers nums. Perform the following steps:

 - Find any two adjacent numbers in nums that are non-coprime.
 - If no such numbers are found, stop the process.
 - Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
 - Repeat this process as long as you keep finding two adjacent non-coprime numbers.
  
Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 10^8.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

# EXAMPLE

    Input: nums = [6,4,3,2,7,6,2]
    Output: [12,7,6]

Explanation: 
- (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
- (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
- (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
- (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
There are no more adjacent non-coprime numbers in nums.

Thus, the final modified array is [12,7,6].

Note that there are other ways to obtain the same resultant array.

# APPROACH

As the problem statement says - Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

So, we need to figure out a way by which we can take a number and find its GCD with the previous number. And if the GCD with previous is > 1 then we take the LCM of both, remove previous number from output and then again do the same calculation with previous numbers.

And that can be done efficiently using a Stack.

So, as we traverse the list, we will maintain a stack of elements where, before pushing a value to the stack, we take the GCD of this value with whatever stack has on top. If the GCD is > 1, it means the current and previous values are non-coprime. So, it means, instead of those values, we need to push their LCM in the stack. Hence, we remove the top of stack and so the new value that we have to push is the LCM.

But now, this LCM itself may be non-coprime with the new stack top. So, we again need to do the same calculation. Hence, this will go on until stack is empty or we reach a point where top of stack and the current value are co prime.

Since we already know the GCD of two numbers, finding the LCM is pretty straightforward.

        LCM(a,b) = (a * b) // gcd(a,b)