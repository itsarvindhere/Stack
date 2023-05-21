def maximumScore(nums, k: int) -> int:
        # Length of the list
        n = len(nums)
        
        # Max Score to Return
        maxScore = 0
        
        # Nearest Smaller Index on Left
        NSL = [-1] * n
        
        stack = []
        
        # Traverse from Left to Right
        for i in range(n):
            # If the top element is greater, remove it
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
            # At this point, if stack is not empty
            # Then top of stack has index of the nearest smaller element on the left
            if stack: NSL[i] = stack[-1]
                
            # Push current element to stack as well
            stack.append(i)
            
        # Nearest Smaller Index on Right
        NSR = [n] * n
        
        stack = []
        
        # Traverse from Right to Left
        for i in range(n - 1, -1, -1):
            # If the top element is greater, remove it
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
            # At this point, if stack is not empty
            # Then top of stack has the index of nearest smaller element on the right
            if stack: NSR[i] = stack[-1]
                
            # Push current element to stack as well
            stack.append(i)
        
        # Now, we calculate the area of the rectangle
        for i in range(n):
            
            # What is the left boundary
            leftBoundary = NSL[i] + 1
            
            # What is the right boundary
            rightBoundary = NSR[i] - 1
            
            # Height of the current block
            height = nums[i]
            
            
            # Now, we can update our maximum score based on the area that we get
            # Note that we are given "k" and that "k" should be >= i and <= j
            # In simple words, whatever rectangle we take, it should have the index "k" in it
            # So, we have to also check that the current rectangle has the index k inside it
            if leftBoundary <= k and rightBoundary >= k:
                
                # What is the area?
                area = ((rightBoundary - leftBoundary) + 1) * height
                
                # Update the maximum score
                maxScore = max(maxScore,area)
        # Return the maximum Score of a good subarray
        return maxScore


nums = [5,5,4,5,4,1,1,1]
k = 0

print("Maximum Score is ", maximumScore(nums,k))