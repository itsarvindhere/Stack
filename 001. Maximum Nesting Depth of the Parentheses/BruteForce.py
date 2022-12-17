def maxDepth(s):
        
    # The Brute Force Approach will be 
    # For any character 
    # Calculate its depth and update maxDepth if necessary
        
    maximumDepth = 0
        
    # For each character
    for i,c in enumerate(s):
        # Calculate its depth
        depth = 0
            
        # Depth means, how many open brackets are there so far
        # That have not yet been closed
        for j in range(i):
            if s[j] == "(": depth += 1
            elif s[j] == ")": depth -= 1
                
        # Update the max depth
        maximumDepth = max(maximumDepth, depth)              
            
    return maximumDepth

s = "(1+(2*3)+((8)/4))+1"

print("Maximum Depth is -> ", maxDepth(s))