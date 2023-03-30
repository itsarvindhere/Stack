# PROBLEM STATEMENT

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

# EXAMPLE

    Input: nums = [3,1,4,2]
    Output: true

Explanation: There is a 132 pattern in the sequence: [1, 4, 2]

# BRUTE FORCE APPROACH

Doing it Brute force way, there are two ways. 

First is to have "3" nested loops, each for "i", "j" and "k". So that would be O(N^3) that would never be accepted for large test cases.

Second is to have only "2" nested loops by fixing one value. Since "j" is the middle value, we can fix "j" and then try to see if we have a valid "i" and "k" values.


Since "k" value needs to be greater than "i" value but smaller than "j" value, if we somehow "minimize" the "i" value and maximize the "j" value, it means we would have a larger range of values that can be "k". So we would want to have a value that is in the range (i,j).

Hence, what we can do is, for each index, we will also keep track of what is the minimum value so far on left.

This minimum value will be our "i" value for any "j" value we choose.

So in case this "i" and "j" are not the same, that means, the only thing left would be to find a "k" value after "j" index which is less than "j" value but greater than "i" value. If we can found one, that would mean there is a 132 pattern.


    Example - [3,1,4,2]

    If we create an array to store the minimum value till any index so far, we would get - 

    minOnLeft = [3,1,1,1]


    Now, we start our loop where we take each index as a potential "j" value.

    Again, note that any index can be a "j" index only if the smallest value in the range [0,j] is not "j" itself.

    nums = [3,1,4,2]


    So based on this fact, index 0 is automatically not going to work.

    At index = 1, we have the value  = 1. We check the minLeft array to see what is the minLeft[1]. We see it is "1" itself. So it cannot be "j" value.

    At index = 2, we have "4". We check the minLeft array to see what is the minLeft[2]. We see it is "1". Since 1 != 4 it means we now have a "j" value and an "i" value.

    Now what's left is to search on the right of "4" for a "k" value, if any.

    Here, there is only one value on right of "4" and that's 2.

    We see that not only 2 < 4 but 2 > 1

    It means, "2" is a valid "k" value such that nums[i] < nums[k]>  nums[j] so we have a 132 pattern hence we return True.

# STACK APPROACH

SOURCE - https://www.youtube.com/watch?v=q5ANAl8Z458

We can solve this problem in O(N) time by using a Monotonic Stack.

See, the reason why even above approach fails is because it is O(N^2). It is O(N^2) because of the inner loop we run from j + 1 to n - 1.

What if, at any point, we can see if we have a valid "j" and a valid "i" value with us?

That is something we can do using a Monotonic Stack. Here we will use a Monotonically Decreasing stack which means, at any time, the top of stack will be the smallest. And the bottom of stack will be the largest.

In this way, if at any time, we have a value in stack that is greater than the current value that loop points to, then we can say that we have a "k" and a "j" value with us.

And for "i", it remains same as above. That is, a separate minLeft array to keep track of minimum so far at each index.


    Example - [3,1,4,2]

    minLeft = [3,1,1,1]
    stack = []

    At index = 0, we have "3". 

    But we see that stack is empty which means even if we take "3" as the "k" value
    There is no valid "j" value or an "i" value yet. So we just cannot take it as a "k" value.

    Also, since Stack is empty, we just push 3 to stack.

    stack = [3]

    AT index = 1, we have "1"

    Suppose we take "1" and make it the "k" value
    And we make "3" as the "j" value. Great, right?

    What about "i" then? The smallest so far is "1" itself. But k value needs to be bigger than "i" so it is not a valid combination. Hence, no 132 pattern here as well.

    Also, "1" is smaller than the top of stack (3). SO pushing "1" won't disturb the order of our monotonic decreasing stack.

    stack = [3,1]

    At index = 2, we have "4"
    We see that if we want to push "4" to stack, it will disturb the order since all values before it are smaller. Hence, we have to remove the smaller values first before pushing "4".

    So, we remove all the smaller values. 

    But now our stack becomes empty. Which means, if we make "4" as our "k" value, then there is no valid "j" value before it because stack is empty. Hence, we don't get 132 pattern here too.

    stack = [4]

    AT index = 3, we have "2".
    "2" is smaller than the top of stack (4). SO pushing "2" won't disturb the order of our monotonic decreasing stack.

    And we also see that if we take "2" as "k" and top of stack (4) as "j", then we still have the option to take "i" as the minimum value in the range [0,j], which is "1"

    Since nums[i] = 1, nums[j] = 4 and nums[k] = 2 make a 132 pattern hence, we found one pattern so we return True.

    
