def removeDuplicates(s):
        
    # Stack to efficiently detect duplicates
    stack = []
        
    # For each character in the given string
    for c in s:
        # If the top of stack has the same character
        # Then we know this character won't be included in final string
        # But, we need to remove the character currently on top of stack
        if stack and stack[-1] == c: stack.pop()
        # Otherwise, just push this character in the stack
        else: stack.append(c)
        
    return "".join(stack)

s = "azxxzy"

print("After Removing Adjacent Duplicates, the string is -> ", removeDuplicates(s))