def scoreOfParentheses(s: str) -> int:
    stack = [0]
        
    for c in s:
        # If it is an opening bracket
        # Simply append its score as 0 to the stack
        if c == "(": stack.append(0)
        # If it is a closing bracket
        else:
            # We will pair it with the opening bracket on top of the stack
            # Remember the score we pushed when we encountered an opening bracket?
            # That score will denote what is the score of the sub-string in between that opening bracket
            # ANd its corresponding closing
            # ANd as per the problem, in this case, the score is 2 * A
            currScore = max(2 * stack.pop(),1)
                
            # Also update the score for the previous opening bracket
            # Because if there is any opening bracket in the stack at this point, 
            # then it means, the current closing bracket is inside another pair
            stack[-1] += currScore

    return stack.pop()

s = "()()"

print("Score -> ", scoreOfParentheses(s))