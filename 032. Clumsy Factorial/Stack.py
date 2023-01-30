def clumsy(n: int) -> int:
    # Stack that we will use to perform the calculations
    stack = [n]
        
    # Which operation to perform
    # 1 -> Multiplication
    # 2 -> Division
    # 3 -> Addition
    # 4 -> Substraction
    operation = 1
        
    # Go through each value from n - 1 to 1
    for i in range(n-1, 0, -1):
        operation %= 4
            
        if operation == 1: stack[-1] *= i
                
        elif operation == 2: stack[-1] = int(stack[-1] / i)
            
        elif operation == 3: stack.append(+i)
                
        else: stack.append(-i)
                
        operation += 1
        
    # Finally, just return the sum of all values in the stack
    return sum(stack)

n = 10
print("Clumsy Factorial is -> ", clumsy(n))