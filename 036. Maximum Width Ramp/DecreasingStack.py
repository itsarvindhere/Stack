def maxWidthRamp(nums):
        # Maximum Width of a ramp
        maxWidth = 0
        
        # Length of the list
        n = len(nums)
        
        # Store all the useful "j" values
        stack = []
        
		# We will only push to stack
		# If either stack is empty
		# Or the current value is greater than value at top of stack
        for i in range(n-1, -1, -1):
            if not stack or nums[stack[-1]] < nums[i]: stack.append(i)
        
        # Since we filled the stack in reverse already, no need to reverse it here
        # And no need to use any index to track it as we can now treat it as a simple stack
        
        # Now, we will take each "i" value and check if top of stack has a valid :"j" value
        for i in range(n):
            # If it has, we can use it to calculate the width and now, we no longer require that j value
            # Why? because, we are starting from left to right, so as soon as an "i" makes a pair with "j"
            # It means, no other "i" after that can result in a bigger width. 
            # So it makes no sense to again check with every i between current i and the "j" on top of stack
            while stack and nums[stack[-1]] >= nums[i]:
                maxWidth = max(maxWidth, stack[-1] - i)
                stack.pop()
        
        # Return the maximum Width
        return maxWidth


nums = [6,0,8,2,1,5]
print("Maximum Width -> ", maxWidthRamp(nums))