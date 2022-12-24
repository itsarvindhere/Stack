def isValid(s):

    match = {
        ")" : "(",
        "}" : "{",
        "]" : "[",
    }
        
    # Stack to keep the opening brackets
    stack = []
        
    # Go through each character
    for c in s:
        # If it is an opening bracket, push it to stack
        if c not in match: stack.append(c)
        # If it is a closing bracket
        else:
            # If stack is not empty then, the top of stack must be a matching opening bracket
            # But if stack is empty, then this is not a valid string at all
            if not stack or stack[-1] != match[c]: return False
                
            # If a match is found, remove the opening bracket on top of stack
            stack.pop()
        
    # If the string is valid, then the stack must be empty at this stage
    # Because all the opening brackets have found their respective closing brackets
    return len(stack) == 0

s = "()[]{}"

print("Is Valid Parenthesis String? -> ", isValid(s) )