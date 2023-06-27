import math
def replaceNonCoprimes(nums):
        # Stack
        stack = []
        
        # Loop over the input list
        for num in nums:
            
            # The value that we have to push to stack
            # It can be this value itself (if its gcd with previous value is 1)
            # Or, it can be the LCM with previous value(s)
            valToAppend = num
            
            # While stack is not empty
            while stack:
                # Get the GCD/HCF of the previous and current value
                gcd = math.gcd(stack[-1],valToAppend)
                
                # Two number are co-prime if their GCD is 1
                # So, if they are not co-prime
                if gcd > 1:
                    # Then, we have to push the LCM of those two numbers in the stack
                    # If we know the GCD/HCF, the LCM can be found easily
                    # LCM(a,b) = (a * b) // gcd(a,b)
                    valToAppend *= stack[-1] // gcd
                    
                    # And now, the previous value needs to be removed from the stack
                    stack.pop()
                    
                # If two numbers are co-prime, we have to keep both in stack
                # So, we pop nothing and break
                else: break
            
            # Finally, we push the "valToAppend" in the stack
            stack.append(valToAppend)
        
        # Finally, return the stack
        return stack


nums = [6,4,3,2,7,6,2]
print("Output -> ", replaceNonCoprimes(nums))