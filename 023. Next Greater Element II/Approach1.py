def nextGreaterElements(nums):
    # Original length
    ogLength = len(nums)
        
    # Output to return
    output = [-1] * ogLength

    # We can double the array to simulate a circular array
    # e.g if we have [1,2,3] and we double it, we get [1,2,3,1,2,3]
    # So the after the "3", we have "1", just how we want it to be as per the problem
    nums *= 2
    n = len(nums)

    # Stack that we will use to eficiently find Nearest Greater Element on Right
    stack = []
        
    for i in range(n - 1, -1, -1):
        # Remove all the useless values
        # That is, all the values that are smaller than current value
        while stack and stack[-1] <= nums[i]: stack.pop()
            
        # If the stack still has some value on top, it means, it is the nearest greater on right
        # Do note that since array length is double but the output array is of the original length
        # We also need to take care of the index (i) values greater than original length
        if stack: output[i % ogLength] = stack[-1]
            
        stack.append(nums[i])
        
    return output

nums = [1,2,3,4,3]
print("Output -> ", nextGreaterElements(nums))