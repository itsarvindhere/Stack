def minOperations(logs):
        
    # A simple counter to keep track of operations
    # 0 value means, we are already in main folder
    operations = 0
        
    for log in logs:
        # If the user moves to child folder, increment operations
        # because we have to use one "../"" operation to come back to parent folder of this folder
        if log != "../" and log != "./": operations += 1
        # Move to the parent folder of curent folder
        # If already in the main folder, do nothing
        # Otherwise, decrement operations
        elif log == "../" and operations != 0: operations -= 1
                
    return operations

logs = ["d1/","d2/","../","d21/","./"]

print("Output -> ", minOperations(logs))