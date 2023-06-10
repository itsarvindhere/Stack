def largestRectangleArea(heights) -> int:
        
        # Method to get the Nearest Smaller on Left or Right Element for each index
        def nearestSmaller(arr, start, end, increment, left):
            n = len(arr)
            
            # If there is no nearest smaller on left for any element
            # Then for that, we will put "-1"
            # And if there is no nearest smaller on right for any element
            # Then for that, we put "n"
            nearestSmallerArray = [-1 if left else n] * n
            
            stack = []
            
            # Loop 
            for i in range(start, end, increment):
                # Remove all the useless values from the stack
                # That is, all the values that are greater or equal to current value
                while stack and arr[stack[-1]] >= arr[i]: stack.pop()
                    
                # At this point, if stack has a value on top then
                # that's the nearest smaller on left/right for current element
                if stack: nearestSmallerArray[i] = stack[-1]
                    
                # Put the current index in stack as well
                stack.append(i)
                
            # Return the list
            return nearestSmallerArray
        
        # Maximum area that we have to return
        maxArea = 0
        
        # Length of the heights list
        n = len(heights)
        
        # Nearest Smaller on Left List
        NSL = nearestSmaller(heights, 0, n, 1, True)
            
        # Nearest Smaller on Right List
        NSR = nearestSmaller(heights, n - 1, -1, -1, False)
        
        # Go through each bar of the histogram
        for i in range(n):
            # Height
            height = heights[i]
            
            # Width
            width = NSR[i] - NSL[i] - 1
            
            # Update the maximum area
            maxArea = max(maxArea, height * width)
            
        # Return the maximum area
        return maxArea


heights = [2,1,5,6,2,3]

print("Area of Largest Rectangle is -> ", largestRectangleArea(heights))