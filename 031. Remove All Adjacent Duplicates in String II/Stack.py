def removeDuplicates(s: str, k: int) -> str: 
    # Stack
    stack = []
        
    # Go through each character
    for c in s:
        # If the top of stack has the same character
        if stack and stack[-1][0] == c: 
                
            # Update the count for the character
            stack[-1][1] += 1

            # If the count becomes equal to "k", we need to pop
            if stack[-1][1] == k: stack.pop()
            
        # We will push a pair to the stack -> [character, count]
        else: stack.append([c, 1])
        
    # Return the final string
    return "".join([pair[0] * pair[1] for pair in stack])

s = "deeedbbcccbdaa"
k = 3

print("Output -> ", removeDuplicates(s,k))