class Solution:
    def calculate(self, s: str) -> int:
        
        # To avoid duplicate code, use this method
        def pushToStack(stack, value):
            if stack and stack[-1] == "-":
                stack.pop()
                value = -value
                    
            # If there is another digit on topp iof stack, add the current one with that digit
            if stack and type(stack[-1]) is int: stack[-1] += value
                    
            # Else out this value as a new value in the stack
            else: stack.append(value)
        
        
        # Stack
        stack = []
        
        # Length of the expression
        n = len(s)
        
        # Go through each character in the expression
        i = 0
        while i < n:
            # If current character is a space or a "+", skip
            if s[i] == " " or s[i] == "+": i += 1
                
            # If it is an opening parenthesis or a "-", put it in the stack
            elif s[i] == "(" or s[i] == "-":
                stack.append(s[i])
                i += 1
                
            # If it is a digit
            elif s[i].isnumeric():
                digit = []
                # Get the full digit
                while i < n and s[i].isnumeric():
                    digit.append(s[i])
                    i += 1
                    
                # Full digit
                fullDigit = int("".join(digit))
                
                # Handle the cases with a "-" symbol on top of stack
                # And then add the value to stack (or sum it with value at top of stack)
                pushToStack(stack, fullDigit)
                
            # If it is a closing parenthesis
            else:
                
                # We need the sum of the values inside the parenthesis
                innerSum = stack.pop()
                
                # Pop the opening parenthesis from stack
                stack.pop()
                
                # Handle the cases with a "-" symbol on top of stack
                # And then add the value to stack (or sum it with value at top of stack)
                pushToStack(stack, innerSum)
                
                # And increment "i"
                i += 1

        return stack[-1]
    

s = "- (3 + (4 + 5))"

print("Output is -> ", Solution().calculate(s))