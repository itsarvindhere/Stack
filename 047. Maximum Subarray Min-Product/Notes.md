# PROBLEM STATEMENT

The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

 - For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.


Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

# EXAMPLE

    Input: nums = [1,2,3,2]
    Output: 14

Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

# APPROACH

This problem may seem like a hard problem at first but if you break it down, you will understand that the main idea is really simple.

See, we want to find the maximum min-product  of any subarray of given array.

So, doesn't it make sense that if we "maximize" the minimum value of a subarray and at the same time we "maximize" the number of elements in a subarray, we will get the maximum min-product?

	That is, if we have a list  -> [1,2,3,2]

    If we take "1" as the minimum value, we know we can take the whole list as a subarray
	But here, we are only maximizing the count of elements.

	We also want to maximize the minimum value in the subarray
	
	Now, we have two choices. We can take "2" as minimum value in a subarray and in that case,
	We have two subarrays to choose from [2,3] and [2,3,2]
	
	It doesn't makes sense to choose [2,3] because we want to maximize the count of elements as well.
	
	Hence, we always take the maximum possible subarray that we can get by taking a certain element as the minimum element.
	
	The other choice is to take "3" as the minimum element. This will maximize the minimum element in subarray
	But then again, it will minimize the count of elements because we can have only [3] as the subarray with minimum value as 3.
	
	So, eventually, we see that the subarray that gives us the maximum min-product is [2,3,2]

So, what did we actually do in above case is to take each element of the given list and consider it as the minimum element of the subarray to which it belongs. Now, we want to see how far this subarray can be extended to left and right side such that this element still remains the minimum element.

And in this way, for every element, we can find the largest subarray with that element as the smallest.

Now you may think - How to find how far we can extend any subarray to left and right side?

That's where we use the Nearest Smaller on Left & Nearest Smaller on Right  (NSL and NSR). These are the basic problems that we go through when dealing with stacks so I am assuming you know how to find NSL and NSR in O(N) time.

Now, take the above example and let's say our list was like [1,2,3,2,1]

Even in this case, the subarray that would give us the maximum min product would be [2,3,2]

Now notice one thing. When we take "2" as the minimum value in subarray, we can only go till index = 1 on left. Because before that index, we have "1" which is smaller than 2. And it is also the "Nearest smaller element to left".

Similarly, we can only go till index = 3 on right because after that index, we have "1" which is smaller than 2 and it is also the "Nearest smaller element to right".

And now you can see that we can quickly get the left and right bound for any value by simply using the NSL and NSR arrays.

So that solves one part of the problem.

The next part is how to quickly get the sum of a subarray. That's where prefix sum comes into the picture.

	Suppose, we have [1,2,3,2]
	
	Prefix sum will be [1,3,6,8]
	
	Now, from this prefix sum, we can find sum of any subarray that starts at any index "x" and ends at any index "y"
	
	By simply doing -> prefixSum[y] - prefixSum[x - 1]
	
	Suppose, we want sum of subarray [2,3,2] which starts at x = 1 and ends at y = 3
	
	So we will do -> prefixSum[3] - prefixSum[1-1]
	
	We get -> 8 - 1 => 7
	
	And indeed the sum of [2,3,2] is 7
	
	Do note that if x is 0 then in that case we cannot just do prefixSum[0 - 1]
	
	In that case, it simply means, there is no left boundary and we can take all elements on left into a subarray.
	
	So in that case, we will do -> prefixSum[y] - 0 or simply prefixSum[y]
	
	
And now, you see this problem became so easy after we broke it down into smaller problems and solved those first.