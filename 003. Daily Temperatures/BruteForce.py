def dailyTemperatures(temperatures):
    n = len(temperatures)
        
    # Output to return
    answer = [0] * n
        
    # For each temperature
    for i in range(n):
        # Go through each temperature on its right
        for j in range(i + 1, n):
            # If we found a warmer temperature, stop
            if temperatures[j] > temperatures[i]: 
                answer[i] = j - i
                break

    return answer

temperatures = [73,74,75,71,69,72,76,73]
print("Output is -> ", dailyTemperatures(temperatures))