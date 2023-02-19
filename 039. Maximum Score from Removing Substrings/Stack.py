def maximumGain(s: str, x: int, y: int) -> int:
        # Maximum points that we can gain
        maxPoints = 0
        
        # Length of the input string
        n = len(s)
        
        # Stack that we will use to check for "ab" and "ba"
        # If x > y, we will only look for "ab" pairs first
        # And vice versa
        stack = []
        
        i = 0
        while i < n: 
            # If stack is not empty
            if stack:
                if x > y and s[i] == "b" and stack[-1] == "a":
                    maxPoints += x
                    stack.pop()
                elif x <= y and s[i] == "a" and stack[-1] == "b":
                    maxPoints += y
                    stack.pop()
                    
                else: stack.append(s[i])
                
            # If stack is empty
            else: 
                stack.append(s[i])
                        
            i += 1
        
        # At this point, stack might have the "ab" or "ba" pairs so we also have to take care of them
        # If x > y, then stack at this point might have some "ba" pairs (since we already took care of ab pairs above)
        # # If x <= y, then stack at this point might have some "ab" pairs (since we already took care of ba pairs above)
        
        stack2 = []
        i = 0
        while i < len(stack):
            if stack2:
                if stack[i] == "b" and stack2[-1] == "a": 
                    maxPoints += x
                    stack2.pop()
                elif stack[i] == "a" and stack2[-1] == "b": 
                    maxPoints += y
                    stack2.pop()
                else: stack2.append(stack[i])
            else:
                stack2.append(stack[i])
                
            i += 1
        
            
        # Return the maximum points
        return maxPoints

s = "cdbcbbaaabab"
x = 4
y = 5

print("Maximum Score -> ", maximumGain(s,x,y))