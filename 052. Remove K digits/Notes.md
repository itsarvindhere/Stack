# PROBLEM STATEMENT

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# EXAMPLE

    Input: num = "1432219", k = 3
    Output: "1219"

Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# STACK APPROACH

This is one of those problems where we have to make use of a stack.

Why?

See, we have to remove the "k" digits, right? And we also want to get the smallest possible number after removing those "k" digits.

So, it should be obvious that if we remove the numbers from the beginning, then we have a better chance to get a smaller number.

	Take this as example -> 4398 and k = 1
	
	Even though we have "9" and "8" that are the bigger numbers
	We still get a smallest number if we remove the first digit "4".
	
	So, we have to greedily try to remove elements from beginning first.
	
	And only if we cannot remove enough elements this way, we will try to remove from end.
	
Now, on what basis we remove? Why did we chose "4" in above example?

That's because, if we traverse this string, then when we are at the digit "3", we see that there is a greater digit before it. So, removing it will ensure that we get a smaller overall number.

And that's the main idea. We have to keep track of previous digits and at any time if the current digit is smaller than previous, we can remove the previous digit.

And to check the previous digits, we can use a stack.

As mentioned above, if we are not able to remove "k" elements using this logic, we then have to remove the remaining elements from the end.