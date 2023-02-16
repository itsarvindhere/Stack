def lengthLongestPath(input: str) -> int:
        # Maximum Length of a path
        maxLength = 0
        
        # Stack that we will use to keep track of levels and the substrings at that level
        stack = []
        
        # Split the input at the newline characters
        input = input.split("\n")
        
        # Length of input
        n = len(input)
        
        # Length of the path
        # We will build this length as we traverse the input
        pathLength = 0
        
        i = 0
        while i < n:
            string = input[i]
            
            # How many tabs are there (This will represent the level)
            # Find the rightmost index of "\t"
            # In this way, (rightIndex + 1) will give us the count
            currLevel = string.rfind("\t") + 1
            
            # Length of string without the tabs
            stringLength = len(string) - currLevel
            
            # If the stack is not empty, only then do the below checks
            if stack:
                # If current level is same as previous level
                if currLevel == stack[-1][0]:
                    # We will remove all the pairs where level is the same
                    # Also make sure to decrement the currLength accordingly
                    while stack and stack[-1][0] == currLevel: pathLength -= stack.pop()[1]
                # If current level is smaller than previous level
                elif currLevel < stack[-1][0]:
                    while stack and stack[-1][0] + 1 != currLevel: pathLength -= stack.pop()[1]
            
            # Push to the stack
            stack.append((currLevel, stringLength))
            pathLength += stringLength
            
            # If this string represents a file
            if "." in string:
                # Note that we also have to add a "/" in the path
                # The number of "/" we have to add in the path is = (length of stack - 1)
                # Minus 1 because we will not add a slash at the end of the path
                maxLength = max(maxLength, pathLength + len(stack) - 1)
                
            i += 1
        
        return maxLength

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print("Length of Longest absolute file path -> ", lengthLongestPath(input))