def find132pattern(nums) -> bool:
        # Length of the list
        n = len(nums)
        
        # For each i
        for i in range(n):
            # Go through each possible j
            for j in range(i + 1, n):
                # Go through each possible k
                for k in range(j + 1, n):
                    # If condition is satisfied return True
                    if (nums[i] < nums[k]) and (nums[k] < nums[j]): return True
        
        # There is no 132 Pattern
        return False

nums = [3,1,4,2]

print("Is 132 Pattern Present? ", find132pattern(nums))