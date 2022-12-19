def finalPrices(prices):
    n = len(prices)
        
    # Output to return
    answer = [0] * n
        
    # Stack that we are going to use to find the nearest price on right that is <= current price
    stack = []
        
    # Loop from last to first price
    for i in range(n - 1, -1, -1):
        answer[i] = prices[i]
            
        # While Stack is not empty, remove all the useless values from top of stack
        while stack and stack[-1] > prices[i]: stack.pop()
            
        # If stack is not empty, it means the top of stack has the price that is <= prices[i]
        if stack: answer[i] -= stack[-1]
                
        # Finally, push the current price to stack as well
        # Since it might be useful for other prices before it 
        stack.append(prices[i])
               
    return answer

prices = [8,4,6,2,3]
print("Output is -> ", finalPrices(prices))