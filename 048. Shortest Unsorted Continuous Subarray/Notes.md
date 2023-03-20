# PROBLEM STATEMENT

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

# EXAMPLE

    Input: nums = [2,6,4,8,10,9,15]
    Output: 5

Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# **1. SORTING - O(NLogN)**
This is the simplest way to solve this problem. 

We are asked for the shortest unsorted subarray.

So, if we take the input array and sort it, then if there were some elements that were unsorted, then some indices in the sorted array will have different values than what the original array had.

	For example, nums = [2,6,4,8,10,9,15]
	
	If we sort, nums = [2,4,6,8,9,10,15]
	
	Here, we see that the leftmost value that has changed is at index 1. We previously had "6" but now there is "4"
	
	It means, the unsorted array should start at index = 1
	
	Similarly, we see that the rightmost value that has changed is at index = 5. We previously had "9" but now there is "10"
	
	It means, the unsorted array should end at index = 5
	
Hence, it means, the length of unsorted subarray is => 5 - 1 + 1 => 5 

# **2. STACK - O(N)**

We can solve this problem without having to sort the input list and in that case, the time complexity will be linear.

For this, we can take help of stack. 

See, the reason why we chose index = 1 to be the beginning of unsorted subarray in above example was because since index = 1 had a different value in the sorted array, it means in the original array, there was a smaller value after the value present at index = 1. And that's something we can find without sorting too. We just want to check if there is a smaller element on right of any index, right? So that can be done simply using the concept of "Nearest Smaller on Right" using stacks.

And the same case for the end of unsorted subarray. We chose index = 5 in above example because at index = 5, the original array had a smaller value. But the sorted array had a bigger value. It means, the index 5 had a greater value to its left side. And that's all we need to check. We want to check if there is a greater value to the left of any index.

And here, we can use the concept of "Nearest Greater on Left" using stacks.
