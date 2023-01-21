def subArrayRanges(nums):
    # Range sum that we have to find
    rangeSum = 0
    
    # Length of the list
    n = len(nums)
    
    # Go through each starting element of a subarray
    for i in range(n):
        # Assume this is the maximum as well as the minimum element of the subarray
        maxElement = nums[i]
        minElement = nums[i]
        for j in range(i + 1, n):
            # Update the maximum and minimum elements if required
            maxElement = max(maxElement, nums[j])
            minElement = min(minElement, nums[j])
            
            # Find the range of this subarray and add it to the Range sum
            rangeSum += maxElement - minElement
            
    
    # Finally, return the Range sum
    return rangeSum

nums = [1,3,3]
print("Sum of Subarray Ranges -> ", subArrayRanges(nums))