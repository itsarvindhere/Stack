def countCollisions(directions: str) -> int:
        
        # Count of collisions
        count = 0
        
        # From stack approach, we understood that, 
        
        # if a car is stationary, all the cars moving towards right before it will collide with it
        # if a car is moving towards left, all the cars moving towards right before it will collide with it
        
        # Counter to keep track of cars moving towards rigt
        carsMovingTowardsRight = 0
        
        # Variable to keep track of the previous car's direction
        previousDirection = ""
        
        # Go through each car's direction
        for direction in directions:
            
            # If current car is moving towards right
            if direction == "R": 
                
                # Increment the count
                carsMovingTowardsRight += 1
                
                # Also update the previous car's direction as "R"
                previousDirection = "R"
            
            # If current car is stationary
            elif direction == "S":
                # All the cars coming towards it will collide with it
                count += carsMovingTowardsRight
                
                # Also update the previous car's direction as "R"
                # Since after collision, all cars will be stationary
                previousDirection = "S"
                
                # Reset the count for cars moving towards right
                carsMovingTowardsRight = 0
                
            # If current car is moving towards left
            else:
                # If the previous car was stationary
                # There will be only one collision
                if previousDirection == "S": 
                    count += 1
                    
                # If the previous car was moving towards Right
                # All cars moving towards right before it will also collide
                elif previousDirection == "R": 
                    
                    count += carsMovingTowardsRight + 1
                    
                    # Also update the previous car's direction as "R"
                    # Since after collision, all cars will be stationary
                    previousDirection = "S"
                    
                    # Reset the count for cars moving towards right
                    carsMovingTowardsRight = 0
                    
                # If previous car was also moving towards left, there will be no collision
                # So we can simply update the previous car's direction and nothing else needs to be done
                else: previousDirection == "L"
                    
        # Finally, return the number of collisions
        return count


directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"

print("Number of Collisions -> ", countCollisions(directions))