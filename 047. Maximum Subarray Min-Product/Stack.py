def maxSumMinProduct(nums):
        # Output to return
        maxMinProduct = 0
        
        # Length of the list
        n = len(nums)
        
        # Prefix Sum array
        # So that we can get the sum of any subarray in O(1) time
        prefixSum = [nums[0]];
        for i in range(1,n): prefixSum.append(nums[i] + prefixSum[i - 1])
            
        # Nearest smaller on left array
        NSL = [-1] * n
        stack = []
        for i in range(n):
            # First remove all the useless values
            # That is, all the indices in stack with greater or equal values
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
            # If stack is not empty, it means top of stack has index of nearest smaller on left
            if stack: NSL[i] = stack[-1]
                
            # Also don't forget to push current index to the stack
            stack.append(i)
            
        # Nearest smaller on right array
        NSR = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            # First remove all the useless values
            # That is, all the indices in stack with greater or equal values
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
            # If stack is not empty, it means top of stack has index of nearest smaller on left
            if stack: NSR[i] = stack[-1]
                
            # Also don't forget to push current index to the stack
            stack.append(i)
            
        # Now, once we get the nearest smaller on left and nearest smaller on right array
        # We can start with the main logic for this problem
        
        # For each number in the array
        # Consider this number to be the smallest in subarray
        # Now, we want to check how far this subarray can extend to left and right
        # Such that this number is still the smallest
        # For that, we will use NSL and NSR arrays
        # Because we can extend our subarray to left till be don't get to the NSL index
        # And same for right side
        for i in range(n):
            # Left boundary
            left = NSL[i] + 1
            
            # Right boundary
            right = NSR[i] - 1
            
            
            # What is the subarray sum
            # If NSL is -1 for any index, then it means we can take the whole subarray till right boundary
            # In other words, in that case, subarray sum will simply be = prefixSum[right]
            # That's why below check for left == 0 (since we already incremented left by 1 above)
            subarraySum = prefixSum[right] - (0 if left == 0 else prefixSum[left - 1])
            
            # And finally, update the maxMinProduct if required
            maxMinProduct = max(maxMinProduct, nums[i] * subarraySum)
            
        # Return the maximum min-product modulo 109 + 7
        return maxMinProduct % (10**9 + 7)


nums = [3,1,5,6,4,2]
print("Maximum min-product is -> ", maxSumMinProduct(nums))