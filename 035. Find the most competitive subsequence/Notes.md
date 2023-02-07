# PROBLEM STATEMENT

Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

# EXAMPLE

    Input: nums = [3,5,2,6], k = 2
    Output: [2,6]

Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.


# **1. BRUTE FORCE APPROACH - O(N^2) - TLE**
In this problem, we are asked to return a "subsequence" of length "k" which is the most competitive. Basically, most competitive means, whatever element we choose, it is the smallest in its range. 

Now the question is - What is this range?

Let me explain with an example. 

	Suppose, we have nums = [3,5,2,1], k = 2
	
	Now, since we want to pick 2 elements for our subsequence, doesn't it make sense 
	that the first element we choose for our subsequence has to be the smallest among the first three elements only?
	
	Because, if we consider the fourth element (1 in this case) as well, then the first element of subsequence will be 1.
	
	But what about the second element? We no longer have any element left to pick after 1. 
	
	Hence, for first element, our search for a minimum element is restricted till the index = 2. 
	
	Think of what would happen if k was 3 in this example?
	
	In that case, our search would be restricted till index = 2. 
	
	Because the first element of our final subsequence can be the smaller among "3" and "5" only.
	
	And then, the rest of the two elements "2" and "1" will be the 2nd and 3rd elements respectively of our final subsequence.
	
	
And so, we can conclude that at any point, our search is restricted between previous minimum element's index and the index after which we have same number of values left as the remaining elements that we have to pick for subsequence.

	For example, in [3,5,2,1], k = 2
	
	When we are at 0th index, that is, when the loop begins with i = 0
	
	We can search for minimum element from i = 0 to i = 2
	
	And whatever we get, that would be the first element of subsequence of length k.
	
	Because after index = 2, we have only one element in the array. 
	And after current iteration, we will have to find only one more element for our subsequence as well.
	
So that's the logic of the Brute Force approach.
	
Yes, it will give TLE but from here, we can start to think of how to optimize the code so that it get accepted.
		
# **2. STACK APPROACH - O(N)**

The simplest way to know whether stack can be used to optimize any code with nested loop is to check whether the value of inner loop's variable depends on outer loop's variable. And as we can see in Brute Force approach, the value of "j" indeed depends on value of "i" (j = i + 1).

So, we can use a stack here to bring the complexity down from O(N^2) to O(N).

What we will do is, we will still loop from beginning to end and in each iteration, we will check if the element on top of stack is greater than the current element in the loop or not. If yes, it means for our subsequence we may very well choose the current loop's element instead of the element on top of stack.

But as in Brute Force approach, we also need to make sure we have enough elements left after index "i" from which we can choose the number of elements that are left to have in the subsequence. If not, then there is no other way but to keep both elements. That is, whatever we have on top of stack and whatever is the current element.

The comments in the code will explain how we decide whether to pop or not. That is, whether to replace the top element with the ith element or to not pop and keep both.