class Solution: 
    # Helper method to get the time at which a car will collide with another car
    def getTime(self, carA, carB):
        return float((carB[0] - carA[0]) / (carA[1] - carB[1]))
    
    def getCollisionTimes(self, cars):
        # How many cars are there?
        n = len(cars)
        
        # Initialize the array that we have to return
        answer = [-1] * n
        
        # Stack
        stack = []
        
        # Loop over the list from right to left
        for i in range(n - 1, -1, -1):
            
            # If current car is going slower than car on top of stack
            # They will never collide
            # So it makes no sense to keep the car on top of stack in the stack
            # Since it will never result in any further collision
            
            # Another condition we need to take care of is when multiple cars are colliding
            # Suppose, we have three cars a,b,c
            
            # Now, suppose we know that all three will collide
            # But, what if the car "b" collides with "c" first, before the car "a" collides with it?
            # SO, in that case, we cannot calculate the time of collision between "a" and "b" because that will be wrong.
            # Since "b" has already collided with "c", it means, "a" will now collide with a fleet that resulted after collision of "b" and "c"
            # Hence, "b" is no longer required for us to calculate collision time for "a" because it collided with "c" already before it would collide with "a"
            
            # That's why, the second condition in while loop is to check 
            # if the time taken for current car to collide with car on top of stack is greater than the time that car on top of stack took to collide with any other car
            # Then it means, the car on top of stack has already collided with a car before the collision with current car could occur
            # Hence, we no longer need the car that is on top of stack so we pop it
            
            while stack and ((cars[i][1] <= cars[stack[-1]][1]) or (answer[stack[-1]] > 0 and self.getTime(cars[i], cars[stack[-1]]) > answer[stack[-1]])): stack.pop()
            # At this point, we have removed all the cars that won't cause any collision with current car
            # But, if the stack is not empty, it means, there is a car on top of stack that will caruse a collision
            if stack: 
                # Now, we can put the time at which both collided in the output list
                answer[i] = self.getTime(cars[i], cars[stack[-1]])
            
            # And finally, push the current car's index to the stack
            # Because it might be a useful data for previous cars that we are about to traverse
            stack.append(i)
            
        return answer
    

cars = [[3,4],[5,4],[6,3],[9,1]]
print("Output ->", Solution().getCollisionTimes(cars))