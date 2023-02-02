# PROBLEM STATEMENT

There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

# EXAMPLE

    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3

Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

# APPROACH

We are given "position" and "speed" of each car. So this means, we can easily calculate how much time each car is going to take to reach the target, right?

Because time = distance/speed and for each car, its distance to target = (target - position)

And once we get the time for each car and that time is sorted by position of each car, then we can easily find which car will have to slow down and hence join the fleet.

	Suppose, we have target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
	
	If we sort by position, we get 
	
	position = [0,3,5,8,10], speed = [1,3,1,4,2]
		 
	Now, when we calculate the time each car is going to take to reach the target, we get
	
	time = [12, 3, 7, 1, 1]
	
	Car at position 0 takes 12h to reach target
	Car at position 3 takes 3h to reach target 
	Car at position 5 takes 7h to reach target 
	Car at position 8 takes 1h to reach target 
	Car at position 10 takes 1h to reach target 
	
	Now, it is like a real world scenario of a single lane road. 
	
	If you are driving your car fast, then unless the next car is driving at a greater speed, 
	you do not have to slow down.

	But if next car itself is driving slow or at the same speed as you, you can do nothing and have to match your car's speed to next car.
	
	And so your car will now also take the same time to reach target as that slow car 
	
	because you cannot get ahead of next car. This means you will join the fleet of next car (which is itself a fleet).
	
And hence, the whole idea is, if a car does not join a fleet on its right, then we can consider it as a fleet in itself.
But if it does, then there is no need to consider that car because it will be taking same amount of time 
as the slowest car of the fleet it joins.

And that's why, when we want to push a car to the fleets stack, we can only do it if the car on its right takes less than to reach target.

# USING A STACK

A car joins a fleet on right only if there exists a fleet that takes more time to reach target than current car.

Otherwise, the current car will start a new fleet of its own.

So for each car, we want to find the first car on its right that is slower than it. And that's the simple idea of Nearest Greater on Right.

If there is no slower car on its right, it means, the current car will start a new fleet.