# PROBLEM STATEMENT

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# EXAMPLE

    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]

Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# BRUTE FORCE APPROACH

Yes ths problem can be solved using a Brute Force approach but that's not the tricky part. The tricky part is how to optimize the Brute Force solution using Stack.

If you can write the Brute Force solution correctly, the Stack solution is super easy.

First, we want to keep track of what is the index of an element in nums1. Because output array is created based on the index of an element in nums1, not in nums2. Moreover, using a Dictionary will also help in quickly checking whether an element is present in nums1 or not.

So, now that our dictionary is ready, we will go through each element in nums2 and if that element is present in nums1, then we will calculate its nearest greater element on right side. If it is not present, no need to do anything and we can skip.

And when we put the value in output array if we found the Nearest Greater on Right, we will use the index of that element in nums1. For this, again we will make use of our Dictionary.

# STACK APPROACH

Using a Stack, we can optimize the process of finding Nearest Greater on Right. So that, the time complexity comes down to O(N) to find NGR instead of O(N^2).


