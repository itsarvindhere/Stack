def minAddToMakeValid(s):
        
        openingBrackets, closingBrackets = 0,0
        
        # For each character in the string
        for c in s:
            # If it is an opening bracket
            if c == "(": openingBrackets += 1
            # If it is a closing bracket
            else:
                # If "openingBrackets" is not 0
                # We have one valid pair so this means, one opening bracket gets used
                if openingBrackets != 0: openingBrackets -= 1
                # It means this closing bracket does not have any opening bracket before it to be paired with
                else: closingBrackets += 1
        
        # For each opening or closing bracket for which we couldn't find a match,
        # We need one closing and opening bracket respectively to match it and make this string valid
        # So, we need to add same number of extra brackets 
        # as we have "openingBrackets" and "closingBrackets" combined at this point
        return openingBrackets + closingBrackets


s = "()))"
print("Output -> ", minAddToMakeValid(s))