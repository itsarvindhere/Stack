def smallestSubsequence(s: str) -> str:
    # Length of the string
    n = len(s)
        
    # What is the last index at which each character occurs?
    indices = {}
    for i in range(n): indices[s[i]] = i
            
    # Stack that we will use to create the subsequence
    stack = []
        
    # Visited set to make sure each element is considered exactly once
    visited = set()
        
    # Main Loop starts
    for i in range(n):
        # What if the current character is smaller than the one on top of stack?
        # Then, we can remove the top character only if 
        # we know the same top character can be found later in the string
        # And that we can check by comparing the last index of that character in original string
        # WIth the current index (value of loop variable i)
            
        # Also, if the current character is already present in stack, we do not want to push it again
        # So that's why, we have the check for "s[i] not in visited"
        while stack and stack[-1] > s[i] and indices[stack[-1]] > i and s[i] not in visited: 
                
            # Don't forget to remove it from the set of visited characters
            visited.remove(stack[-1])
                
            # Now remove it from top of stack
            stack.pop()
            
        # Only if the current character is not present in the visited set
        if s[i] not in visited:
            # Now we can push the current character's index to the stack
            stack.append(s[i])
            
            #Also, we will make sure to add it to visited set
            visited.add(s[i])

    # Now, just return the subsequence
    return "".join(stack)

s = "bcabc"
print("Output -> ", smallestSubsequence(s))