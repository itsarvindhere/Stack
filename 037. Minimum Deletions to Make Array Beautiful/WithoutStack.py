def minDeletion(nums):
        # Deletions Required
        deletions = 0
        
        # Length of the list
        n = len(nums)
        
        # Why we are using a stack in above approach?
        # We are using it just to compare current element with previous if current index is odd
        # So can we do this without a stack and in O(1) space?
        previousElement = nums[0]
        
        for i in range(1,n):
            # Instead of actually deleting elements and then shifting next elements to left
            # We can easily convert current index to the index that it would be 
            # after we have deleted some elements before it
            # That would simply be (current index - how many elements we have deleted so far)
            indexAfterDelete = i - deletions
            
            # If the index that we would be at (if we had actually deleted the elements) is odd
            # And it has the same element as at the "even" index before it, we need to delete this one
            if indexAfterDelete%2 != 0 and previousElement == nums[i]: deletions += 1   
            # Otherwise, this is not deleted to this will make it to the final beautiful array
            else: previousElement = nums[i]
    
        # Since we also want to ensure that our list is of an even length
        # If after removing elements, we still have odd number of elements
        # It means, we have to delete one more element to make the array beautiful
        if (n - deletions) % 2 != 0: deletions += 1
        
        # Return the number of deletions
        return deletions


nums = [1,1,2,2,3,3]
print("Minimum Deletions Required -> ", minDeletion(nums))