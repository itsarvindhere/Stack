def reverseParentheses(s):
        stack = []
        
        # Go through each character
        for c in s:
            # If it is an opening bracket or an alphabet
            if c != ")": stack.append(c)
            # If it is a closing parenthesis
            else:
                # We want to reverse the string between the last opening parenthesis till the top of stack
                reverse = []
                while stack[-1] != "(": reverse.append(stack.pop())
                    
                # At this point, "reverse" has the string between innermost opening and closing parenthesis
                # Pop the opening bracket as we are done with it
                stack.pop()
                
                # Just push back the string that we reversed
                # Note that it is already reversed so we simply put it in the same order as it is in "reverse" list
                for c in reverse: stack.append(c)

        return "".join(stack)


s = "(ed(et(oc))el)"
print("Output -> ", reverseParentheses(s))