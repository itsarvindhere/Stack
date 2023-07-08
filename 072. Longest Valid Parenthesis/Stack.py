def longestValidParentheses(s: str) -> int:
        
        # Length of the input string
        n = len(s)
        
        # longestLengthToReturn
        longestLength = 0
        
        # Stack to keep track of opening brackets
        stack = []
        
        # To keep track of valid parenthesis substrings
        validSubstrings = []
        
        # Loop over the input string
        for i in range(n):
            
            # If it is an opening parenthesis, just put its index in the stack
            if s[i] == '(': stack.append(i)
                
            # Otherwise, if it is a closing parenthesis
            else:
                
                # If stack is not empty, it means we have an opening parenthesis to have a pair
                if stack:
                    
                    # The starting index of this valid substring
                    startIdx = stack.pop()
                    
                    # The ending index of this valid substring
                    endIdx = i
                    
                    # What is the length of this valid substring
                    length = endIdx - startIdx + 1
                    
                    # Now, it is possible that this whole substring include some other substrings
                    # that we have already added in "validSubstrings"
                    # So, we will not require all those substrings now that we have this current one
                    while validSubstrings and validSubstrings[-1][0] > startIdx and validSubstrings[-1][1] < endIdx: validSubstrings.pop()
                    
                    # Now we can put the data of this current substrings in the "validSubstrings" list
                    # The data we keep is [start index, end index, length]
                    
                    # If the validSubstrings list is not empty yet
                    # And the endIdx of substring on top => startIdx of currentSubstring - 1
                    # Then we can combine the two lengths into one
                    if validSubstrings and validSubstrings[-1][1] == startIdx - 1:
                        validSubstrings[-1][1] = endIdx
                        validSubstrings[-1][2] += length
                    else:
                        validSubstrings.append([startIdx, endIdx, length])
                    
            i += 1
        
        # Now that we have the data for all the valid substrings
        # We can now get the maximum length out of all the valid substrings
        for data in validSubstrings: longestLength = max(longestLength, data[2])
        
        # Return the output
        return longestLength


s = ")()())"
print("Output -> ", longestValidParentheses(s))