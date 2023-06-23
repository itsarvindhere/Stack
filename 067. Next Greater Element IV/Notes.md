# PROBLEM STATEMENT

You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must find its respective second greater integer.

The second greater integer of nums[i] is nums[j] such that:

 - j > i
 - nums[j] > nums[i]
 - There exists exactly one index k such that nums[k] > nums[i] and i < k < j.

If there is no such nums[j], the second greater integer is considered to be -1.

 - For example, in the array [1, 2, 4, 3], the second greater integer of 1 is 4, 2 is 3, and that of 3 and 4 is -1.

Return an integer array answer, where answer[i] is the second greater integer of nums[i].

# EXAMPLE

    Input: nums = [2,4,0,9,6]
    Output: [9,6,6,-1,-1]

Explanation:
0th index: 4 is the first integer greater than 2, and 9 is the second integer greater than 2, to the right of 2.
1st index: 9 is the first, and 6 is the second integer greater than 4, to the right of 4.
2nd index: 9 is the first, and 6 is the second integer greater than 0, to the right of 0.
3rd index: There is no integer greater than 9 to its right, so the second greater integer is considered to be -1.
4th index: There is no integer greater than 6 to its right, so the second greater integer is considered to be -1.
Thus, we return [9,6,6,-1,-1].

# APPROACH

VIDEO EXPLANATION - https://www.youtube.com/watch?v=Up8p_jfktZs

Here, we will use two stack (three to be precise). 

So, one thing is clear. To get second greater, we need to know first greater. And we know how to find first greater element on right with stack.

What we will do is, we will maintain two stacks. Lets call them stack1 and stack2.

 - Stack1 will always have elements that do not have next greater element yet
 - Stack2 will always have elements that have next greater element


    For example - nums = [2,4,0,9,6] 

    Here, suppose we have stack1 and stack2

    When we start, we have "2". 

    Since right now, stack2 and stack1 are  empty already, we put it in stack1

    stack1 = [2]
    stack2 = []

    Next, we have "4"

    We see that "4" is greater than "2" that is top element of stack1
    So what does it mean? It means, "4" is the next greater element of "2"

    And so, "2" does not belong in stack1 now. It belongs in stack2

    stack1 = [4]
    stack2 = [2]


    Next, we have "0"
    "0" is not greater than "2" or "4" . So "0" stays in stack1 with "4"

    stack1 = [4,0]
    stack2 = [2]

    Next, we have "9"

    Now, we first check if "9" is greater than "2'. IT IS!

    What does this mean? It means, "9" is second greater element for "2".
    So, for element "2" we found second greater so we can pop it from stack2 and update output list.
    
    output = [9,-1,-1,-1,-1]    
    stack1 = [4,0]
    stack2 = []

    But, "9" is also greater than "4" and "0"

    So it means both "4" and "0" do not belong in stack1. They belong in stack2

    But do note that we want to maintain the order in which we inserted elements. 
    So we cannot just pop from stack1 and push in stack2 because in that case, "0" will be put before "4"
    So, we will use a temporary stack to take "4" and "0" from stack1 and put them in temp stack.

    So, temp stack will become [0,4]

    Now we can take elements from temp stack and put them in stack2.

    output = [9,-1,-1,-1,-1]    
    stack1 = [9]
    stack2 = [4,0] 

    Next, we have "6"

    Is "6" greater than "0"? YES. So "6" is second greater for "0"

    output = [9,-1,6,-1,-1]    

    And similarly, "6" is greater than "4" so "6" is second greater for "4"

    output = [9,6,6,-1,-1]   

And loop ends.


So, the output is [9,6,6,-1,-1]