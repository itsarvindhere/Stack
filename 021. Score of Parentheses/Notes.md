# PROBLEM STATEMENT

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

 - "()" has score 1.
 - AB has score A + B, where A and B are balanced parentheses strings.
 - (A) has score 2 * A, where A is a balanced parentheses string.


# EXAMPLE

    Input: s = "(())"
    Output: 2

# APPROACH

Like other parenthesis problems, we can make use of a stack to solve this problem.

It is given that if we have something like "(A)", where A is a balanced parenthesis string, then the score will be 2 * score of A.

For example, if we have "(())"

Then here, we can see that inside the first opening bracket and last closing bracket, we have another "()". The score of this inner part is 1 so the score in total of all the string will be 2 * 1 => 2


Hence, using a stack what we can do is, as we encounter an opening bracket, there are two possibilities -

    1. The next bracket is a closing bracket 
    2. The next bracket is an opening bracket

First possibility Means that the score will simply be "1". But 2. means that there is another balanced  parenthesis string inside so we first need to find its score.

Hence, as soon as we find an opening bracket, we will push its score to the stack initially as 0. 

ANd as we find a closing bracket, we will pair it with the opening bracket on top of stack by taking the score of opening bracket and taking the maximum of either "2 * score" or "1". Because if the score is 0, then it means 2 * score will be 0 so in that case we will take "1" as the score.

     s = "(())"

     First, we have an opening bracket. 
     
     So we push score 0 to stack.

     Stack = [0]

     Next, we again have an opening bracket.

     Stack = [0,0]

     Now, we have a closing bracket. 

     So, take the score on top => 0

     And take maximum of 2 * score or 1

     Here, maximum is 1. So it means, score of "()" is 1.

     AT this point, stack is looking like [0] and we have score as 1 for the current pair.

     So what we will do now is increment the score on top of stack by the score we got. Because that makes sense now that we are done finding the score of inner balanced parenthesis substring.


     stack = [0 + 1] => [1]

     And next, we again encounter the closing bracket.

     So we do the same process. 

     Take the maximum of (2 * 1) and (1) and choose that as the score. And if the stack has score on top, add the score to it.

     Here, 2 is the maximum score out of 2 and 1. So, we will take 2. 

Now if you see, we have already popped the top, stack is empty so there is no place to put this score back into the stack. Hence to avoid such condition, we will initialize the stack with one value in it -> 0.


And so, when the loop ends, stack will have one value only which is the score of parenthesis.
