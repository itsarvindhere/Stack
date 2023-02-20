# PROBLEM STATEMENT

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# EXAMPLE

    Input: asteroids = [5,10,-5]
    Output: [5,10]

Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# **APPROACH #1 USING STACK**

Since we have to compare an asteroid with all valid asteroids before it with which it can collide, we can make use of a stack here. So for example, we we have a stack such as [10,5]

And we get a new value as "-3", we know that it will collide with the asteroid before it because the asteroid before it is moving towards right and the current asteroid is moving towards left. And after exploding, 5 will destry -3 so there will be no change in the stack.

If it was the other way around -> stack = [10,3] and new asteroid's size as "-5", then the new asteroid would've destroyed the previous one and the stack would've become [10,-5]

So, all of this we can do efficiently using a stack in O(N) time.

Also, when it is time to push an asteroid to stack, we have to check these two conditions - 

    1. Stack is empty (Which means either it is the first asteroid or the current asteroid destroyed all previous asteroids)
    2. Stack is not empty (which means, the previous and current asteroids are moving either in same direction or away from each other)


# **APPROACH #2 USING STACK**

We can make the above code even better. Just think about it. If current asteroid is moving towards right, does it have any change of colliding with any asteroid on its left? NO! 

And that's the optimization we can add to our code.

So, if current asteroid moves towards right side, there is no need to do all the computation for it and we can simply push it to the stack.

This also means, at the end of our for loop when we are checking the conditions, we no longer have to consider the case when stack > 0 as we have already covered it in the beginning. So the only case we have to take care of now is when the current asteroid moves towards left but so does the asteroid before it.