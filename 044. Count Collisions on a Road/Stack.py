def countCollisions(directions: str) -> int:
        
        # Count of collisions
        count = 0
        
        # Stack to keep track of previous car's direction
        stack = []
        
        # Loop starts
        for direction in directions:
            # If stack is not empty
            if stack:
                
                # What are the conditions for a collision?
                
                # 1. Current car is stationary and previous car is coming towards it
                condition1 = stack[-1] == "R" and direction == "S"
                
                # 2. Current car is going towards left and previous car is going towards right
                condition2 = stack[-1] == "R" and direction == "L"
                
                # 3. Current car is going towards left and previous car is stationary
                condition3 = stack[-1] == "S" and direction == "L"
                
                # If any of the three conditions are true, there will be a collision
                if condition1 or condition2 or condition3:
                
                    # Let's take conditions 1 and 2
                    # That is, either current car is stationary and previous car is going towards right
                    # Or, current car is going towards left and previous car towards right
                    # In both cases there will be a collision
                    if condition1 or condition2:
                        
                        # Increment the count accordingly
                        count += 1 if condition1 else 2
                        
                        # Remove the previous car since it has already collided with current car
                        stack.pop()

                        # Also, if there are more cars coming towards right before previous car, they all will collide
                        # And that will further contribute to the number of collisions
                        while stack and stack[-1] == "R": 
                            count += 1
                            stack.pop()

                        # Finally, after we are sure that there won't be any more collisions from previous cars
                        # We can push "S" to the stack
                        stack.append("S")
                
                    # Let's take condition3 -> Current car is going towards left and previous car is stationary
                    # There will be a collision between the two and number of collisions increase by 1
                    else: count += 1

                    
                # If collision does not happen with the previous car, push the current car's direction to stack
                else: stack.append(direction)
                    
            # If stack is empty
            else: stack.append(direction)
                    
        # Finally, return the number of collisions
        return count


directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"

print("Number of Collisions -> ", countCollisions(directions))