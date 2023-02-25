# PROBLEM STATEMENT

There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

The number of collisions can be calculated as follows:

 - When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
 - When a moving car collides with a stationary car, the number of collisions increases by 1.
  
After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.

# EXAMPLE

    Input: directions = "RLRSLL"
    Output: 5

Explanation:

The collisions that will happen on the road are:

    - Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
    - Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
    - Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
    - Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
    - 
Thus, the total number of collisions that will happen on the road is 5. 

# STACK APPROACH - O(N) Time & O(N) Space

The code is well commented but still, here is what we are doing -

    1. If a car is stationary and there are cars before it that are moving towards right, all will collide with it
    2. If a car is moving towards left and previous car is moving towards right, both will collide
        2.1. And after collision both become stationary. Which again means the same as first point. 
            That is, if there are cars before these two and they are moving towards right, all of them will collide
    3. If a car is moving towards left and previous car is stationary, both will collide.
   
So we see that points 1 and 2 are the same and the only thing that's different is the initial directions of the two cars and the count by which we have to increment our number of collisions.


# WITHOUT STACK APPROACH - O(N) Time & O(1) Space

From the stack approach, what did we understand?

	If a Car is stationary, all the cars moving towards it previously will collide
	If a car is moving towards left, all the cars moving towards right will collide with it
	If a car is moving towards left and previous car is stationary, there will be only one collision
	
So, do we even need a stack for this? We can easily keep track of how many cars are moving towards right at any time using a simple counter variable.

And similarly, we can use a variable to keep track of what was the previous car's direction.

And that's the idea of the O(1) space approach.

DO note that when current car is moving towards left and previous car is moving towards right, the total number of collisions will be - 
		
			Count of cars moving towards right + 1
			
Example: If we have "RRRL"

Then, when the last car collides, count will be incremented by "2" and now cars will become stationary.

In other words, the string will now be "RRSS"

This means, the previous cars that were moving towards right will now increment the count of collisions by only 1, not by 2. 

So for this case, total number of collisions -> 2 + 1 + 1 => 4 => (Count of Cars moving towards right + 1)