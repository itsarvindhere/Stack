def removeOuterParentheses(s):
        
    # We will keep each part without its outer parenthesis in this list
    output = []
        
    # Keep track of Count of Opening and closing brackets in the output stack
    count = 0
        
    # Keep track of removed parenthesis
    removedCount = 0
        
    # For each character
    for c in s:
            
        # If this is an opening bracket => "("
        if c == "(":
                
            # If the number of parenthesis removed so far is even
            # That means there are two possibilities
                
            # Either "removedCount" is 0
            # Or it is some even number
                
            # In both cases, we have to remove this bracket so we increment "removedCount"
            if removedCount % 2 == 0: removedCount += 1
                    
            # Otherwise, this bracket should be the part of output string
            else: 
                output.append(c)
                count += 1
            
        # If this is a closing bracket => ")"
        else:
                
            # If we have same number of opening brackets as closing brackets in the output stack
            # It means, we already have a balanced string there
            # So, the current closing bracket should be removed
            if count == 0: removedCount += 1
                    
            # Otherwise, if there is an imbalance, it should be the part of output string
            # WE want to make sure output string is a balance string with same number of opening brackets as closing brackets
            else: 
                output.append(c) 
                count -= 1
        
    return "".join(output)

s = "(()())(())"

print("Output -> ", removeOuterParentheses(s))