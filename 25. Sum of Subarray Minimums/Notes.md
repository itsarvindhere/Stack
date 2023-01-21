# PROBLEM STATEMENT

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# EXAMPLE

    Input: arr = [3,1,2,4]
    Output: 17

Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

# APPROACH

This problem can be solved easily if you know how to efficiently find the "Nearest Smaller Element on Left" and "Nearest Smaller Element on Right" using a stack. I am assuming you know how to use stack to find NSL and NSR index for an element.

Suppose, we have arr = [3,1,2,4]

Now, since we want to find the minimum element of each subarray and then sum all those elements, what if we can find how many times an element is the minimum among all subarrays?

	Subarrays of [3,1,2,4] are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
	
	Here if you see
		"1" is minimum in -> 6 subarrays
		"2" is minimum in -> 2 subarrays
		"3" is minimum in -> 1 subarray
		"4" is minimum in -> 1 subarray
		
	So we can say, sum => (1 * 6) + (2 * 2) + (3 * 1) + (4 * 1) => 6 + 4 + 3 + 4 => 17
	
And so, now, what we can do is, try to find for how many subarrays a particular element is minimum element.

But how to find that?

Here, we will use the concept of Nearest Smaller on Left and Nearest Smaller on Right.

	Take "2" for example in [3,1,2,4]
	
	It is pretty obvious that for "2" to be the minimum in a subarray, that subarray should not include "1", 
	which is the nearest element on the left that is smaller than 2.
	
	Since on right of 2, there is no smaller element than it, it means,
	any element after "2" can be there in a subarray and still "2' will be minimum.
	
	So, for "2" to be minimum, all subarrays can be formed from the range [2,4] only.
	And here, we get two subarrays from this range -> [2] and [2,4]
	
	So, for "2", Nearest Smaller Index on Left is -> 1
	And Nearest Smaller Index on Right is ->  4 (Since it stretches till the end, we can take length of array as NSR in this case)
	
	Hence, all subarrays formed between index 1 and 4 (both exclusive) will have "2" as the minimum element.
	
And that's the main idea of this approach. We will first find the Nearest Smaller on Left index for each element, and then Nearest Smaller on Right index for each element. Then, we can easily find how many subarrays will be formed by doing -> (leftCount * rightCount).

And once we get that, the only thing left is to add this contribution => (element * subarrayCount) to the totalSum.

**NOTE**: There will be test cases where there are duplicate elements. e,g, [71,55,82,55].

So to make sure our code works for those also, what we can do is to use ">=" in one of the two calculations -> NSR or NSL (You can choose any)