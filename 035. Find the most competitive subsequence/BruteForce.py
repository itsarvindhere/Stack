def mostCompetitive(nums, k):
    # Subsequence to return
    output = []
    
    # Length of the list
    n = len(nums)
    
    i = 0
    while i < n:
        # Suppose ith element is the minimum element
        minElement = nums[i]
        
        # Index of the minimum element
        minElementIndex = i 
        
        # What is the range till which we can search for minimum element
        maxRange = n - (k - len(output))
        
        # Now, we will search and find the minimum element & its index between i + 1 and maxRange
        for j in range(i + 1, maxRange + 1):
            if nums[j] < minElement:
                minElement = nums[j]
                minElementIndex = j
        
        # Push the minimum element in the output array
        output.append(minElement)
        
        # If we got a k length subsequence, we are done
        if len(output) == k: break
        
        # If we found minimum element at "minElementIndex"
        # we can only search after that element in next iteration
        i = minElementIndex + 1
    
    return output


nums = [3,5,2,6]
k = 2

print("Most Competitive Subsequence is -> ", mostCompetitive(nums,k))