def decodeAtIndex(s: str, k: int) -> str:
        # List to keep track of the length of the string as we iterate over it
        lengths = []
        
        # We will iterate over the string
        for c in s:
            length = lengths[-1] if lengths else 0
            
            # If this is an alphabet, the decoded string's length will increase by only 1
            if not c.isnumeric(): length += 1
                
            # But if it is a digit, this will increase the length by "digit * length so far"
            else: length *= int(c)
            
            # Push the length to the list
            lengths.append(length)
			
            # Pushing the lengths > k will of no use anyway
            if length > k: break
        
        # Length of the list
        n = len(lengths)
        
        # Traverse backwards now
        for i in range(n - 1, -1, -1):
            # We will use the modulus to bring the value of k in the desired range
            k %= lengths[i]

            # Here, If k becomes 0 & we are not at any digit right now
            # Then the "ith" character in the encoded string will be the "kth" character in decoded string
            if k == 0 and not s[i].isnumeric(): return s[i] 
            
        return "Hala Madrid"


s = "leet2code3"
k = 10

print("Output -> ", decodeAtIndex(s,k))