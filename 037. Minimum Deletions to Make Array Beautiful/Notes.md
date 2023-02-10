# PROBLEM STATEMENT

You are given a 0-indexed integer array nums. The array nums is beautiful if:

 - nums.length is even.
 - nums[i] != nums[i + 1] for all i % 2 == 0.
 - Note that an empty array is considered beautiful.

You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.

Return the minimum number of elements to delete from nums to make it beautiful.

# EXAMPLE

    Input: nums = [1,1,2,2,3,3]
    Output: 2

Explanation: You can delete nums[0] and nums[5] to make nums = [1,2,2,3] which is beautiful. It can be proven you need at least 2 deletions to make nums beautiful.

# **1. USING A STACK - O(N) TIME & O(N) SPACE**

One thing is clear, whenever an index is even, we want to make sure no element after it is the same. And so, the first thing that comes to mind is a stack since for such problems where we have to remove adjacent elements, we use a stack.

The next thing is, if we have to delete an element, ofcourse we won't do the actual deletion from the list. Because since the length of the list can be up to 10^5, it does not make sense to actually delete an element and then shift all the elements after it to the left.

So, for any element, how can we actually find out at what index this element would've been if we had deleted some elements before it? 

	That is simply -> (Current Index - How many elements we deleted so far )
	
Because it makes sense right? We have to shift an index to left by the same amount as the elements we delete before it. 

Okay. So we got the number of deletions that we would've to make in any list. From this number, can we get what would be the number of elements in the beautiful version of the input array? Yes we can.

	We can just do -> (Original Length - Number of deletions)

And so, if this value is odd, what does that mean? That means, even after we did our deletions, the array is still of an odd length. This is not good since for an array to be beautiful, it should be of an even length. So, what is the best way to convert an odd length array into an even length array? 
	
	Just remove one element from it.
	
And it means, one more deletion in this case.

# **2. WITHOUT A STACK - O(N) TIME & O(1) SPACE**

Do you think we need a stack at all? Because we use a stack only for one thing and it is to compare elements. But for that, we can simply use a variable right? And that's the whole idea of an O(1) space approach.  Instead of a stack, we will use a variable to keep track of previous element so that if we have to, we can compare the current and previous elements.

The rest of the code remains the same.
