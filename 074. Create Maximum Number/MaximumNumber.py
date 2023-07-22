class Solution:
    # Helper method to get the greatest subsequence out of a list of a given length
    def getGreatestSubsequence(self, nums, subsequenceLength):
        # Length of the list
        n = len(nums)
        
        # Stack to efficiently compare numbers
        stack = []
        
        # Loop over the list
        for i in range(n):
            
            # If current element is greater than element on top of stack
            # We can remove it
            # But only if we have enough elements to put in stack so that required subsequenceLength is matched
            # (n-i) gives us the remaining elements to traverse
            # (len(stack) - 1) gives us the length of stack if we pop one element
            # So, what we are saying is "The elements in stack after we pop + elements left to traverse" should be >= subsequenceLength
            # Only then we can pop
            while stack and stack[-1] < nums[i] and (n - i) + (len(stack) - 1) >= subsequenceLength: stack.pop()
                
            
            # Now we can put the index of current element in the stack (only if we don't already have 'subsequenceLength' elements in the stack)
            if len(stack) < subsequenceLength: stack.append(nums[i])
            
        # Return this stack
        return stack
            
    # Helper method to compare subarrays of two lists such that one starts at index i and the other at index j
    # We do this comparison when we have same value at the two pointers so we have to decide which one to choose
    def isGreater(self, nums1, nums2, i, j):
        
        # Length of first list
        m = len(nums1)
        
        # Length of second list
        n = len(nums2)
        
        # While Loop to compare by positions
        while i < m or j < n:
            
            # If indices go out of bounds
            
            # If i is >= m, then nums1 is not lexicographically greater than nums2
            if i >= m: return False
            
            # If j is >= n, then nums1 is lexicographically greater than nums2
            elif j >= n: return True
        
            # If indices are not out of bounds, we can compare the elements
            
            # If "i" element in nums1 is greater than "j" element in nums2
            # Then nums1 is lexicographically greater than nums2
            elif nums1[i] > nums2[j]: return True
            
            # If "i" element in nums1 is smaller than "j" element in nums2
            # Then nums1 is not lexicographically greater than nums2
            elif nums1[i] < nums2[j]: return False
            
            # If both are equal, move on to next comparison
            i += 1
            j += 1
            
        # If we didn't return anything, then both subarrays are the same
        # So we can return either True or False since we can choose any of the two
        # Let's return true
        return True
            
    def maxNumber(self, nums1, nums2, k: int):
        
        # Final output to return
        output = []
        
        # If we had only one list then it would've been super simple 
        # to get a lexicographically greatest number
        # But, in this problem, we have two numbers
        # And what we don't exactly know is, how many numbers we should take from nums1 and how many from nums2
        
        
        # Since k <= m + n
        # We can try every possible combination. Since m and n can be at most 500 so it shouldn't give us TLE
        
        # For example, if k = 5 then we can maybe take 1 number from nums1 and 4 from nums2
        # Or maybe take 2 from nums1 and 3 from nums2
        # And so on...
        
        # And then, we will merge the two lists that we will get to get the final output
        # And return the output that gives us the maximum number
        
        # So, first step is to go through every possible choice of taking numbers from nums1 and nums2
        for count in range(k + 1):
            
            # Suppose k = 5 but nums1 has only 2 elements
            # In that case, we can only pick either 0 or 1 or 2 elements from nums1
            # It doesn't make sense when we say pick "3" elements from nums1 and "2" from nums2
            # Because nums1 doesn't even have 3 elements in the first place
            # So, in such case, we won't do anything and we will move on to next combination
            if count > len(nums1) or (k - count) > len(nums2): continue
            
            list1 = self.getGreatestSubsequence(nums1, count)
            list2 = self.getGreatestSubsequence(nums2, k - count)
            
            # After we get the two lists, we will now merge them
            mergedList = []
            
            # Pointers for the two lists
            i,j = 0,0
            
            # While Loop to compare by positions
            while i < len(list1) or j < len(list2):

                # If indices go out of bounds

                # If i is >= m, then pick "j" element in list2
                if i >= len(list1): 
                    mergedList.append(list2[j])
                    j += 1

                # If j is >= n, then pick "i" element in list1
                elif j >= len(list2):
                    mergedList.append(list1[i])
                    i += 1
                    
                    
                # If indices are not out of bounds, we can compare the elements

                # If "i" element in nums1 is greater than "j" element in nums2
                # Then pick the i element of nums1
                elif list1[i] > list2[j]: 
                    mergedList.append(list1[i])
                    i += 1

                # If "i" element in nums1 is smaller than "j" element in nums2
                # Then pick the j element of nums2
                elif list1[i] < list2[j]: 
                    mergedList.append(list2[j])
                    j += 1

                # If both are equal, we use the helper method to choose 
                else:
                    # If subsequence of nums1 starting at index "i"
                    # if lexicographically greater than subsequence of nums2 starting at "j"
                    # We pick the i element
                    if self.isGreater(list1, list2, i, j):
                        mergedList.append(list1[i])
                        i += 1
                        
                    # Otherwise, we pick the "j" element
                    else:
                        mergedList.append(list2[j])
                        j += 1
            
            
            # Finally, we get our merged list
            # Now we can compare it with previous merged list to see which one is the bigger lexicographically
            # Based on that we can update the output list
            if output < mergedList: output = mergedList
        return output
    


solution = Solution();


nums1 = [3,4,6,5]
nums2 = [9,1,2,5,8,3]
k = 5
print("Output is -> ",solution.maxNumber(nums1,nums2,k));