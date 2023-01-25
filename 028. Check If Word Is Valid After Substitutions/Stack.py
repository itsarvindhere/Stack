def isValid(s):
    stack = []
        
    for c in s:
        # If it is an "a", simply push it to the stack
        if c == "a": stack.append(c)
                
        # If it is "b", it can be valid only if there was an "a" before it
        elif c == "b":
            if stack and stack[-1] == "a": stack.append(c)
            else: return False
                
        # If it is "c", it can be valid only if there was a "b" before it
        else:
            # If there was "b" before it, it means, we found one combination of "abc" so we can remove it
            if stack and stack[-1] == "b": 
                stack.pop()
                stack.pop()
            else: return False
        
    # After above steps, the stack should be empty
    # Only then "s" can be valid
    return not stack

s = "abcabcababcc"
print("Is Valid? ->", isValid(s))