def checkValidString(s: str) -> bool:
    # Length of the input string
    n = len(s)

    # We will greedily try to pair the closing brackets with the opening brackets
    # Only if there are no opening brackets to pair, we will use the stars
    # Otherwise, the stars will either be just empty string or closing brackets
        
    # Stack to keep track of opening brackets
    openStack = []
        
    # Stack to keep track of Stars
    starStack = []
        
    # Go through each character
    for i in range(n):
        # If it is an opening bracket
        if s[i] == "(": openStack.append(i)
        # If it is a closing bracket
        elif s[i] == ")":
            # Do we have an opening bracket to pair with this closing bracket?
            if openStack: openStack.pop()
                
            # If not, Do we have a star to treat it as an opening bracket and pair with this closing bracket?
            elif starStack: starStack.pop()
                
            # If there is no star or an opening bracket to pair with this closing bracket
            # This string cannot be a valid string at all
            else: return False
                    
            
        # If it is a star
        else: starStack.append(i)
                
    # At this point, there might be some opening brackets in the openStack
    # This time, we will use the stars as closing brackets to match
    # For each opening bracket in openStack, we want a star after it
    # Hence, index of star should be greater than index of the respective open bracket
    while openStack and starStack:
        openBracketIndex = openStack.pop()
        starIndex = starStack.pop()
            
        if openBracketIndex > starIndex: return False
            
    # If string is valid, there should be no opening brackets left to match
    return not openStack


s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

print("Is Valid String -> ", checkValidString(s))