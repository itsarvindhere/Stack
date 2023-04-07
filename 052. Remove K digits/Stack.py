def removeKdigits(num: str, k: int) -> str:
    # Length of the list
    n = len(num)
        
    # If we have to remove all the digits
    if k == n: return "0"
        
    # Stack that we will use to check if previous digit is greater than current
    stack = []
        
    # Go through each character
    for c in num:
        # If there is a greater digit before
        # And k is not yet 0
        # We can remove the previous digit
        while stack and stack[-1] > c and k > 0: 
            stack.pop()
                
            # Also, decrease k since we removed one digit
            k -= 1
            
        # Push the current digit to stack
        # Just avoid pushing a zero if stack is empty
        # We want to avoid leading zeros
        if not stack and c == "0": continue 
                
        stack.append(c)
        
    # If we did not remove "k" elements
    # We will simply remove from the top of stack
    while stack and k > 0:
        stack.pop()
        k -= 1
            
    return "0" if not stack else "".join(stack)


num = "1432219"
k = 3

print("Output -> ", removeKdigits(num,k))

