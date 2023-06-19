# PROBLEM STATEMENT

You are given an integer array nums and an integer threshold.

Find any subarray of nums of length k such that every element in the subarray is greater than threshold / k.

Return the size of any such subarray. If there is no such subarray, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

# EXAMPLE

    Input: nums = [6,5,6,5,8], threshold = 7
    Output: 1

Explanation: The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is returned.
Note that the subarray [6,5] has a size of 2, and every element is greater than 7 / 2 = 3.5. 
Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the given conditions.
Therefore, 2, 3, 4, or 5 may also be returned.

# APPROACH

It was quite hard for me to figure out the solution so I looked into the hints and as the hint #1 mentions -> ***For all elements to be greater than the threshold/length, the minimum element in the subarray must be greater than the threshold/length.***

If you read it a couple of times, you'll say that it is an obvious statement. 

But this statement also tells us that it would be easier to find the subarray length (if there exists a valid subarray that satisfies the condition), if we can find the minimum possible element of that subarray. Because, if we find the minimum element that satisfies the condition, then all elements in that subarray will also satisfy the condition.

This step shouldn't be that difficult. Because we can loop over the given list and at each iteration, we can take the current index as the index of minimum element in the subarray.

But the difficult part is to efficiently find the length of the subarray that contains the current element and in that subarray, the current element is  also the minimum element.

So, now we have a new sub-problem -> 

	Given an array. 
	Take an element at index "x" and consider it to be the minimum element of a subarray. 
	Return the maximum length of that subarray
	
	Example -> nums = [1,3,4,3,1]

	Let's take the element "1" at index 0 as the minimum.
	
	The subarray will be [1,3,4,3,1] because in this subarray, minimum element is "1"
	
	Similarly, if we take element "3" at index = 1 as the minimum,
	then subarray will be [3,4,3] because minimum element is "3"
	
Did you notice something? When we considered "3" as the minimum element
Then, on the left side, we couldn't extend since there was "1" on the left which is already smaller than 3.

But on the right, we could extend to "4" and also to "3" because both are >= 3

We had to stop at "1" on the right because again, it is smaller than "3"

It means, if we take an element as minimum element of a subarray, then we can extend to left until we find a smaller element than it.
Similarly, we can extend to right until we find a smaller element.

And there are two ways to find this smaller element on left or right.

First is the Brute Force Way where we have two nested for loops -> O(N^2)

The second is the Stack way where we can find the Nearest Smaller Element on Left & Nearest Smaller Element on Right -> O(N)

In this problem, the length of the list can be up to 10^5 so ofcourse O(N^2) solution will give TLE.

Hence, we have to use the Stack approach to find the NSL and NSR for the input list.

	Example - 
	
	nums = [1,3,4,3,1]
	NSL  = [-1, 0, 1, 0, -1]
	NSR  = [5, 4, 3, 4, 5]
	
	
	So, lets loop over "nums"
	
	In first iteration, we have index = 0 at which we have element = "1"
	
	The Index of Nearest Smaller Element on Left is NSL[0] => -1
	The Index of Nearest Smaller Element on Right is NSR[0] -> 5
	
	So, the length of the subarray where "1" is minimum will be:
		
		= 5 - (-1) - 1 
		= 5 + 1 - 1
		= 5
		
	So, we now know that there is a subarray of length "5" with mininum element as nums[0]
	
Now read the very first line of this solution -
	
	"For all elements to be greater than the threshold/length, 
	the minimum element in the subarray must be greater than the threshold/length"
	
It means, if nums[0] is greater than threshold / length
Then all elements in this subarray of length "5" also satisfy this condition.
	
Here, nums[0] = 1 and threshold / length = 6 / 5 => 1.2
	
Since 1 is not greater than 1.2, this subarray does not satisfy this condition.
	
	So, we move to next element, that is nums[1] => 3
	
	For nums[1], NSL[1] => 0 and NSR[1] => 4
	
	So length of subarray where "3" is minimum element -> 4 - 0 - 1 => 3
	
	Now we check condition. Thershold is 6 and length of subarray (k) is 3
	
	threshold / k => 2
	
	We see that 3 is indeed > 2 
	
	So it means, this subarray of length 3 with "3" as its minimum element is a valid subarray
	
Hence, we return "3".
