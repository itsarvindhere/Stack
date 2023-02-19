def evalRPN(tokens) -> int:
        # Set of Operands (For O(1) lookup time)
        operands = {'+', '-', '*', '/'}
        
        # Stack
        stack = []
        
        for token in tokens:
            # If it is not an operator
            if token not in operands: stack.append(int(token))
            # If it is an operator
            else:
                # Take previous two operands
                op2 = stack.pop()
                op1 = stack.pop()
                
                if token == "+": stack.append(op1 + op2)
                elif token == "-": stack.append(op1 - op2)
                elif token == "*": stack.append(op1 * op2)
                else: 
                    stack.append(int(op1/op2))
                          
        return stack[-1]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print("Output -> ", evalRPN(tokens))