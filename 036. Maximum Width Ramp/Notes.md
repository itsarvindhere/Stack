# PROBLEM STATEMENT

A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

# EXAMPLE

    Input: nums = [6,0,8,2,1,5]
    Output: 4

Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.


# **1. BRUTE FORCE APPROACH - O(N^2)**

The Brute Force approach is pretty straightforward. We can take every index and then check every index on its right to see which one gives us maximum width. And this goes on for every index in the array. Hence, we need a nested for loop.

# **2. SLIGHTLY BETTER BRUTE FORCE APPROACH - O(N^2)**

One thing that we noticed is, if for any index "i", we found a rightmost "j" index that gives is maximum width for "i", then the next time we check for the next index, we can ignore all the values between previous i and the previous j that we found.

# **3. STACK APPROACH (USING REVERSE) - O(N)**
So, what did we conclude from the approach 2? We saw that our comparisons will be reduced if we know what are all the valid "j" values that we can compare our "i" values with. In that way, we don't need to compare "i" with every index after it if we beforehand know what all "j" indices are the candidates to result in a bigger width.

And that's where we will use a stack.


Let's take an example and see how we can use a stack. Or before that, let's understand how stack can even be considered here.

	nums = [6,0,1,2,3,8,4,1,5]
	
	Let's see what are all the useful values of "j"
	
	Starting with the number 6 at index = 0
	
	For "6", rightmost greatest is "8" which is at index = 5
	So it means, no matter what number of between 6 and 8, we don't care
	If we are at index 0, We will get a bigger width at index = 5.
	
	Next, we have the index 1, at which we have the number 0.
	
	Now, for 0, we see that the rightmost valid index is last index at which we have 5 (index 8)
	It means, no matter what number we have between index 1 and index 8,
	the maximum width that index 1 will make is with index 8
	
	And since 8 is the last index in this array, it means, basically we have only two useful j values in this array
	
	These useful "j" indices are -> [5,8]
	
So, to get these values using a stack, we can simply iterate from beginning to end. 

In each iteration, if stack has some index, compare the current value with value at top index in stack. If the current value is greater, it means, the value on top of stack now is useless so it can be removed before pushing current value.

And similarly, when we remove all the useless values, we will be left with only useful "j" indices.

Now, one thing you will note is that we will get the stack with indices in increasing order. Which means, from top to bottom, we will have indices from largest to smallest. But since we want to compare our "i" indices with "j" values that come first in the array, we want stack to have indices in decreasing order. One way to do that is to reverse this stack.
 
# **4. STACK APPROACH (TREAT IT AS A LIST) - O(N)**

Since in python, a stack is basically a list, why reverse it to compare from left to right? We can simply traverse this list using a pointer from left to right and avoid reversing it.
	
# **5. STACK APPROACH (CREATE A DECREASING STACK) - O(N)**

Since we have understood that we want stack with indices in decreasing order from top to bottom, it means, we can loop in reverse while building the stack so that we get indices in decreasing order as well.
