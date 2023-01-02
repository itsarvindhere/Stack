def minAddToMakeValid(s):
    openingBrackets, closingBrackets = [],[]
    
    # For each character in the string
    for c in s:
        # If it is an opening bracket
        if c == "(":
            openingBrackets.append(c)
        # If it is a closing bracket
        else:
            # If "openingBrackets" stack is not empty
            # We have one valid pair
            if openingBrackets: openingBrackets.pop()
            else: closingBrackets.append(c)

    # For each opening or closing bracket for which we couldn't find a match,
    # We need one closing and opening bracket respectively to match it and make this string valid
    # So, we need to add same number of extra brackets 
    # as we have "openingBrackets" and "closingBrackets" combined at this point
    return len(openingBrackets) + len(closingBrackets)


s = "()))"
print("Output -> ", minAddToMakeValid(s))