def calculate(s: str) -> int:
        # Length of the input string
        n = len(s)
        
        # There are two reason to use a stack in above approach
        # 1. We want to know what was the previous operator
        # 2. We want to know what was the previous operand
        # And we can do that using simple variables as well
        prevOperand = 0
        prevOperator = ""
        
        # Final Output that we have to return
        finalOutput = 0
        
        # Set of operators
        operators = {"+", "-", "/", "*"}
        
        # Main Loop starts
        i = 0
        
        while i < n: 
            
            # If it is a space, we will ignore and move to next character
            if s[i] == " ": 
                i += 1
                continue
            
            # Otherwise, if it is a number
            elif s[i] not in operators: 
                
                # Get the current operand
                # Since an operand can have multiple digits
                # We want to capture the whole operand before doing any calculations
                # This won't affect the complexity since we won't go over all these indices (i) again
                currentOperand = 0  
                while i < n and s[i] not in operators and s[i] != " ": 
                    currentOperand = (currentOperand * 10) + int(s[i])
                    i += 1
                    
                # Once we get the number, now we will check if we had any operator previously or not
                if prevOperator:
                    
                    # If it is a "+" operator, we don't do anything and simply replace the previous operand with current operand
                    # Why? Because what if there are multiplication and division operations after it?
                    # If we calculate the sum here, our final calculation might not be correct
                    # In simple words, we will first do all the multiplication and division operations
                    # And only after that we will do the addition and substraction
                    # Don't forget to store the previousOperand in finalOutput before replacing it
                    if prevOperator == "+": 
                        finalOutput += prevOperand
                        prevOperand = currentOperand
                        
                    # If it is a "-" operator, we will again replace the previous operand with current operand
                    # The only difference will be that we will set prevOperand to negative of currentOperand
                    elif prevOperator == "-": 
                        finalOutput += prevOperand
                        prevOperand = -currentOperand
                        
                    # If it is "*" operation, we will multiple current operand with previous operand
                    # And then replace the previous operand with this new result that we get after multiplication
                    elif prevOperator == "*": prevOperand *= currentOperand
                        
                    # If it is "/" operation, we will divide current operand and previous operand
                    # And then replace the previous operand with this new result that we get after division
                    # Do note that "integer division should truncate toward zero."
                    else: prevOperand = int(prevOperand / currentOperand)     
                
                
                # If haven't found any operator yet, it means it is the first operand in this string
                else: prevOperand = currentOperand
            
            # If it is an operator
            else: 
                prevOperator = s[i]
                i += 1

        # Finally, do not forget to add the last operand in the result
        finalOutput += prevOperand
        
        return finalOutput


s = "1*2-3/4+5*6-7*8+9/10"
print("Output -> ", calculate(s))