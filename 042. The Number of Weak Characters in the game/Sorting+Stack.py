def numberOfWeakCharacters(properties) -> int:
    count = 0
        
    n = len(properties)
        
    # Can sorting help us optimize the brute force code?
    # What if the characters were sorted based on their attack property?
        
    # Since we know there can be characters with same attack values
    # What we can do is, if attack value is same, sort by the defense values (in decreasing order)
    properties.sort(key = lambda x: (x[0], -x[1]))

    # Stack
    stack = []
    
    # Now, we will loop in reverse
    for i in range(n - 1, -1, -1):
            
        # For each character, we will remove all useless values on its right side
        # That is, all the characters on right with a smaller defense value
        # Why we did not consider the attack values here?
        # Because since the array is sorted based on attack values
        # It means, every character on right of any character has attack greater or equal to it
        # So we are only concerned with defense values at this point
        while stack and stack[-1] < properties[i][1]: stack.pop()
            
        # At this point, if stack is empty, it means
        # Either this is the last character
        # Or, all values to its right are useless, that is, with a smaller defense value
        if not stack: stack.append(properties[i][1])
                
        # If stack is not empty
        else:
            # Then, if top of stack has a character with strictly greater defense value
            # Then it means, the current character is the weak character so increment the count
            if stack[-1] > properties[i][1]: count += 1
                    
            # Otherwise, we can push it to the stack
            else: stack.append(properties[i][1])
            
    return count


properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]

print("Number opf Weak Characters -> ", numberOfWeakCharacters(properties))