# PROBLEM STATEMENT

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# EXAMPLE

    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

# APPROACH

This is just a variation of "Nearest Greater on Right" problem which is one of the most basic problems you will come across while studying stacks.

Before going with the Stack approach, let's first understand how we will write a Brute force solution which is not that hard.

## **1. BRUTE FORCE APPROACH - O(N^2)**

The Brute Force approach is pretty straightforward. Since we are asked to find a warmer temperature than the current temperature in future, that simply means we can use a nested for loop such that we loop for the first temperature in the future that is greater than current day's temperature.  As soon as we find it, we will stop our loop.

But think what would happen if we have an input like [10,10,10,10,10,10]

In this case, for each element, we will loop till the end, only to find that there is no greater temperature at all. And this is not efficient at all.

So, for such test cases, this code will give TLE.
		
## **2. STACK APPROACH - O(N)**

Using a Stack, we can bring the time complexity down and avoid TLE.

The thing is, when we have such a case where we have a nested for loop in which the inner loop depends on the loop variable of the outer loop, then we can think of using a Stack to optimize our code. In the Brute Force approach, we saw that inner loop depends on outer loop's variable (j = i + 1).

So the trick is that, if we have to find the greater or smaller element to the "right" of an element in an array, then we will start our loop from the end. And if we have to find the greater or smaller element to the "left" of an element in an array, then we will start our loop from the start.

So here, we start our loop from the last index and now, what we are going to do is first remove all the useless elements present on top of stack. That is, all the temperatures that are smaller or equal to current temperature.

If our stack becomes empty, that means we did not find any greater element at all than current element. But if it is not empty, it means, the top of stack has the index of nearest greater temperature on the right.

And that's the whole idea of this approach.