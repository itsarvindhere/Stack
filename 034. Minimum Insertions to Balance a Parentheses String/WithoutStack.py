def minInsertions(s: str) -> int:
    # Minimum Insertions required
    insertions = 0
        
    # Length of the string
    n = len(s)
        
    # Variable to efficiently track opening brackets
    openingBrackets = 0
        
    i = 0
    while i < n:
        # If this is an opening bracket
        if s[i] == "(": openingBrackets += 1
        # If this is a closing bracket
        else:
            # If we are not yet at the last character
            if i < n - 1:
                # 1. There are two closing brackets together
                if s[i + 1] == ")":
                    # If there are 1 or more opening brackets before 
                    # We have a valid pair so we can decrement
                    if openingBrackets > 0: openingBrackets -= 1
                    # If there is no opening bracket before
                    # We need to add one opening bracket for a valid pair
                    else: insertions += 1
                            
                    i += 1
                    
                # 2. There is only one closing bracket
                else:
                    # If there are 1 or more opening brackets before 
                    # We only need to add one closing bracket
                    if openingBrackets > 0: 
                        openingBrackets -= 1
                        insertions += 1
                    # If there is not even an opening bracket before
                    # we need to add one opening and one closing bracket
                    else:
                        insertions += 2
                            
            # If we are at the last character and it is a closing bracket
            else: 
                # If there is an opening bracket to pair with it
                if openingBrackets > 0: 
                    # Then we need only one closing bracket for this pair
                    insertions += 1
                    openingBrackets -= 1
                    
                # Otherwise, we not only need one closing bracket but also one opening bracket
                else: insertions += 2
        i += 1
            
    # If there are opening brackets left to pair, then we need to put 2 closing brackets for each of them
    insertions += openingBrackets * 2

    return insertions


s = "))())("

print("Minimum Insertions Required -> ", minInsertions(s))