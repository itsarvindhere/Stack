def survivedRobotsHealths(positions, healths, directions: str):
        # Count of robots
        n = len(positions)
        
        # Keep the data in a single list for each robot
        # And also keep track of original indices since we will sort
        robots = [[positions[i], healths[i], directions[i], i] for i in range(n)]
        
        # Since positions can be unsorted, sort the robots by their positions
        robots.sort()
        
        # Stack to simulate the collisions
        stack = []
        
        # Go through each robot
        for robot in robots:
            
            # Flag to check if collision occured or not
            collision = False
            
            while stack:
                # If the direction of current robot is same as previous
                # Or, if current robot is going left and previous is going right
                # Then there won't be any collision so exit
                if robot[2] == stack[-1][2] or (robot[2] == "R" and stack[-1][2] == "L"):
                    collision = False
                    break
                    
                # Otherwise, there is a collision with previous robot
                collision = True
                
                # If the health is same, then pop from stack
                # And we don't continue because both robots will be removed now from line
                if robot[1] == stack[-1][1]: 
                    stack.pop()
                    break
                else:
                    # If the current robot has a higher health than robot on top of stack
                    if robot[1] > stack[-1][1]:
                        # The robot will be popped from stack
                        stack.pop()
                        
                        # If stack is empty, then there won't be any more collisions
                        if not stack: collision = False
                        
                        # Also, the health of current robot will decrease by 1
                        robot[1] -= 1
                        
                    # If the current robot has a lower health than robot on top of stack
                    else:
                        # The health of robot on top of stack will decrease by 1
                        # And current robot will be removed from line
                        stack[-1][1] -= 1
                        
                        # Break since we have removed current robot from the line
                        break

            # If collision flag is False, put this robot in the stack
            if not collision: stack.append(robot)
        
        # Sort the stack based on original indices to get the order correct
        stack.sort(key=lambda x:x[3])
        
        # We just want the health so just keep that data in the stack
        stack = [pair[1] for pair in stack]
        
        # Finally, return the stack
        return stack



positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"

print("Output is ->", survivedRobotsHealths(positions, healths, directions))