from collections import defaultdict
def evaluate(expression: str) -> int: 
        # Split expression at spaces
        # Since there are cases where ")" and "(" do not have space around them
        # We will add spaces around them and then split the expression
        expression = expression.replace("(", " ( ").replace(")", " ) ").split()
        
        # Variables and their values
        values = defaultdict(list)
        
        # Stack
        stack = []
        
        # Protected keywords
        protected = {"add", "mult", "let"}
        
        # To keep track of protected keywords
        keywords = []
        
        # REsult of expression
        expressionResult = 0
        
        # If previous value was a digit
        ifPreviousDigit = False
        
        # Loop over the expression
        for c in expression:
            # If it is an opening parenthesis
            if c  == "(" : stack.append(c)
                
            # If it is a word (or word with numbers e.g. "a1" and "a5b")
            elif (not c.isnumeric()) and (c.isalnum()):
                # If it is a variable
                if c not in protected: 
                    
                    # If this variable is assigned to the variable on top of stack
                    # e.g. if we have something like (let b 3 a b)
                    # Where for variable "a" the value is the value of variable "b"
                    if (keywords and keywords[-1] == "let") and not ifPreviousDigit and type(stack[-1]) is list and not type(stack[-1][0]) is int:
                        values[stack[-1][0]].append(int(values[c][-1]))
                        stack[-1][1] = True
                        ifPreviousDigit = True
                    else:
                        # We will add an additional flag that indicates whether a value has been assigned to this variable 
                        # In other words, whether there is a digit after this variable in the input expression
                        stack.append([c, False])
                else: 
                    keywords.append(c)
                
                ifPreviousDigit = False
            
            # If it is a digit
            elif c.isnumeric() or c[0] == "-": 
                if keywords and keywords[-1] == "let" and not stack[-1][1]:
                    values[stack[-1][0]].append(int(c))
                    # Recall what is mentioned in the comment above. Sine it is a digit, we set the flag for variable on top of stack as True
                    stack[-1][1] = True
                else:
                    stack.append([int(c), True])
                    
                ifPreviousDigit = True
            
            # If it is closing parenthesis
            else:
                # Variables
                localVars = []
                
                #  While we don't come across a protected keyword
                while stack[-1] != "(": localVars.append(stack.pop())
				
                # What type of expression it is 
                expressionType = keywords.pop()
                
                # Pop the opening parenthesis
                stack.pop()
                
                # Let's find the result of this expression
                result = None
                
                # If it is an "add" or "mult" expression
                if expressionType != "let":
                    var1, var2 = localVars[0][0], localVars[1][0]
                    
                    value1, value2 = 0,0 
                    
                    # Get the two operands
                    if var1 in values: value1 = values[var1][-1]
                    else: value1 = var1
                        
                    if var2 in values: value2 = values[var2][-1]
                    else: value2 = var2
                    
                    # Get the result
                    result = value1 + value2 if expressionType == "add" else value1 * value2
                        
                # If it is a "let" expression
                else:
                    # Loop over the local variables
                    for var in localVars:
                        # If among local variables, we have an integer value
                        # Then that is the result of this let expression
                        # So we can immediately exit
                        if type(var[0]) is int: 
                            result = var[0]
                            break
                        # Otherwise, if result is "None", set it to the current value
                        else:
                            if not result: result = values[var[0]][-1]
                                
                    # Since it is a "let" expression, also pop the values from dictionary if there are multiple values assigned to this variable
                    # Because in current scope, the current value has been utilized so we won't need it anymore
                    for var in localVars:
                        if type (var[0]) is not int and len(values[var[0]]) > 1: values[var[0]].pop()
                            
                # Common Task for all three operations
                
                # If stack has a variable that was not assigned a value
                # Then this result is a value for that variable
                if (keywords and keywords[-1] == "let") and stack and type(stack[-1]) is list and not stack[-1][1]:
                    values[stack[-1][0]].append(result)
                    stack[-1][1] = True 
                    
                # Otherwise, push this result to the stack
                # And to avoid any errors, also put it in the dictionary with same value as itself
                else:
                    values[result].append(result)
                    stack.append([result, True])
                    expressionResult = result
					
        # And Finally, return the result of this expression
        return expressionResult 

expression = "(let x 1 y 2 x (add x y) (add x y))"
print("Output is -> ", evaluate(expression))