def nextGreaterElement(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
        
    output = [-1] * m
        
    # Dictionary to keep the element and its index in nums1 and for quick check if nums1 has some element or not
    indices = {}
        
    for i in range(m): indices[nums1[i]] = i
        
    # Now, for each element in nums2, just find its Nearest Greater on Right if this element is present in nums1 as well
    for i in range(n):
        # Skip if this element is not present in nums1
        if nums2[i] not in indices: continue
                
        # If it is present, find its nearest greater on right
        for j in range(i + 1, n):
                
            # If Nearest Greater is found
            if nums2[j] > nums2[i]:
                # Get the index of this element in nums1
                idx = indices[nums2[i]]
                    
                # And now put the value at this index in output array
                output[idx] = nums2[j]
                    
                # Stop
                break       
    return output


nums1 = [4,1,2]
nums2 = [1,3,4,2]

print("Output -> ", nextGreaterElement(nums1, nums2))