def canBeValid(s: str, locked: str) -> bool:
        # Length of the string "s"
        n = len(s)
        
        # If there are odd number of characters, we can not make this string valid
        # Because we want an opening bracket for each closing bracket
        # meaning, there should be even number of characters in the string to begin with
        if n%2 != 0: return False
        
        # Stack to keep track of indices at which we can change the character
        notLocked = []
        
        # Stack to keep track of opening brackets (except the ones having "0" in locked)
        stack = []
        
        # Go through each character in the string "s"
        for i,c in enumerate(s):
            
            # If at same index in "locked", we have a "0"
            # Push this index in notLocked stack
            if locked[i] == "0": notLocked.append(i)
                
            # Otherwise
            else:
                # If it is an opening bracket
                if c == "(": stack.append(i)
                    
                # If it is a closing bracket
                else:
                    # Do we have an opening bracket to pair with this?
                    if stack: stack.pop()
                    
                    # Do we have an index before at which we can flip the bracket to match with this closing bracket?
                    elif notLocked: notLocked.pop()
                        
                    # Otherwise, there is no way to make this string valid
                    else: return False
                    
        # If stack is not empty, it means, there are some opening brackets that don't have a closing bracket to pair with
        # So we will now look at the notLocked stack to see if we have some indices that we can use to form a pair
        while stack and notLocked:
            # If there is no index on the right of index on top of stack at which we can flip
            # This means, we cannot make this string valid
            if stack.pop() > notLocked.pop(): return False        
            
        return not stack



s = "))()))"
locked = "010100"

print("Can the string be made Valid? ", canBeValid(s, locked))