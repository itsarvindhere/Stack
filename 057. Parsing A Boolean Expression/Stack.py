def parseBoolExpr(expression: str) -> bool:  
        # We will use a stack
        stack = []
        
        # Go through the expression
        for c in expression:
            # We don't want to put commas in the stack
            if c == ",": continue
                
            # If it is not a closing parenthesis
            if c != ")": stack.append(c)
                
            # If it is a closing parenthesis
            else:
                # We will keep track of count of "f" and "t" as we pop
                countF, countT = 0,0
                
                while stack and stack[-1] != "(":
                    top = stack.pop()
                    if top == "f": countF += 1
                    else: countT += 1
                        
                # Remove the opening bracket as well
                stack.pop()
                
                # And now, top of stack will have the symbol -> | or & or !
                symbol = stack.pop()
                
                # If it is an OR operation
                # Then just one "t" is enough for us to evaluate this expression to True
                if symbol == "|":
                    if countT > 0: stack.append("t")
                    else: stack.append("f")
                        
                # If it is a NOT operation
                # Then the opposite will be the output
                # That is, if "t" then output will be "f" and vice versa
                elif symbol == "!":
                    if countT > 0: stack.append("f")
                    else: stack.append("t")
                        
                # If it is an AND operation
                # Then we need all "t" to evaluate this expression to "True"
                else:
                    if countF == 0: stack.append("t")
                    else: stack.append("f")
                        
        # Return the output
        return False if stack[-1] == "f" else True

expression = "|(&(t,f,t),!(t))"

print("Output -> ",parseBoolExpr(expression))