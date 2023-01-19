def exclusiveTime(n, logs):
    # The output list to return
    output = [0] * n
        
    # Stack to keep track of function execution
    stack = []
        
    # Go through each log
    for log in logs:
        # Extract the data from the log
        function_id, startOrEnd, timestamp = log.split(":")
        function_id, timestamp = int(function_id), int(timestamp)
            
        # If this is the start of a function
        if startOrEnd == "start":
            # Push this to the stack
            # Before pushing, it is possible that there was some function in stack already which has not yet ended
            # In that case, we have to take care of the time the previous function has executed for so far
            if stack:
                output[stack[-1][0]] += (timestamp - stack[-1][1])
                
            # We will push a pair to the stack -> (function_id, timestamp)
            stack.append([function_id, timestamp])
            
        # If this is the end of a function's execution
        else:
            output[stack[-1][0]] += timestamp - stack[-1][1] + 1
                
            stack.pop()
                
            # If the stack has some function in it after we removed the top function
            # Then, it means that function did not execute for the time the top function was executing
            # And since when that function "started", we had already pushed the time till it executed (before the second function took over)
            # This means, we now need its new "start" time. Which is simply the time after which the current function ended executing
            # Because only if the current function ends, the previous function can resume executing
            if stack: stack[-1][1] = timestamp + 1

        
    # Return the output list
    return output

n = 2
logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
print("Output -> ", exclusiveTime(n,logs))