def secondGreaterElement(nums):
        # Length of the list
        n = len(nums)
        
        # Output list to return
        output = [-1] * n
        
        # Stack 1 -> Keep Elements with no next greater element
        stack1 = []
        
        # Stack 2 -> Keep Elements with next greater element
        stack2 = []
        
        for i in range(n):
            
            # We know stack2 has all those elements that have next greater
            # So, if current "i" element is greater than element on top of stack
            # It just means, for that top element, the 2nd greater is "i" element
            # And the same will be case for all such elements in stack2
            while stack2 and nums[stack2[-1]] < nums[i]: output[stack2.pop()] = nums[i]
                
            # We know that stack1 has all those elements that have no next greater
            # So if current "i" is greater than top of stack1, it means
            # The element on top of stack1 has found its next greater element
            
            # Note that we cannot simply pop and put elements from stack1 to stack2
            # We want to maintain the order
            # So, we have to first push the elements in a temporary stack
            # And then from that temp stack to the stack2
            # So that order is same as in stack1
            tempStack = []
            while stack1 and nums[stack1[-1]] < nums[i]: tempStack.append(stack1.pop())
            
            while tempStack: stack2.append(tempStack.pop())
                
            stack1.append(i)
                 
        # Finally, return the output list
        return output

nums = [2,4,0,9,6]

print("Output is -> ", secondGreaterElement(nums))