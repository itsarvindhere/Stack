def dailyTemperatures(temperatures):
    n = len(temperatures)
        
    # Output to return
    answer = [0] * n
        
    # Stack that we will use to get the first greater temperature on the right of each temperature
    stack = []

    # Since we want the "first greater on right"
    # We will loop from last to first
    for i in range(n - 1, -1, -1):
            
        # Remove all useless elements from stack
        # That is, all the temperatures <= current temperature
        while stack and temperatures[stack[-1]] <= temperatures[i]: stack.pop()
            
        # If there is still some elements left in stack
        # Then it means the top of stack has index of a temperature that is bigger than current temperature
        if stack:
            # The top is the nearest greater on the right
            top = stack[-1]
            answer[i] = top - i
                
        # Push the current index to stack. It may be the nearest greater on right for some previous temperature(s)
        stack.append(i)
            
    return answer

temperatures = [73,74,75,71,69,72,76,73]
print("Output is -> ", dailyTemperatures(temperatures))