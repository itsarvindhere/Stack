def numberOfWeakCharacters(properties) -> int:
    count = 0
    
    n = len(properties)
    
    # For each character
    # We will go through every other character to see if there exists a character 
    # with strictly greater attack and defense
    for i in range(n):
        attack1,defense1 = properties[i]
        for j in range(n):
            attack2, defense2 = properties[j]
            
            # If there exists such a character
            # We will increment our count and exit this inner loop
            if attack2 > attack1 and defense2 > defense1: 
                count += 1
                break
                
    
    return count


properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]

print("Number opf Weak Characters -> ", numberOfWeakCharacters(properties))