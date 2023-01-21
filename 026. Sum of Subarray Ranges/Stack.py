# To find the Sum of Subarray minimums
def sumSubarrayMins(arr):
    # Length of the list
    n = len(arr)
        
    # Total Sum of minimums that we have to return
    totalSum = 0
        
    # Keep track of Nearest Smaller Elements on Left and Right
    # Notice how we initialized them with -1 and n.
    # Because, if for any element, nearest smaller index on left is -1, it means there is no smaller element to its left
    # ANd similarly, if for any element, nearest smaller index on right is n, it means there is no smaller element to its right
    NSL, NSR = [-1] * n, [n] * n
        
    # Stacks that we will use to find Nearest Smaller on Left & Nearest Smaller on Right
    stack = []
        
    # Length of the given list
    n = len(arr)
        
    # First, let's find nearest smaller index on left for each element
    # Since for each element, we want to look on left of it
    # We will loop in reverse of that. That is, from left to right
    for i in range(n):
            
        # Remove all the useless elements from top of stack
        # That is, all those elements that are greater or equal to ith element
        while stack and arr[stack[-1]] >= arr[i]: stack.pop()
        
        # If stack is not empty at this point, it means, top of stack has index of nearest smaller on left
        if stack: NSL[i] = stack[-1]
                
        # And just push ith element to stack as well
        stack.append(i)
            
            
    # Next, let's find nearest smaller index on left for each element
    # Since for each element, we want to look on right of it
    # We will loop in reverse of that. That is, from right to left
    stack.clear()
        
    for i in range(n - 1, -1, -1):
            
        # Remove all the useless elements from top of stack
        # That is, all those elements that are greater than ith element
        while stack and arr[stack[-1]] > arr[i]: stack.pop()
        
        # If stack is not empty at this point, it means, top of stack has index of nearest smaller on left
        if stack: NSR[i] = stack[-1]
                
        # And just push ith element to stack as well
        stack.append(i)
            
            
    # Now, for each element, the number of subarrays in which it is minimum is 
    # (Elements between it and NSL) * (Elements between it and NSR)
    for i in range(n): 
        # Count of elements between NSL[i] and i
        leftCount = i - NSL[i]
            
        # Count of elements between NSR[i] and i
        rightCount = NSR[i] - i
            
        # Count of subarrays
        subarrayCount = leftCount * rightCount
            
        # Add the contribution of this element in the totalSum
        totalSum += (arr[i] * subarrayCount)
            
    return totalSum
    
# To find the Sum of Subarray Maximums
def sumSubarrayMax(arr):
    # Length of the list
    n = len(arr)
        
    # Total Sum of maximums that we have to return
    totalSum = 0
        
    # Keep track of Nearest Greater Element on Left and Right
    # Notice how we initialized them with -1 and n.
    # Because, if for any element, nearest greater index on left is -1, it means there is no greater element to its left
    # ANd similarly, if for any element, nearest greater index on right is n, it means there is no greater element to its right
    NGL, NGR = [-1] * n, [n] * n
        
    # Stacks that we will use to find Nearest Greater on Left & Nearest Greater on Right
    stack = []
        
    # Length of the given list
    n = len(arr)
        
    # First, let's find nearest Greater index on left for each element
    # Since for each element, we want to look on left of it
    # We will loop in reverse of that. That is, from left to right
    for i in range(n):
            
        # Remove all the useless elements from top of stack
        # That is, all those elements that are smaller or equal to ith element
        while stack and arr[stack[-1]] <= arr[i]: stack.pop()
        
        # If stack is not empty at this point, it means, top of stack has index of nearest greater on left
        if stack: NGL[i] = stack[-1]
                
        # And just push ith element to stack as well
        stack.append(i)
            
            
    # Next, let's find nearest greater index on right for each element
    # Since for each element, we want to look on right of it
    # We will loop in reverse of that. That is, from right to left
    stack.clear()
        
    for i in range(n - 1, -1, -1):
            
        # Remove all the useless elements from top of stack
        # That is, all those elements that are smaller than ith element
        while stack and arr[stack[-1]] < arr[i]: stack.pop()
        
        # If stack is not empty at this point, it means, top of stack has index of nearest smaller on left
        if stack: NGR[i] = stack[-1]
                
        # And just push ith element to stack as well
        stack.append(i)
            
            
    # Now, for each element, the number of subarrays in which it is maximum is 
    # (Elements between it and NGL) * (Elements between it and NGR)
    for i in range(n): 
        # Count of elements between NSL[i] and i
        leftCount = i - NGL[i]
            
        # Count of elements between NSR[i] and i
        rightCount = NGR[i] - i
            
        # Count of subarrays
        subarrayCount = leftCount * rightCount
            
        # Add the contribution of this element in the totalSum
        totalSum += (arr[i] * subarrayCount)
            
    return totalSum
    
def subArrayRanges(nums):
    return sumSubarrayMax(nums) - sumSubarrayMins(nums)

nums = [1,3,3]
print("Sum of Subarray Ranges -> ", subArrayRanges(nums))