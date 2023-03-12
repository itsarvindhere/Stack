def robotWithString(s: str) -> str:
        t = []
        output = []
        
        # To keep the count of each character in the string "s"
        # So that, as we push a chracter to stack "t", we will also reduce its count
        # This way, at any time, we can check if there is a smaller character present after any character in "s"
        freq = {}
        for c in s: freq[c] = freq.get(c,0) + 1

        for c in s:
            # Push the current character to the stack
            t.append(c)
            
            # Also reduce its count
            freq[c] -= 1
            
            # If the count becomes 0
            if freq[c]== 0: freq.pop(c)
                
            # We can push the current character to output string
            # If we are sure there is no smaller character left in the dictonary
            while t and freq and min(freq) >= t[-1]: output.append(t.pop())
                
        # IF "t" is not yet empty
        while t: output.append(t.pop()) 
            
        return "".join(output)


s = "bdda"

print("Lexicographically smallest string -> ", robotWithString(s))