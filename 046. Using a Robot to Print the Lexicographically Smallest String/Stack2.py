def robotWithString(s: str) -> str:
        # Output string that we have to return
        output = []
        
        # First, find the smallest character on right of each character
        # If there is no smaller character on right of any character, "z" will be the default value for that
        smallestOnRight = ["z"] * len(s) 
        
        smallest = "z"
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            smallestOnRight[i] = smallest
            smallest = min(smallest, s[i])
        
        # Now once we get the smallest character on right of each character
        # We can start with the main logic of pushing the character to "t" and from "t" to paper
        t = []
        for i in range(n):
            # Push current character's index to "t"
            t.append(i)
            
            # Now, if there is no smaller character on right
            # We can safely write it on the paper
            while t and smallestOnRight[i] >= s[t[-1]]: 
                output.append(s[t.pop()])
            
        # If t is not yet empty
        while t: output.append(s[t.pop()])
        
        return "".join(output)


s = "bdda"

print("Lexicographically smallest string -> ", robotWithString(s))