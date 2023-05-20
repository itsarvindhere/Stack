# PROBLEM STATEMENT

There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

 - positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
 - speedi is the initial speed of the ith car in meters per second.


For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.


# EXAMPLE

    Input: cars = [[1,2],[2,1],[4,3],[7,2]]
    Output: [1.00000,-1.00000,3.00000,-1.00000]

Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.


# STACK APPROACH

A car can collide with any car on its right only if that right car is moving slower than the current car.

So basically, if we know that there is a slower car on right of a car, we can easily find when the two will collide.

This problem is a variation of one of the most basic stack problems which is "Nearest Smaller on Right". In the Nearest Smaller on Right problem, for each element in the array, we have to find what is the nearest smallest element on right side. And what we do is, we loop in reverse (right to left), and for each current element, we check what is the top of stack. If top of stack has a bigger element, it is of no use since current is smaller. But if top of stack has a smaller element, then it means that's the nearest smaller on right.

I explained the "NSR" problem and its solution because that's exactly what we have to use in this problem, with a slight variation.

Here, we are dealing with the "Nearest Smaller 'speed' on Right".

So, the basic approach remains the same. That is, we will loop from right to left and if current car is moving slower than the car that is on top of stack, then the top of stack is of no use so we can pop it off. 

But now comes the one extra part.

	Suppose, we have cars = [[3,4],[5,4],[6,3],[9,1]]
	
	Initially, output = [-1.00000 ,-1.00000, -1.00000, -1.00000]
	
	We start from right to left and initially, stack is empty.
	
	We put the index of last car in the stack. Stack = [3]
	
	Next, at i = 2 we have [6,3]
	
	We check the speed of car on top of stack.
	The car on top of stack is [9,1] and its speed is 1, lower than speed of current car.
	
	It means, current car will collide with the car on top of stack.
	And to calculate the time, we can simply use the formula ->
		(distance between two cars) / (speed difference between two cars)
		
	So, it means, the two will collide at time = (9 - 6) / (3 - 1) => 3/2 => 1.5 seconds
	
	And so, we will push this value 1.5 in the output list for current car.
	
	output = [-1.00000 ,-1.00000, 1.50000, -1.00000]
	
	And we also push the current car's index in stack.  Stack = [3,2]
	
	Next, at i = 1, we have [5,4]
	
	At top of stack, we have car at index 2 that is [6,3]
	
	We see that since top of stack has a car with a lower speed than current car, they should collide.
	But, we also need to think that the car on top of stack could've collided with other car already 
	before it collides with current car.
	
	Let's calculate the time at which cars [5,4] and [6,3] collide.
	
	Time = (6 - 5) / (4 - 3) => 1s
	
	And if we check our answer list, then we know car with [6,3] collided with the car [9.1] at 1.5s
	
	It means, that the car [6,3] will collide with car [5,4] first. And then it will collide with the car [9,1].
	
	How did we figure this out? We used the same formula for time that we used in previous step.
	
Hence, this is the extra step we need to take. 
	
We need to make sure that we are also removing the car from stack that has already collided with any other car on right, before it collides with current car. Because if the car on top of stack has already collided with a car on right, then it would've formed a new fleet of speed and distance same as the car with which it collided. In simple words, in this case, the car on top of stack is of no use now so we pop it.

	Coming back to our example, since [6,3] collided with [5,4] first, we do not pop it. 

	Output list becomes  [-1.00000 ,1.00000, 1.50000, -1.00000]
	So, stack becomes [3,2,1]
	
	Finally, we have i = 0 and car = [3,4]
	
	Now, at top of stack, car at index 1 is present -> [5,4]
	
	The speeds are same so we pop the top of stack.
	
	Now, at top of stack, car at index 2 is present -> [6,3]
	
	The speed of car at top of stack is slower than current car. So current car should collide with it right?
	
	Again, we have to check the time.
	
	Time taken for [3,4] to collide with [6,3] => (6 - 3) / (4 - 3) => 3 seconds
	But as we know, [6,3] collided with [9,1] in 1.5 seconds
	
	So, before [3,4] could collide with [6,3],
	[6,3] had already collided with [9,1]
	
	Hence, [6,3] should be popped as well,
	
	And now, we are left with [9,1]
	
	Not only the speed is slower than [3,4], but [9,1] never collided with any other car.
	
	So, the two will collide.
	
	And time for collision will be => (9 - 3) / (4 - 1) => 6 / 3 => 2 seconds
	
So, finally, output comes as [2.00000,1.00000,1.50000,-1.00000]

Do Note that to check if a car has already collided with any other car, we can simply check if for it, the time in output list is positive or not. Because only if time is positive we can be sure that it collided with any other car.