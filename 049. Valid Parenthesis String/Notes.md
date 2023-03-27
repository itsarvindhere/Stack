# PROBLEM STATEMENT

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

 - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
 - Any right parenthesis ')' must have a corresponding left parenthesis '('.
 - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
 - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


# EXAMPLE

    Input: s = "(*))"
    Output: true

# STACK APPROACH

We greedily try to match the right parenthesis with an opening bracket if there exists any before it, instead of using a previous "star" as opening bracket.

	Why?  Because the "star" is optional to use. 
	
	"star" should be a second option when we do not have any opening brackets to match with a current closing bracket.
	
The simplest way to think of the solution for this problem is to ignore that we even have a choice to use stars. Just think that we are asked to check if a parenthesis string is valid or not which has only "(" or ")". How will we do that? That is simple right? We will just try to match a closing bracket with an opening bracket if there is one. If not, we can say that this string is not valid.

Now, just add in the "star" option. This just means we have now one extra option to use in case there is no opening bracket to match with a closing bracket. In that case, we can see if we have stars to use as opening brackets.

And this means, we need to keep track of the previous opening brackets & also the previous stars. A stack will be the best data structure in this case. In fact, whenever you see parenthesis related problems, stack is the first thing you should think of.

So, we take two stacks, one to keep track of opening brackets, and the other to keep track of stars.

Then, we traverse the whole string and if we get an opening bracket or a star, we can simply put the index in the respective stacks. Why indices? You will get that later.

If we get a closing bracket, we do what we discussed above. We first check if we have any opening brackets with us. If yes, we pop from opening brackets stack because we have paired one opening bracket with a closing bracket.

if not, we will then check if we have any stars with us. If yes, we pop from stars stack because we have paired one star (we used it as an opening bracket) with a closing bracket.

And if both are not available, it means there is no way at all to make this string a valid string. Because we have no opening brackets or stars to pair with current closing bracket. In that case, we can straight away return False.

Now comes the fun part. Once we are done with this step, it is possible that we will have some unmatched opening brackets left with us. And as you might have guessed it, we will now use the available stars as "closing brackets". But there is a catch.

For any opening bracket at index "i", we can use a star as a closing bracket only if it is present at an index greater than "i". Or in other words, we can pair a star with an opening bracket only if it exists on the right of the opening bracket in the original string.  If for any opening bracket, we do not have any star on its right, there is no way to make this string a valid string hence we can return False.

And that's what we are going to check and that's why we pushed indices in the stacks, not the characters themselves.

And if we can successfully do this, we should have an empty stack of opening brackets, meaning, all the opening brackets matched.
 