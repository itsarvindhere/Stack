# PROBLEM STATEMENT

As the ruler of a kingdom, you have an army of wizards at your command.

You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

 - The strength of the weakest wizard in the group.
 - The total of all the individual strengths of the wizards in the group.
  
Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

# EXAMPLE

    Input: strength = [1,3,1,2]
    Output: 44

Explanation: The following are all the contiguous groups of wizards:
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
- [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.

# APPROACH

Honestly speaking, this was quite a tricky question for me. 

It was easy to break this problem into sub-problems because there are several other problems where we do the same thing that we do in this problem.

Just for reference, here is one such problem -> https://leetcode.com/problems/sum-of-subarray-minimums/

Let's break down this problem into sub-problems. 

Basically, in this problem, we want to take each subarray, take its sum and multiply the sum by the minimum element of that subarray.

	For example, suppose we have strength = [4,3,1,2]
	
	All the subarrays and their min elements and sum will be 
	[4] => Minimum Element = 4 and Sum = 4
	[3] => Minimum Element = 3 and Sum = 3
	[1] => Minimum Element = 1 and Sum = 1
	[2] => Minimum Element = 2 and Sum = 2
	[4,3] => Minimum Element = 3 and Sum = 7
	[3,1] => Minimum Element = 1 and Sum = 4
	[1,2] => Minimum Element = 1 and Sum = 3
	[4,3,1] => Minimum Element = 1 and Sum = 8
	[3,1,2] => Minimum Element = 1 and Sum = 6
	[4,3,1,2] => Minimum Element = 1 and Sum = 10


So, just to group everything nicely, let's take each element and see what all subarrays are there when it is the minimum element in those subarrays.

	For element 4, we have only one subarray where it is the minimum - 
		
		[4] => Min = 4, Total Sum = 4 => 4 * 4 => 16
	
	For element 3, we have two subarrays where it is the minimum -
	
	   [3] and [4,3] => Min = 3, Total Sum = 10 => 3 * 10 => 30
	   
	For element 1, we have 6 subarrays where it is the minimum -
	
	 [1], [3,1], [1,2], [4,3,1], [3,1,2], [4,3,1,2] => Min = 1, Total Sum = 32 => 1 * 32 => 32


	For element 2, we have only one subarray where it is the minimum -
	
	[2] => Min = 2 Total Sum = 2 => 2 * 2 => 4
	

So, Overall total => 16 + 30 + 32 + 4  => 82


From this example, we see that we can divide this problem in two subproblems - 

	1. First, for each element, find what all subarrays are there in which it is the minimum
	2. Find the sum for all those subarrays and multiply that sum by the minimum element


Solving the subproblem 1 is pretty easy if you have done problems such as https://leetcode.com/problems/sum-of-subarray-minimums/

We will use stack to get the Nearest Smaller on Left & Nearest Smaller on Right data for the input list. And using that, we can then find for every index, what is the boundary.

	For example, for strength = [4,3,1,2]

	Nearest Smaller on left data = [-1,-1,-1,2]
	
	Nearest Smaller on Right Data = [1,2,4,4]
	
	Each value in above two lists is an index. 
	-1 basically means there is no smaller element to the left.
	4 means there is no smaller element to the right.
	
	So, from this data, what can we infer?
	
	Let's take the element 1 at index "2"
	
	For index = 2, NSL[2] = -1 and NSR[2] = 4
	
	It means, for element 1, there is no smaller element on left or right
	
	So, it basically means all the subarrays that have "1" in them will have "1" as the minimum element.
	
	Let's take the element 3 at index "1"
	
	For index = 1, NSL[1] = -1 and NSR[1] = 2
	
	What it  means is, all the subarrays formed between indices -1 (not including) and 2 (not including) 
	which have "3" in them, will have "3" as the minimum element. That is, [4,3] and [3]
	
So, that's how we define the boundaries for each element. 

**NOW COMES THE MOST TRICKY PART OF THIS PROBLEM!**

Now that we know what are the left and right boundaries, how can we efficiently find the sum of all the subarrays between those boundaries that contain the minimum element at index "i"?

For that, we have to take an example and try to find a generalized solution for this sub-problem.

	strength = [4,3,1,2]
	Let's also get the prefix sum = [0,4,7,8,10]
	
	Let's take the element 1 at index 2
	
	Let's take subarrays that start with index 0 and include the element "1"
	That is [4,3,1] and [4,3,1,2]
	
	Sum of subarray from index 0 to index 2 => Sum of [4,3,1] => Prefix[3] - Prefix[0] => 8 - 0 => 8
	Sum of subarray from index 0 to index 3 => Sum of [4,3,1,2] => Prefix[4] - Prefix[0] => 10 - 0 => 10
	
	Let's take subarrays that start with index 1 and include the element "1", that is [3,1] and [3,1,2]

	Sum of subarray from index 1 to index 2 => Sum of [3,1] => Prefix[3] - Prefix[1] => 8 - 4 => 4
	Sum of subarray from index 1 to index 3 => Sum of [3,1,2] => Prefix[4] - Prefix[1] => 10 - 4 => 6

	Let's take subarrays that start with index 2 and include the element "1", that is [1], [1,2]
	
	Sum of subarray from index 2 to index 2 => Sum of [1] => Prefix[3] - Prefix[2] => 8 - 7 => 1
	Sum of subarray from index 2 to index 3 => Sum of [1,2] => Prefix[4] - Prefix[2] => 10 - 7 => 3
	
	
Since we want to get the total sum of all these subarrays, let's sum up all the prefix sum equations. We get - 

	Prefix[3] - Prefix[0] + Prefix[4] - Prefix[0] + Prefix[3] - Prefix[1] + Prefix[4] - Prefix[1] + Prefix[3] - Prefix[2] + Prefix[3] - Prefix[2]
	
We can rewrite it as - 

	=> (Prefix[3] +  Prefix[4] +  Prefix[3] +  Prefix[4] +  Prefix[3] +  Prefix[4]) - (Prefix[0] + Prefix[0] + Prefix[1] + Prefix[1] + Prefix[2] + Prefix[2])

	=> 3 * (Prefix[3] +  Prefix[4])  -  2 * (Prefix[0] + Prefix[1] + Prefix[2])

	Left part of this equation is 3 * (Prefix[3] +  Prefix[4])
	Right Part of this equation is 2 * (Prefix[0] + Prefix[1] + Prefix[2])
	
Now, how can we simplify it even further? When we had to get sum of elements between any two or more continuous indices, we used a prefix sum array. But here, we have to get the sum of elements between two or more indices of prefix sum itself. That means, we will need a prefix sum of prefix sum now.

That's the whole reason why we want the Prefix Sum of Prefix Sum.

	Strength = [4,3,1,2]
	Prefix sum = [0,4,7,8,10]
	Prefix of Prefix sum = [0,0,4,11,19,29]

 Coming back to our equation 
 
	 Left part =>  3 * (Prefix[3] +  Prefix[4])
	 Right Part => 2 * (Prefix[0] + Prefix[1] + Prefix[2])

	 We can rewrite these two parts now as - 
	 
	 Left part =>  3 * (PrefixOfPrefix[5] - PrefixOfPrefix[3])
	 Right Part => 2 * (PrefixOfPrefix[3] - PrefixOfPrefix[0])
	 
What are "3" and "2" here?

These are simply the number of elements on the left of element 1(including itself) and the number of elements on the right of element 1(including itself).

**THE FINAL GENERALIZED FORMULA TO FIND THE SUM OF ALL SUBARRAYS WHERE ELEMENT AT INDEX "i" IS THE MINIMUM ELEMENT IS -**

	 Left part =>  leftCount * (PrefixOfPrefix[NSR[i] + 1] - PrefixOfPrefix[i + 1])
	 Right Part => rightCount * (PrefixOfPrefix[i + 1] - PrefixOfPrefix[NSL[i] + 1])
	
	 Total Sum = leftPart - rightPart
	
And all that's left now is to multiply this totalSum with the element at index "i" since it will be the smallest element in all the subarrays whose sum we just calculated using the above formula.