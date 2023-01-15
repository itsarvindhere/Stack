def removeStars(s: str) -> str:
    stack = []
        
    # Go through each character in the string
    for c in s:
            
        # If we encounter a star, we know we have to remove the character to its left
        # So we simply pop the top of stack
        if c == "*": stack.pop()
                
        # Otherwise, if we encounter an alphabet, we will push it to the stack
        # So that at any time, top of stack will give us previous character
        else: stack.append(c)
        
        
    # Finally, return the string
    return "".join(stack)

s = "leet**cod*e"

print("Output -> ", removeStars(s))