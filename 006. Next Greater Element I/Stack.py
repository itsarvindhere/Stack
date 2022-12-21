def nextGreaterElement(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
        
    output = [-1] * m
        
    # Dictionary to keep the element and its index in nums1 and for quick check if nums1 has some element or not
    indices = {}
        
    for i in range(m): indices[nums1[i]] = i
            
    # Now, simply find the next greater element in nums2 but only for those elements that are present in nums1
    stack = []
        
    for i in range(n - 1, -1, -1):
            
        # Skip the element if it is not present in nums1
        # But do not forget to push it to stack since it might be nearest greater for any other value
        if nums2[i] not in indices: 
            stack.append(nums2[i])
            continue
            
        # First remove all the useless elements
        while stack and stack[-1] <= nums2[i]: stack.pop()
                
        # If stack still has some elements, then top of stack is the nearest greater on right
        # But here, we know the output is created based on the indices in nums1
        # So here we will make use of our dictionary again
        idx = indices[nums2[i]]
            
        if stack: output[idx] = stack[-1]
                
        # And finally push the current element to stack
        stack.append(nums2[i])

    return output


nums1 = [4,1,2]
nums2 = [1,3,4,2]

print("Output -> ", nextGreaterElement(nums1, nums2))