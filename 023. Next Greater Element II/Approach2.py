def nextGreaterElements(nums):
    # length of the input list
    n = len(nums)
        
    # Output to return
    output = [-1] * n
        
    # Stack that we will use to eficiently find Nearest Greater Element on Right
    stack = []
        
    for i in range((2 * n) - 1, -1, -1):
        # Remove all the useless values
        # That is, all the values that are smaller than current value
        while stack and stack[-1] <= nums[i % n]: stack.pop()
            
        # If the stack still has some value on top, it means, it is the nearest greater on right
        # Do note that since we are looping twice but the output array is of original length only
        # We also need to take care of the index (i) values greater than original length
        if stack: output[i % n] = stack[-1]
            
        stack.append(nums[i % n])
        
    return output

nums = [1,2,3,4,3]
print("Output -> ", nextGreaterElements(nums))