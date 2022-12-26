def makeGood(s):
        
    # Stack to efficiently compare adjacent characters
    stack = []
        
    # Go through each character in the string
    for c in s:
            
        # If the top of stack has the same character but in opposite case
        # We would not include these two characters in our output string
        # So not only we do not push the current character in stack, but we also pop the top of stack
        if stack and stack[-1] == c.swapcase(): stack.pop()
                
        # Otherwise, push the current character to the stack
        else: stack.append(c)
        
    # Finally, just return the output string
    return "".join(stack)

s = "leEeetcode"
print("Output -> ", makeGood(s))