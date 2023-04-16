# PROBLEM STATMENT

You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

# EXAMPLE

    Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
    Output: 3
    
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.


# APPROACH

First, let's take a look at an example.

	nums = [5,3,4,4]
	
	- Step 1: [5,3,4,4] becomes [5,4,4]
	- Step 2: [5,4,4] becomes [5,4]
	- Step 3: [5,4] becomes [5]
	
	Here, we have to perform three steps to make the array non-decreasing (increasing).
	
	Now, ofcourse it is not a good idea to keep looping again and again until we are sure that array is now non-decreasing.
	
	So, how can we quickly figure out, what is the number of steps required for this array to become non-decreasing.
	
	It seems like we are simply counting how many smaller elements on right are there.
	
	BUT THERE IS A CATCH THAT I WILL DISCUSS IN LATER PART.
	
	For example, for "5" at index = 0, we have to remove "3", "4" and "4". So there are "3" elements we have to remove for this "5".

	So, the steps = 3.
	
	It also makes sense since in one step, we can only remove one element such that it is smaller than previous. So here,
	
	In one step, we first remove "3". Then in second step, we remove "4" And finally, we remove the other "4".

	
Remember I said there is a catch in the above approach.

Based on the above approach, it makes sense to simply loop from left to right and see how many smaller elements are there on right of an element, right? But will it give us the right output?

	Take this example ->  [5,3,4,3]
	
	As per our logic, we will remove all the smaller elements on right of "5" and so it takes 3 steps.
	
	But just think about it. Before "5" removes the last "3", won't "4" already remove it?
	
	The problem statement says in one step, all those elements will be removed that have a greater element on their left.
	
	And so, in Step 1, we will remove the "3" on right of "5" and also the "3" on right of "4", leaving us with [5,4]
	
	And in Step 2, we will remove the "4" and so output is 2 steps.
	
And that's the whole idea of using the stack and looping from right to left. Such that, before we reach "5", we have already calculated how many elements "4" will remove and that will represent how many steps it would take.

Finally, to summarize the solution, let's take an example.

	nums  = [7,14,4,14,13,2,6,13]
	
	
	We loop from right to left.
	
	First, we have "13". We removed 0 elements. Stack = [(13,0)]
	
	Next, we have "6". Again, 0 elements removed since we don't have smaller element on top of stack.
	And same story with "2".
	
	Stack = [(13,0), (6,0), (2,0)]
	
	Next up, we have "13". Here, we see that stack has two smaller elements on top. 
	So, before pushing "13" we have to remove these two elements.
	
	Since for "6" and "2", the count of "0", it means we haven't yet performed any step at all.
	
	So, we perform our first step only when we reach "13". We will remove "2" first. 
	stepCount += 1
	
	Then we will remove "6".
	stepCount += 1
	
	Hence, for "13", we removed "2" elements and that took "2" steps. 
	
	Stack = [(13,0), (13,2)]
	
	Next, we have "14". Here, we see that top of stack has "13" and we are already at step 2 at this point since "13" removed "2" elements.
	
	So, when "14" removed the topmost "13", it makes sense that it did that in at least the step 2 (or above).
	
	That's the reason why in the code we did stepCount = max(stepCount + 1, stack[-1][1])
	
	Because if we had just done stepCount += 1, then for "14", 
	it would've meant that one element removed and hence only one step performed.
	And we would've lost the actual steps performed so far, which is "2".
	
	So, the idea is to keep track of maximum steps performed at any point we remove any element.
	Because it makes sense that if we removed some elements already and "x" steps have been taken,
	then if we remove another, then it is either the "x"th step itself or the "x + 1"th step.
	
	So, at this point, we remove (13,2) from stack and right now, stepCount = 2
	
	Then we remove the next "13" and this one took another step. So stepCount = 3
	
	Hence, Stack = [(14,3)] and so far, steps = 3
	
	Similarly, we keep going and eventually, we will find that the maximum value for steps will be "3".
	
Hence, nums  = [7,14,4,14,13,2,6,13] is converted to a non-decreasing array in 3 steps.