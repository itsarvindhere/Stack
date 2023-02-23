def numberOfWeakCharacters(properties) -> int:
    count = 0
        
    n = len(properties)
        
    # Can sorting help us optimize the brute force code?
    # What if the characters were sorted based on their attack property?
        
    # Since we know there can be characters with same attack values
    # What we can do is, if attack value is same, sort by the defense values (in decreasing order)
    properties.sort(key = lambda x: (x[0], -x[1]))

    # Why were we using a stack in above approach? To keep track of the largest defense value so far
    # But that we can do using a simple variable only
    maxDefenseValSoFar = 0 
        
    # Now, we will loop in reverse
    for i in range(n - 1, -1, -1):
        # Update the maxDefenseValSoFar if current defense value is >= previous
        if properties[i][1] >= maxDefenseValSoFar: maxDefenseValSoFar = properties[i][1]
        # If current defense value is < previous, it means current character is the weak character
        else: count += 1
            
    return count


properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]

print("Number opf Weak Characters -> ", numberOfWeakCharacters(properties))