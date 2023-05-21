# PROBLEM STATEMENT

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.


# EXAMPLE

    Input: nums = [1,4,3,7,4,5], k = 3
    Output: 15

Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 


# APPROACH

This problem is almost the same as [LC 84 .Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

Why I said "almost"? Because, the extra thing in this problem is the value "k" that we are provided with as input.

Let's take an example and try to solve it as Largest Rectangle in Histogram 

	nums = [1,4,3,7,4,5], k = 3
	
If you take each value and represent it has a bar on a bar chart, we get something like this - 

![image](https://assets.leetcode.com/users/images/bb2600b7-a70d-40c8-9de6-2366264296a4_1684659903.7957752.png)

	Now, we want the largest rectangle that we can make in this histogram. 

	For that, we can take each bar and see how far to left and right we can extend this bar. 

	For example, if I take the first bar with height = 1, 
	then I can extend it all the way till the end. 
	
	Why? because, there are no smaller bars in between so it will span across the entire chart.

	And so, we will get a rectangle that has length => (rightmost index - leftmost index) + 1 => (5 - 0) + 1 => 6
	And the height = 1 (same as height of the bar from which we extended)

	So, area => 6 * 1 => 6

	But, is this the largest rectangle? For that, we have to take every bar and do the same thing as above.

	When we are at the third bar with height = 3, 
	we will see that we can extend it till index 1 on left and till index 5 on right.

	So for it, the area will be => 5 * 3 => 15

	And this is the largest rectangle in this histogram. 

And for this current problem as well, "15" is the output for this list. 

But, does this mean we just have to find maximum area? In that case, what is the use of "k"?

Well, "k" is just an index that we are given such that we are asked to only take those subarrays that include this index in them.
In simple words, the starting index of those subarrys should be k or less than k. And the last index should be k or more than k.

And if we use this logic in our histogram, it simply means,

	Only consider the rectangles which include the index "k"
	
So, when for any index, we check the left boundary and right boundary for its rectangle, we also need to make sure this left and right boundaries include "k" in between.

	That is, leftBoundary <= k and rightBoundary >= k.

Only if this condition is satisfied, we can update the maximum score.

And well, that's pretty much all that's different than the Largest Rectangle in Histogram problem. We just have this one extra check while we update the maximum score.