# PROBLEM STATEMENT

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# EXAMPLE

    Input: nums = [1,2,1]
    Output: [2,-1,2]

Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

# **APPROACH #1 - DOUBLE THE LIST**

To simulate a circular array, what we can do is double the given input list. And now, just use the same template as the "Nearest Greater Element I".

The only change will be when we have to set some value in the output array. Since the output array is of the same size as original list, we can use "mod" to make sure there is no issue with index being greater than length of output list.

# **APPROACH #2 - LOOP TWICE**

We can avoid doubling the input list and rather, simply loop twice the length of the input list. And to make sure the index remains between [0, original length], we will make use of the Modulus operator "%". 