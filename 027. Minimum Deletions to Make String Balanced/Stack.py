def minimumDeletions(s):
    # Since we want to ensure that the string is balanced in such as way that
    # There is no "a" after "b" in the final string
    # It means, whenever we come across something like "ba", we know we have to make one deletion
    deletions = 0
        
    # We will use this stack to put the "b" in it whenever we come across one
    # In short, this stack is only to keep track of previous "b"
    stack = []
        
    # Go through each character of the string
    for c in s:
        # If this is an "a"
        if c == "a":
            # Then, if the stack is not empty
            # It means, there was a "b" before it
            # So we need to make a deletion here
            if stack:
                stack.pop()
                deletions += 1
        # If it is a "b", just push it to the stack
        else: stack.append(c)
        
    return deletions

s = "aababbab"
print("Minimum Deletions ->", minimumDeletions(s))
                