class Solution:
    
    # Helper method to get the nearest smaller on left
    def getNearestSmallerOnLeft(self, nums):
        
        # Length of nums
        n = len(nums)
        
        # Output to return
        NSL = [-1] * n
        
        # Stack
        stack = []
        
        # Loop
        for i in range(n):
            
            # Remove all greater values from stack
            # Note that here, I did not do ">=" as in getNearestSmallerOnRight because we don't want to have duplicate subarrays
            while stack and nums[stack[-1]] > nums[i]: stack.pop()
                
            # If stack is not empty, the top of stack is the nearest smaller on left
            if stack: NSL[i] = stack[-1]
            
            # Put the current index in stack
            stack.append(i)

        # Return the NSL data
        return NSL
    
    # Helper method to get the nearest smaller on right
    def getNearestSmallerOnRight(self, nums):
        
        # Length of nums
        n = len(nums)
        
        # Output to return
        NSR = [n] * n
        
        # Stack
        stack = []
        
        # Loop
        for i in range(n - 1, -1, -1):
            
            # Remove all greater/equal values from stack
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
            # If stack is not empty, the top of stack is the nearest smaller on right
            if stack: NSR[i] = stack[-1]
            
            # Put the current index in stack
            stack.append(i)

        # Return the NSR data
        return NSR
    
    def totalStrength(self, strength) -> int:
        
        # Final Output to return
        output = 0
        
        # Mod
        mod = 10**9 + 7
        
        # Length of the list
        n = len(strength)
    
        
        # Data for Nearest Smaller Element on Left
        NSL = self.getNearestSmallerOnLeft(strength)
        
        # Data for Nearest Smaller Element on Right
        NSR = self.getNearestSmallerOnRight(strength)
        
        # Prefix Sum
        prefixSum = [0] * (n + 1)
        
        for i in range(1,n + 1): prefixSum[i] = prefixSum[i - 1] + strength[i - 1]
        
        # Prefix Sum of Prefix Sum
        prefixOfPrefix = [0] * (n + 2)
        
        for i in range(1,n + 2): prefixOfPrefix[i] = prefixOfPrefix[i - 1] + prefixSum[i - 1]
        
        
        # Main loop
        for i in range(n):
            
            # Left Boundary
            leftBoundary = NSL[i]
            
            # Right Boundary
            rightBoundary = NSR[i]
            
            # Elements between leftBoundary (not including) and i (including)
            leftCount = i - leftBoundary
            
            # Elements between i (including) and rightBoundary (not including)
            rightCount = rightBoundary - i
            
            # Time for the left and right parts of the equations
            leftPart = (leftCount * (prefixOfPrefix[rightBoundary + 1] - prefixOfPrefix[i + 1])) % mod
            rightPart = (rightCount * (prefixOfPrefix[i + 1] - prefixOfPrefix[leftBoundary + 1])) % mod
            
            # Total Sum of subarrays that contain "i" element as the minimum element
            totalSubarraySum = leftPart - rightPart
            
            # Finally, we can multiply this sum by minimum element and add the result to the output
            output += strength[i] * totalSubarraySum
            
            # To handle large values, use mod
            output %= mod
            
            
        # Finally return the output
        return output
    

strength = [4,3,1,2]

print("Output ->", Solution().totalStrength(strength))