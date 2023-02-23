# PROBLEM STATEMENT

You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

# EXAMPLE

    Input: properties = [[5,5],[6,3],[3,6]]
    Output: 0

Explanation: No character has strictly greater attack and defense than the other.

# **1. BRUTE FORCE APPROACH - O(N^2) - TLE**

So, if we were asked to write the Brute force solution, what would it be?

For every character, we would simply check the whole list for any other character with a strictly greater attack and defense values. If we found one, that means, current character is a weak character so we can increment the count.


    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        count = 0
        
        n = len(properties)
        
        # For each character
        # We will go through every other character to see if there exists a character 
        # with strictly greater attack and defense
        for i in range(n):
            attack1,defense1 = properties[i]
            for j in range(n):
                attack2, defense2 = properties[j]
                
                # If there exists such a character
                # We will increment our count and exit this inner loop
                if attack2 > attack1 and defense2 > defense1: 
                    count += 1
                    break
                    
        
        return count
		
# **2. SORTING APPROACH WITH STACK - O(NLogN)**

How can we optimize the above code?

How to avoid going through the entire list for each character?

If our list was sorted by the attack values, doesn't that mean, for every character, we will find a character with strictly greater attack and defense on right side only?

	Take an example => [[5,5],[6,3],[3,6]]
	
	If we sort this list based on attack values in increasing order, 
	
	we get [[3,6],[5,5],[6,3]]
	
	If now we take [5,5], we know that we can find a stronger character on its right only. 
	
	There is no need to check for previous characters since all will have a smaller attack value only.
	
	Here, we will make use of stack.
	
	Basically, at any time, top of stack will give us the character on right with the largest defense value so far.
	
	For example, initially, stack will be [3] (Defense value for [6,3] is 3)
	
	Then, when we are at [5,5], we see that "5" is larger than "3' so it means "3" is now useless.
	
	Stack becomes [3]
	
	Next, we have [3,6], 
	
	Again, here we have defense value as "6" but stack has "3", so stack is updated.
	
	And finally, we conclude that there are no weak characters at all. 

	
While this approach may sound simple, things get a bit complicated when there are characters with the same attack values but different defense values.

 Consider this case => [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
 
 If we were to sort this list based on attack values, we would get - 
 
		[[6, 9], [7, 5], [7, 9], [7, 10], [10, 4], [10, 7]]

       Now, let's see what will be the issue with this case.
	   
	   Basically, at any time, top of stack will give us the character on right with the largest defense value so far.
	   
	   So, suppose we are at [10,4]. In that case, top of stack will give us 7.
	   
	   And if the top of stack has a greater defense value than current character, we will say that the current character is weak.
	   
	   But did you see the issue with this case?
	   
	   When we are at [10,4], we see stack has value "7" on top so [10,4] should be a weak character as per our logic.
	   
	   But we can see that it is not true since attack values are the same.
	   
	   Now, even if we write a logic so that we also check for equal attack values, this will not be enough to get a correct answer.
	   
	   And the reason is same attack values for multiple characters.
	   
What if, our sorted list had [10,4] after [10,7]. That is, for same attacks, the bigger defense value is placed before the smaller value.

		In that case, initially, stack would've had [4] on top.
		
		But as soon as we get to [10,7], we would've removed the "4" since it would become useless.
		
		And here we see we do not increment the count for weak characters since "4" is already rejected and popped from stack.
		
So, it means, our logic will work if we sort the list in such a way that, if two characters have same attack values, they are sorted based on their defense values in decreasing order. 

	That means, for the above example, list after sorting will become -> [[6, 9], [7, 10], [7, 9], [7, 5], [10, 7], [10, 4]]

And now, we can see that our logic will work as expected.

Initially ,stack as [4], then we see that in [10,7], the defense value 7 is bigger. So we remove the "4" and stack now becomes [7]

Then we get to [7,5]. We see that 5 is not greater than 7 which means, [7,5] is a weak value so count becomes 1.

Next, we have [7,9]. We see that 9 is greater than 7 so stack is updaetd to [9]
Next, we have [7,10]. We see t hat 10 is greater than 9 so stack is updated to [10]

And finally, we have [6,9]. We see that stack has [10] on top and current character's defense is "9". So it means, it is a weak character.

Count becomes 2.

Hence, in [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]], there are two weak characters and these are [6,9] and [7,5]


# **3. SORTING APPROACH WITHOUT A STACK - O(NLogN)**

What are we using the stack for? We are using it to keep the biggest defense value so far, right? But isn't that something we can do with just simple variable? 