def maxDepth(s):
        
    # Okay, so with Stack we can optimize the code
    # But that also means we used extra memory
    # But is that really required?
        
    # Because all that we want to count is number of open brackets that are not yet closed, right?
    # And that we can do with a simple variable too
    count = 0
        
    maximumDepth = 0
            
    # For each character
    for c in s:
            
        # IF the character is an opening bracket
        # That means the depth is increased by 1
        if c == "(": count += 1
        # If the character is a closing bracket
        # That means, one opening bracket has been closed
        elif c == ")": count -= 1
                
        # And finally, just calculate the depth at this moment and update maximum depth if required
        maximumDepth = max(maximumDepth, count)

    return maximumDepth

s = "(1+(2*3)+((8)/4))+1"

print("Maximum Depth is -> ", maxDepth(s))