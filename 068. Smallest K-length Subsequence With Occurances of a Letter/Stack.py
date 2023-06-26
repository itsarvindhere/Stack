def smallestSubsequence(s: str, k: int, letter: str, repetition: int) -> str:
              # Length of the string
        n = len(s)
        
        # Count of "letter" characters on right of each character
        countOnRight = [0] * n
        countSoFar = 0
        
        for i in range(n - 1, -1, -1):
            # Update the count of "letter" characters on right of current character
            countOnRight[i] = countSoFar
            if s[i] == letter: countSoFar += 1
                
        # Stack that we will use to generate the smallest subsequence
        stack = []
        
        # Loop over the string
        for i in range(n):
            
            # If the stack is not empty then what are the situations we will face?
            while stack:
                
                # 1. The character on top of stack might be greater than the current character
                if s[stack[-1]] > s[i]:
                    # Here also, we have two situations
                    
                    # 1.1 The character on top of stack is "letter"
                    if s[stack[-1]] == letter:
                        # In this case, if we pop the top of stack
                        # It would mean repetition will increase by "1"
                        # So,we need to be sure that we have enough "letter" characters on the right of s[i]
                        
                        # If we have enough "letter" characters on right of current index
                        # Then we can pop the top of stack
                        
                        # And since the character that we are popping is same as "letter"
                        # Then repetitions will increase by "1" because we now have
                        # "1" extra "letter" to put in our subsequence
                        
                        # Another condition to keep in mind is that we should only remove from stack
                        # If we know that we have enough characters left to traverse to make sure
                        # We can get a "k" length subsequence
                        # We don't want to get a stack with less than "k" characters in it at the end
                        if countOnRight[i] > repetition and (k - len(stack)) < (n - i): 
                            repetition += 1
                            stack.pop()
                            
                        # Otherwise, we cannot pop so the top of stack will remain in stack
                        # And so we come out of the loop
                        else: break


                    # 1.2 The character on top of stack is not "letter"
                    # In this case, we can safely pop the top of stack
                    else:                         
                        if (k - len(stack)) < (n - i): stack.pop()
                        else: break
                        
                # 2. The character on top of stack might be smaller or equal than the current character
                elif s[stack[-1]] <= s[i]:
                    
                    
                    # 2.1 The only time we should pop from stack in this case
                    # is when current character is "letter"
                    # Even then, there should be a certain condition
                    if s[i] == letter:
                        
                        # Length of stack represents the length of subsequence
                        # So, at any point, if we want to know how many characters are left to put in subsequence to return
                        # We can say -> k - len(stack)
                        # So, at this point, if k - len(stack) is less than repetitions
                        # It means, we need to pop from stack
                        if k - len(stack) < repetition: stack.pop()
                        else: break
                        
                    # Otherwise, no need to pop from the stack
                    else: break
            
            # Push the current character's index in the stack
            # Also, if the character that we push is same as "letter", that means we need one less repetition
            if s[i] == letter: repetition -= 1
                
            stack.append(i)
    
        # Our stack has only the indices at this point
        # Also, we need only first "k" characters
        stack = [s[i] for i in stack[:k]]
        
        # Finally, just return the string
        return "".join(stack)


s = "mmmxmxymmm"
k = 8
letter = "m"
repetition = 4

print("Output -> ", smallestSubsequence(s, k, letter, repetition))