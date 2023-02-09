def maxWidthRamp(nums):
        # Maximum Width of a ramp
        maxWidth = 0
        
        # Length of the list
        n = len(nums)
        
        i = 0
        
        # Index from which we will start looking for a valid "j" value for a given "i" value
        startingIndexForCheck = 0
        
        # Go through each possible "i" value
        while i < n:
            # For each i value, instead of checking all the j values
            # We can start from the previous rightmost range that we got
            # Because it makes no sense to check indices between because the maxWidth will always be smaller than before
            startingIndexForCheck = max(startingIndexForCheck, i)
            
            for j in range(startingIndexForCheck + 1, n):
                # If it satisfies the condition, update the maxWidth if required
                if nums[i] <= nums[j]: 
                    maxWidth = max(maxWidth, j - i)
                    startingIndexForCheck = j
                    
            i += 1
                    
        # Return the maximum Width
        return maxWidth


nums = [6,0,8,2,1,5]

print("Maximum Width -> ", maxWidthRamp(nums))