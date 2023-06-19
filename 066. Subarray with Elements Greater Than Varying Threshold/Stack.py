def validSubarraySize(nums, threshold: int) -> int:
        # Length of the list
        n = len(nums)
        
        
        # Nearest Smaller on Left
        NSL = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
            if stack: NSL[i] = stack[-1]
                
            stack.append(i)
            
        # Nearest Smaller on Right
        NSR = [n] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
            if stack: NSR[i] = stack[-1]
                
            stack.append(i)
        
        # Now that we have NSL and NSR data HOW IS THIS HELPFUL?
        # If we take each element and consider it as minimum in any subarray
        # Then, we can easily get the length of that subarray by simply
        # checking the left and right boundaries to which the subarray will extend
        # Those boundaries are simply nearest smaller elements on left and right
        for i in range(n):
            # Left boundary
            leftBoundary = NSL[i]
            
            # Right boundary
            rightBoundary = NSR[i]
            
            # Length of the Subarray
            subarrayLength = rightBoundary - leftBoundary - 1
            
            # Check the condition
            if nums[i] > (threshold / subarrayLength): return subarrayLength
		
		# Such a subarray does not exist
        return -1


nums = [6,5,6,5,8]
threshold = 7

print("Output -> ", validSubarraySize(nums, threshold))