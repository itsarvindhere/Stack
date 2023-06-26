# PROBLEM STATEMENT

You are given a string s, an integer k, a letter letter, and an integer repetition.

Return the lexicographically smallest subsequence of s of length k that has the letter letter appear at least repetition times. The test cases are generated so that the letter appears in s at least repetition times.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.


# EXAMPLE

    Input: s = "leet", k = 3, letter = "e", repetition = 1
    Output: "eet"

Explanation: There are four subsequences of length 3 that have the letter 'e' appear at least 1 time:
- "lee" (from "leet")
- "let" (from "leet")
- "let" (from "leet")
- "eet" (from "leet")
- 
The lexicographically smallest subsequence among them is "eet".

# APPROACH

We want a "k" length subsequence that has at least "repetition" number of "letter" characters. 

And that subsequence needs to be lexicographically smallest. 

This problem can be solved efficiently using a Stack because otherwise, you won't be able to write a solution that gets accepted due to the constraints.

So, as we traverse the input string, we will keep pushing the characters in the stack. Now in this process, we may or may not pop from the stack. We will pop only if we see that popping will make the ongoing subsequence lexicographically smallest as well as will ensure that we get at least "repetition" number of "letter" characters.

Now the question is, what are situations we may encounter?

For that, we have to analyze a few examples. 

	Suppose, we have  s = "laeet", k = 3, letter = "e", repetition = 1
	
	It means, generate a lexicographically smallest subsequence of length 3
	with the letter "e" occuring at least once.
	
	So, if we start putting characters in stack from left to right.
	
	Initially, stack is empty. So we simply put "l" in stack
	
	stack = ["l"]
	
	Next, we have "a". Here, what do we see? 
	
	We see that top of stack has "l". And the current character is "a".
	
	And since "a" is smaller than "l", instead of "l", we should put "a"
	to get a lexicographically smaller subsequence than current ongoing subsequence.
	
But then again, we need to think. What can be the consequences of removing "l"? 
	
	What if we had the input string as "lae" and k = 3?
	
In that case, it would not be ideal to remove any character at all since we want a subsequence of length 3
and the length of string is also 3

So, when we pop, we also need to make sure that we have enough characters with us to get a "k" length subsequence even if we pop the top of stack. Only if that is True, we can pop.

And that's the reason why in the code, you will see that when the top of stack is greater than current character, then we pop only if a certain condition is true -

		if (k - len(stack)) < (n - i): stack.pop()
		
What does this mean? 

	k -> Length of subsequence we have to generate
	len(stack) -> Length of stack at this point
	k - len(stack) -> Characters the subsequence requires so that its length is "k"
	(n - i) -> Characters we still have to traverse
	
So we are saying, only pop the top of stack if the number of characters that subsequence is requiring, is less than number of characters that we still have to traverse.

And that's just one case. 

What can be some other case? 

Another case can be if  the top of stack has a greater character than current character but also, the top of stack is "letter" itself.

	For example, s = "eatxyzw", k = 2, letter = "e" and repetition = "1"
	
	Here, when we put first character in stack, stack = ["e"]
	
	But then, when we have "a", then we see that "e" is greater than "a"
	
	So, ideally, we should remove "e" so that we get a lexicographically smaller subsequence 
	
But, the issue is, "e" is also the "letter" and so we cannot remove it just like that. 

Here, the condition (k - len(stack)) < (n - i) is also True but still we see that removing "e" will be a wrong step.

So this means, whenever we have a character on top of stack that is not only greater than current character but is also the "letter" itself, then we have to think of an additional condition on the basis of which we can remove or not remove.

Here, why we cannot remove "e"? Because we know that there is only one "e" in this whole input string and also, we want "e" to appear at least once in the final subsequence. So that's why we cannot pop it. But, if we had "eaetxyz" then we would've removed it because we have an extra "e" on the right of "a" so we know that even if we remove the first "e", we still have an "e" on the right.

	And that's why we have pre computed the number of "letter" characters 
	on the right of each character in input string.
	
This will help us in this specific case when the top of stack is a letter and is also greater than the current character.
So, now, the condition to pop() in this case is -> 

	if countOnRight[i] > repetition and (k - len(stack)) < (n - i): 
		repetition += 1
		stack.pop()
		
Note that as we pop, we are also incrementing the "repetition" because we know that we now have one extra "e" to find and put in the subsequence.

Similarly, when we will push a "letter" into the stack, we will decrement the "repetition" because we now have one less "e" to find.

Finally, there will also be a case where the top of stack has a smaller character than current character but we still have to pop.

For example, s = "aee", letter = "e", k = 2 and repetition = "2"

	Initially, stack will have "a" => ["a"]
	
	Then, when we are at "e", we see that top of stack has a smaller character
	So it means, right now our subsequence is the smallest that it can be.
	
	But, still, if you see, we cannot keep "a" in the final subsequence. Why?
	
	because, since length of stack is "1", it means, we have already put one character in our subsequence.
	
	So, the number of characters left to put are k - len(stack) -> 2 - 1 => 1
	
	But, we still have repetition = 2
	
This means, we have space of only 1 character in our subsequence but we still have to put 2 "e" characters. That cannot be possible. So, to make space for two "e" characters, one element needs to be popped from top of stack. And that's why we pop "a" here.

Hence, the condition will be -> 

		if k - len(stack) < repetition:  stack.pop()
				 

And that's the whole idea of this solution.
 