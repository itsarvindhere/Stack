def find132pattern(nums) -> bool:
        # Length of the list
        n = len(nums)
        
        # Since i needs to be the smallest of the three values
        # Let's create an array to store the index of smallest element so far on left
        smallestSoFar = [0] * n
        
        for i in range(1,n): 
            if nums[smallestSoFar[i - 1]] < nums[i]: smallestSoFar[i] = smallestSoFar[i - 1]
            else: smallestSoFar[i] = i
                           
        # We will fix "j" and then try to find i and k
        for j in range(n):
            
            # i is the index of the smallest element in the range [0,j]
            i = smallestSoFar[j]
            
            # Since i needs to be less than j, we need to skip if i == j
            if i == j: continue
            
            # Otherwise, now we have "i" and "j"
            # So to find "k", we just need to search on right of "j" and find a value 
            # that is greater than value at "i" but smaller than value at "j"
            for k in range(j + 1, n):
                # If we found a 132 pattern, return True
                if nums[k] > nums[i] and nums[k] < nums[j]: return True
        
        return False

nums = [3,1,4,2]

print("Is 132 Pattern Present? ", find132pattern(nums))