# PROBLEM STATEMENT

A string is a valid parentheses string (denoted VPS) if it meets one of the following:

    - It is an empty string "", or a single character not equal to "(" or ")",
    - It can be written as AB (A concatenated with B), where A and B are VPS's, or
    - It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:

    - depth("") = 0
    - depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
    - depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
    - depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

# EXAMPLE

    Input: s = "(1+(2*3)+((8)/4))+1"
    Output: 3

Explanation: Digit 8 is inside of 3 nested parentheses in the string.

# APPROACH

Before discussing the approaches, just understand what "depth" actually means.

It means, how deep a specific character is in a string. And that deepness depends on the brackets. 

	For example, if we have a string "(((1)))"

Then we say the depth of 1 is "3" because there are three nested brackets inside which "1" is placed.

	 What if we had "()((1))"?
	 
In this case, the depth would be "2" because there are two nested brackets inside which "1" is placed.

We did not count the first bracket because it was closed before we reached 1.

And that's the whole idea. It is all about how many open brackets are there so far which have not been closed yet. 

That's the depth for any character.

# BRUTE FORCE APPROACH

In the Brute Force approach, for any character, we will go through the whole string from beginning to that character to see how many open brackets we find that have not been closed yet.

It won't give any TLE due to the constraint being so small but with this, we can start to think about a more efficient solution.

# STACK APPROACH

See, for any character, all we want is to find how many opening brackets are there before it, that have not been closed yet, right?

So, why not use a Stack for that purpose. Our stack will simply store the opening brackets such that any time we want to find how many opening brackets are there that haven't been closed yet, we simply take the length of stack for that.

And if we encounter a closing bracket, we know that one opening bracket has been closed so in that case, we will pop.

The downside is that we are using extra memory. But still, this is a much better solution than the Brute Force one.

# CONSTANT MEMORY APPROACH

One thing that's common in both the above approaches is that, all we want is to keep track of how many brackets are open so far that have not been closed yet. 

Isn't that something a simple counter variable can do? Why use extra memory for that?

