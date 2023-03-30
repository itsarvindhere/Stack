def find132pattern(nums) -> bool:
        # Length of the list
        n = len(nums)
        
        # Since i needs to be the smallest of the three values
        # Let's create an array to store the smallest element so far on left
        minOnLeft = [0] * n
        minOnLeft[0] = nums[0]
        for i in range(1,n): minOnLeft[i] = min(nums[i], minOnLeft[i - 1])
                
                
        # Monotonically Decreasing Stack
        # Meaning, the value on top is the smallest value in the stack
        # And the value on the bottom is the largest in the stack
        # Since it is going to be monotonically decreasing, we can only push if order is not disturbed
        # That is, suppose we have a value "x" on top of stack and a new value "y" needs to be pushed
        # But "y" is greater than "x". Since we want a monotonically decreasing stack, it means, 
        # "x" has to be removed first before pushing y so that order is maintained
        stack = []
        
        # We take each index as the "k" value
        # And try to see if we have a "j" and an "i" value satisfying the "132" criteria
        # BTW we can start from index 2 since index 0 and index 1 can never be "k"
        # But just to keep everything simple, we can start from beginning
        for k in range(n):
            
            # Make sure order is maintained
            # Hence, remove all the values that are not greater than current value
            while stack and nums[stack[-1]] <= nums[k]: stack.pop()
                
            # At this point, if stack is not empty, it means
            # There is a value before current "k" value that is greater
            # So that can be our "j" value
            
            # Also, if the current value is greater than the minimum value on the left of this "j" value
            # Then we found our 132 pattern
            if stack and nums[k] > minOnLeft[stack[-1]]: return True
            
            stack.append(k)
        
                
        return False


nums = [3,1,4,2]

print("Is 132 Pattern Present? ", find132pattern(nums))