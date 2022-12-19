# PROBLEM STATEMENT

You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

# EXAMPLE

    Input: prices = [8,4,6,2,3]
    Output: [4,2,4,2,3]

Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.

# **1. BRUTE FORCE APPROACH - O(N^2)**

The Brute Force solution will be accepted because the prices array can have at most 500 values. But from here, we can think of optimizing this solution.

Basically, this is a variation of the "Nearest Smaller on Right" problem. The only slight difference is that here, we want the "Nearest Smaller or Equal on the Right".

In Brute Force approach, for each price, we have to look at every other price on its right till we do not find a price that is less or equal. If there is no price at all which satisfies this condition, we will have to traverse the array till the end which is not efficient.	
		
# **2. STACK APPROACH - O(N)**

Using a stack, we can optimize the code such that each price is pushed or popped only once. So for a price, we do not have to go through all the values to its right. Using a stack, we will first remove all the useless values. That is, all those prices that are greater than the current price because they are of no use to us. 

And then, we know that if stack still has some values, then the topmost value will be the one that we are looking for. And if the stack does not have any values at this point, it simply means there is no price on right that is <= current price.
