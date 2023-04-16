def totalSteps(nums):
        # Length of the input list
        n = len(nums)
        
        # Steps
        steps = 0
        
        # Stack
        stack = []
        
        # Loop in reverse
        for i in range(n - 1, -1, -1):
            # How many elements were removed for this particular element to push to stack
            # That represents the number of steps performed
            stepCount = 0
            
            # Remove all the elements on top of stack that are smaller
            while stack and stack[-1][0] < nums[i]:
                # We want to keep track of what is the maximum stepCount so far
                # That's why, we want the maximum value here
                stepCount = max(stepCount + 1, stack[-1][1])
                stack.pop()
                
            # Push the current element to stack along with the step count
            stack.append([nums[i], stepCount])
            
            # Update the steps performed
            steps = max(steps, stepCount)
        
        return steps



nums = [5,3,4,4,7,3,6,11,8,5,11]
print("Steps Taken -> ", totalSteps(nums))