def canSeePersonsCount(heights):
	# Length of the list
        n = len(heights)
        
        # Output list to return
        output = [0] * n
        
        # Stack
        stack = []
        
        # Loop in reverse
        for i in range(n - 1, -1, -1):
            
            # Remove all the smaller persons
            # Because the person before current person won't be able to see those at all
            # But keep in mind that current person can still see all those people that we are removing from stack
            # That's why we also keep updating the count as we pop from stack
            count = 0
            while stack and stack[-1] < heights[i]:
                count += 1
                stack.pop()
            
            # If stack is not empty, it means, there is a person that is taller than current person
            # And it is pretty obvious that the current person can see that person as well
            # So in that case, increment count by 1
            if stack: count += 1
                
            # Update the count in output list
            output[i] = count    
                
            # Don't forget to push the current height in the stack
            stack.append(heights[i])
                
        
        # Return the output list
        return output

heights = [10,6,8,5,11,9]
print("Output -> ", canSeePersonsCount(heights))