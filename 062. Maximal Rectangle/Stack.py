def maximalRectangle(matrix) -> int:

        # STEP 1 - TAKE EACH LEVEL AND GET THE RESULTING HISTORGRAM AFTER COMBINING PREVIOUS LEVELS
        
        # Rows
        rows = len(matrix)
        
        # Columns
        cols = len(matrix[0])
    
        # First histogram is just the first row
        histograms = [[int(x) for x in matrix[0]]]
        
        # Previous histogram
        prevHistogram = histograms[0]
        
        # Start with 2nd row
        for row in range(1,rows):
            # Current histogram
            histogram = []
            # Go through each column of this row
            for col in range(cols):
                # If this is a 0, it represents ground floor
                # So, then, at this index, there will be no building i.e., height = 0
                if matrix[row][col] == "0": histogram.append(0)
                # Otherwise, combine the current height and height of building at this index in previous histogram
                else:
                    histogram.append(int(matrix[row][col]) + prevHistogram[col])
                    
                    
            # Now, put this histogram in list of histograms
            histograms.append(histogram)
            
            # And also update previous histogram
            prevHistogram = histogram
            
            
        # STEP 2 - NOW, TAKE EACH HISTOGRAM, FIND THE MAXIMUM AREA, AND UPDATE THE MAXIMUM AREA OF MATRIX IF REQUIRED 
        
        # Recall how we used to find the Maximal Rectangle in a Histogram
        # We used to make use of Nearest Smaller on Left & Nearest Smaller on Right Data for each index
        
        # Method that takes a 1D array and gives us the Nearest Smaller on Left data for each index
        def nearestSmallerOnLeft(arr):        
            NSL = [-1] * len(arr)
            
            stack = []
            
            for i in range(len(arr)):
                while stack and arr[stack[-1]] >= arr[i]: stack.pop()
                
                # IF stack is not empty, top index is the Nearest Smaller on Left Index for this element
                if stack: NSL[i] = stack[-1]
                    
                # Push this index to stack
                stack.append(i)
                
                
            # Return the NSL array
            return NSL
        
        # Method that takes a 1D array and gives us the Nearest Smaller on Right data for each index
        def nearestSmallerOnRight(arr):        
            NSR = [len(arr)] * len(arr)
            
            stack = []
            
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]: stack.pop()
                
                # IF stack is not empty, top index is the Nearest Smaller on Right Index for this element
                if stack: NSR[i] = stack[-1]
                    
                # Push this index to stack
                stack.append(i)
                
                
            # Return the NSR array
            return NSR
        
        # Method that takes a 1D array and gives us the area of the largest rectangle in this array / histogram
        def maximalAreaInHistogram(arr):
            NSL = nearestSmallerOnLeft(arr)
            NSR = nearestSmallerOnRight(arr)
            
            # Maximum Area
            maxArea = 0
            
            # Find the maximum area of a rectangle in this array
            for i in range(len(arr)):
                height = arr[i]
                leftBoundary = NSL[i] + 1
                rightBoundary = NSR[i] - 1
                
                width = rightBoundary - leftBoundary + 1
                
                maxArea = max(maxArea, height * width)
            
            # Return the maximum area
            return maxArea
            
        # Now, we can go through each histogram and find the maximum area
        maxAreaInMatrix = 0
        for histogram in histograms: maxAreaInMatrix = max(maxAreaInMatrix, maximalAreaInHistogram(histogram))

        # Return the maximum Area in the Matrix
        return maxAreaInMatrix


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print("Maximum Area is -> ", maximalRectangle(matrix))