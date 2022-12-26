def minOperations(logs):
        
    # Stack to keep track of folders as the user moves between them
    # NOTE -> If stack is empty, that means we are in the "main" folder
    stack = []
        
    for log in logs:
        # If the user moves to child folder
        if log != "../" and log != "./": stack.append(log)
        # Move to the parent folder of curent folder
        # If already in the main folder, do nothing
        # Otherwise, we can pop()
        elif stack and log == "../": stack.pop()
    
    # The number of times we have to use "../" to reach "main" folder means
    # How many pops() we have to do until stack is empty again
    # And that's simply the length of stack
    return len(stack)

logs = ["d1/","d2/","../","d21/","./"]

print("Output -> ", minOperations(logs))