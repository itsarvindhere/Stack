# PROBLEM STATEMENT

You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

# EXAMPLE

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5

Output: [9,8,6,5,3]

# APPROACH

The credits to this approach -> https://www.youtube.com/watch?v=ZHexy3JW2JA

Basically, we can divide this problem into sub problems and then solve each of the subproblem.

We want to make the maximum number by picking numbers from two different lists but the thing is we can only pick them in the same order as they appear in each of the lists.

What that means is,

    Suppose, we have nums1 = [1,8,9] and nums2 = [3,4] and k = 4

    We are asked to create the maximum number of length "4"

    In that case, we cannot pick "9" to be the first digit
    Because if we do that, then we only have two numbers left to choose from  - "3" and "4".
    We cannot choose "1" and "8" because we have already chosen "9" and we are asked to preserve the order

    So, we have to choose "8" as the first digit, "9" as second, "3" as third and "4" as forth.

    So, the output in this case will be [8,9,3,4]


So, as we see, we have to make a choice of picking numbers. We can take some amount of numbers from one list and some amount from other.
It is also possible that we take numbers from only one list.

    E.g. if nums1 = [9,9,9] and nums2 = [1,2,3] and k = 3

    Then we simply return [9,9,9] since there cannot be any greater number that we can create of length 3

    So, in this case, we picked 0 elements from second list.


So, how can we know how many numbers we should take from one list and how many we should take from the other?

Well, we cannot. So, we have to try all the possible combinations.

That is, suppose, k = 4 and nums1 = [1,2,3] and nums2 = [1,5,4]

We can either pick 0 numbers from nums1 and 4 numbers from nums2 -> Invalid since length of nums2 is "3"
We can either pick 1 number from nums1 and 3 numbers from nums2 -> [3] and [1,5,4] will be the best combo
We can either pick 2 numbers from nums1 and 2 numbers from nums2 -> [2,3] and [5,4] will be the best combo
We can either pick 3 numbers from nums1 and 1 number from nums2 -> [1,2,3] and [5] will be the best combo
We can either pick 4 numbers from nums1 and 0 number from nums2 -> Invalid since length of nums1 is "3"

Hence, for all the valid cases, we will get two lists and those two lists have to be the most optimal ones. 

That is, if we want to pick "2" numbers from nums1, that subsequence of length 2 should be the lexicographically greatest subsequence of nums1.

Once we get these two lists, now it's time to merge the two together to form one single list of length "k". We have to merge the two such that we generate the maximum possible number by combining the two.

For example, if list1 is [2,3] and list2 is [5,4] the merged result will be [5,4,2,3]

But, it is not always the case that we have different numbers in both lists.

We may encounter cases when there are same numbers so we have to choose which one to put in our merged list and what pointer to increment.

And for that case, we have to write a separate logic.

Since we want the lexicographically largest subsequence, if we have a case where both pointers are pointing to the same number, we will then compare the values after those pointers to see which subsequence will give us a bigger value first. We will then pick that subsequence.

Let's take an example to understand it - 

    Suppose, list1 is [2,1,1,0,2,0] and list2 is [1,1,1,0,2,1]

    At first, we will put the item "2" in the merged list as first digit since it is greater than "1" in list2

    so, after that pointer1 will be at index 1 in list1
    And pointer2 will still be at index 0

    And as we can see, at both pointers we have the element "1"

    So, which one to pick and which pointer to increment?

    At this point, we have to see which subarray will give us a greater element first.

    At pointer1 + 1 index we have element "1"
    But at pointer2 + 1 as well, we have "1"

    So, we increment them.

    Now, At pointer1 + 1 index we have element "0"
    But at pointer2 + 1, we have "1" 

    This means, the second subarray is lexicographically greater than first one.

    So, we will pick element at pointer2 and increment pointer2. 

This situation will come when elements are equal at both pointers.


Alright. So, let's say we formed a merged list.

Now, whether it is the maximum or not, that depends on whether it is greater than the previous merged list we formed.

So, whenever we form a merged list, we compare it with the previous one and update accordingly.

And so, finally, our output will point to the maximum number generated.
