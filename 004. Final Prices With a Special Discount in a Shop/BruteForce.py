def finalPrices(prices):
    n = len(prices)
        
    # Output to return
    answer = [0] * n
        
    # For each item's price
    for i in range(n):
        answer[i] = prices[i]
        # Search for the price on right that is less than or equal to its price
        for j in range(i + 1, n):
            # If found, put the discounted price in output array
            if prices[j] <= prices[i]:
                answer[i] -= prices[j]
                break
                    
    return answer

prices = [8,4,6,2,3]
print("Output is -> ", finalPrices(prices))