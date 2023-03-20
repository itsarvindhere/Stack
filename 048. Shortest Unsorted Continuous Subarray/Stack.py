def findUnsortedSubarray(nums):
    # Length of the input list
    n = len(nums)
        
    # Find nearest smaller element on right
    NSR = [-1] * n
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]: stack.pop()
                
        if stack: NSR[i] = stack[-1]
                
        stack.append(i)
            
    # Find the Nearest Greater on left
    NGL = [-1] * n
    stack = []
        
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]: stack.pop()
                
        if stack: NGL[i] = stack[-1]
                
        stack.append(i)
            
    # Now,  we have the Nearest Smaller on Right & Nearest Greater on Left data
    # So now, the beginnig of the unsorted subarray will be the leftmost index that has a smaller element on right
    # Similarly, the end of the unsorted subarray will be the rightmost index that has a greater element on left
                    
    # Find the beginning of the unsorted subarray
    i = 0
    while i < n and NSR[i] == -1: i += 1
        
    # Find the end of unsorted subarray
    j = n - 1
    while j >= i and NGL[j] == -1: j -= 1
            
    return j - i + 1


nums = [2,6,4,8,10,9,15]

print("Length of shortest unsorted subarray is -> ", findUnsortedSubarray(nums))