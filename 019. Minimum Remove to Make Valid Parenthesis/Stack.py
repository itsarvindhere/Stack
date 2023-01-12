def minRemoveToMakeValid(s):
    stack = []
        
    # Convert the string to List to update any index quickly
    # Basically, 
    # we will replace all those indices from where we have to remove parenthesis with an empty string
    strToArr = list(s)

    # Go through each character
    for i,c in enumerate(strToArr):
        # If it is an opening bracket
        if c == "(": stack.append(i)
                
        # If it is a closing bracket
        elif c == ")":
            # If there is an opening bracket on top of stack
            # We can pair them. 
            if stack and strToArr[stack[-1]] == "(": stack.pop()
            else: stack.append(i)
                    
                    
    # Now, We will replace all those indices from where we have to remove parenthesis with an empty string
    for idx in stack: strToArr[idx] = ""

    # Now simply return the output string
    return "".join(strToArr)

s = "lee(t(c)o)de)"

print("Output -> ", minRemoveToMakeValid(s))