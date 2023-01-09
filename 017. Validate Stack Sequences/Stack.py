def validateStackSequences(pushed, popped):
    # Stack that was empty initially
    stack = []
        
    # Pointer for "popped" list
    j = 0
        
    for i in range(len(pushed)):
            
            # Push the ith element in "pushed" list on to the stack
            stack.append(pushed[i])
                
            # While the top of stack has the same element as the jth element in "popped" list
            while(stack and stack[-1] == popped[j]):
                stack.pop()
                j += 1
    
    # Only if the stack is empty at this point, we return True
    return len(stack) == 0

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

print("Output -> ", validateStackSequences(pushed, popped))