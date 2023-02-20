def asteroidCollision(asteroids):
        # Stack that we will be using to simulate collisions
        stack = []
        
        # For each asteroid's size
        for size in asteroids:
            # It will destroy all the asteroids that are smaller than it before it
            # Only if it is moving towards left and the previous ones are moving towards right
            
            # Flag to check if both asteroids explode (only happens when size is same)
            bothExploded = False
            
            while stack and stack[-1] > 0 and size < 0 and abs(size) >= stack[-1]:
                if abs(size) == stack.pop(): 
                    bothExploded = True
                    break
                    
            # If both the asteroids exploded, we can move to the next asteroid
            if bothExploded: continue
                
            # What are the conditions for us to take an asteroid and put it in stack
            # That is, it was not destroyed by any other asteroid before it
            
            # First condition : Stack is empty
            # That is, either it is the first asteroid in the list
            # Or, it destroyed all asteroids before it
            condition1 = not stack
            
            # Second condition: Either Asteroids are moving in one direction
            # Or away from each other
            # In both cases, they will not collide
            condition2 = stack and ((stack[-1] > 0 and size > 0) or (stack[-1] < 0 and size < 0) or (stack[-1] < 0 and size > 0))
            
			# If both the conditions are true, only then we can consider this asteroid
            if condition1 or condition2: stack.append(size)

        return stack


asteroids = [10,2,-5]

print("After collision -> ", asteroidCollision(asteroids))