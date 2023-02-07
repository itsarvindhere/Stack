def mostCompetitive(nums, k):
        # Stack that we will use to build a k-length subsequence
        stack = []
        
        # Length of the list
        n = len(nums)
        
        # Go through each element in the list
        for i,num in enumerate(nums):
            # If this element is smaller than previous element, that means
            # We may replace the previous element with this element
            # Since we want to make sure our subsequence is the most competitive one
            # But as we saw in brute force approach, we also need to make sure about elements left to choose
            # We do not want to remove any element from stack and eventually have less than k elements in it
            
            # So, we can only pop from stack, if we know that after "ith" index, 
            # we still have enough values to pick to make sure we get a k length subsequence
            
            # Suppose the ith element is smaller than what the top of stack has
            # So, if we have to pop the element at top of stack, then
            
            # How many elements are left to pick -> How many we have to pick - how many we have picked
            # We have picked same numbers of elements as the (length of stack - 1) 
            # Why minus 1? Because we are assuming we have to pop since ith element is smaller than top of stack
            
            # And total we have to pick are "k" elements
            # So, elements left to pick -> k - (len(stack) - 1)

            # Hence, we want to make sure the number of values left to traverse after "i" index
            # Are at least equal to number of values we have to pick for our subsequence
            # Number of values after "i" index => (n - i)

            # Hence, the conditions becomes -> n - i >= k - (len(stack) - 1)
            
            
            while stack and stack[-1] > num and n - i >= k - (len(stack) - 1): stack.pop()
                
            # Now push the current element on top of stack
            stack.append(num)

        # Since we want only the "k" length subsequence, just return first k elements
        return stack[:k]


nums = [3,5,2,6]
k = 2

print("Most Competitive Subsequence is -> ", mostCompetitive(nums,k))