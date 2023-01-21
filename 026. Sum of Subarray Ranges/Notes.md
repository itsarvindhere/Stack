# PROBLEM STATEMENT

You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

# EXAMPLE

    Input: nums = [1,2,3]
    Output: 4

Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

# APPROACH

# **#1. BRUTE FORCE APPROACH - O(N^2)**

Since the maximum length of array can be 1000, a Brute Force approach will work. So we can go through each subarray, keep track of its maximum and minimum and find its range and add it to the rangeSum.

# **#2. STACK APPROACH - ~O(N)**
Super Easy if you have done the problem -> https://leetcode.com/problems/sum-of-subarray-minimums/
Here is my explanation for the code for that problem -> https://leetcode.com/problems/sum-of-subarray-minimums/discuss/3080727/Python-Combination-of-NSL-and-NSR

In this problem, the only extra step is that, we also want to find "Sum of Subarray Maximums". And that's it.
We can use the same code as the Sum of subarray minimums but with a little tweaks and boom! This problem can be solved as well.

The main idea is that, instead of having to find minimum and maximum in each subarray and then finding the range sum, why don't we find how many times an element is the maximum element among all subarrays and how many times that element is the minimum element among all subarrays. 

And so, we will find "Sum of all the maximum elements of all subarrays" and the "Sum of all the minimum elements of all subarrays".

And then, all we need to do is return the difference of these two sums, which is the Range Sum.

**NOTE - The code for this approach is too much to grasp initially so I would recommend to just go through the explanation for "Sum of Subarray Minimums" problem that I linked above. And once you grasp that, then you will instantly figure out what the below code does.**