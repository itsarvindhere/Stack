def maxDepth(s):
        
    # We see that in the worst case in above approach
    # For the last character that is not a bracket, we have to traverse the whole list again (except last element)
    # This is definitely not an efficient approach
        
    # What if for any character, we can keep track of how many opening brackets we have seen so far that have not been closed yet?
    # So we will use a stack just to keep the opening brackets so far that are not yet closed
    # And at any time, the length of stack will give us what are number of opening brackets so far that haven't been closed yet
    stack = []
        
    maximumDepth = 0
            
    # For each character
    for c in s:
            
        # IF the character is an opening bracket
        # That means the depth is increased by 1 or by length of stack
        if c == "(": stack.append(c)
        # If the character is a closing bracket
        # That means, one opening bracket has been closed. So we can pop once
        elif c == ")": stack.pop()
                
        # And finally, just calculate the depth at this moment and update maximum depth if required
        maximumDepth = max(maximumDepth, len(stack))

    return maximumDepth

s = "(1+(2*3)+((8)/4))+1"

print("Maximum Depth is -> ", maxDepth(s))