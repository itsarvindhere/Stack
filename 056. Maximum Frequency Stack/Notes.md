# PROBLEM STATEMENT

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

 - FreqStack() constructs an empty frequency stack.
 - void push(int val) pushes an integer val onto the top of the stack.
 - int pop() removes and returns the most frequent element in the stack.
 - If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

# EXAMPLE

    **Input**

    ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    [[], [5], [7], [5], [7], [4], [5], [], [], [], []]

    **Output**
    [null, null, null, null, null, null, null, 5, 7, 5, 4]

    **Explanation**

    FreqStack freqStack = new FreqStack();
    freqStack.push(5); // The stack is [5]
    freqStack.push(7); // The stack is [5,7]
    freqStack.push(5); // The stack is [5,7,5]
    freqStack.push(7); // The stack is [5,7,5,7]
    freqStack.push(4); // The stack is [5,7,5,7,4]
    freqStack.push(5); // The stack is [5,7,5,7,4,5]
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

# OPTIMAL APPROACH


So, the optimal approach is using two dictionaries / hashmaps.

Why two? 

Because, while we will use one to keep track of frequency of each number, just as we did in the above approach, we will use the second dictionary to keep track of what all elements have a particular frequency.

Now, how will this help us? This will help us in making sure that in case we have multiple elements with the same frequency, we always pop and return the one that was most recently pushed.

Just take an example and you will understand. 

	Suppose, at any point, we have our second dictionary as - 
	
	{ 2 : [5] , 1 : [3]}
	
	It means, "5" is the only number that appears twice and "3" is the only number that appears once.
	
	Now, if we push one more "3", then our dictionary will be like - 
	
	{ 2 : [5,3] , 1 : [3]}
	
	So, as you can see, the most recently popped element will always be the last element of the list.
	
	And so, now if we want to pop and return the most frequent element, we know that we simply need to pop from the list [5,3]
	
	At this point, you would've also understood that we also need to keep track of what is the maximum frequency at any point.
	
	And for that, we will have a third variable that gives us the maximum frequency at any point.
	
	As we push an element, it is possible that we get a new maximum frequency so we will update accordingly.
	
	And as we pop, we need to update the frequency accordingly.
	
	See, take the above example.
	
	{ 2 : [5,3] , 1 : [3]}
	maxFreq = 2
	
	At this point, the maximum freq is 2 so if we pop, we will get "3".
	
	Dictionary will become - { 2 : [5] , 1 : [3]}
	
	Now, do you think there is any need to update maxFreq here? NO! Because the list for "2" still has an element. 
	
	And that's the whole point. We will only update maxFreq in pop operation, 
	when we know that after popping, the list is empty.


And keeping all this in mind, here is the simple and easy to understand code.