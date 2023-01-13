# PROBLEM STATEMENT

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

 - For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
 - Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

Implement the StockSpanner class:

 - StockSpanner() Initializes the object of the class.
 - int next(int price) Returns the span of the stock's price given that today's price is price.


# EXAMPLE

    Input
    ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    [[], [100], [80], [60], [70], [60], [75], [85]]
    Output
    [null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6


# 3 APPROACHES

## **APPROACH #1 - FOR A PRICE, FIND HOW MANY PRICES AS <= IT BEFORE IT**

This is probably the one solution that will instantly come into someone's mind after reading the problem statement. We can simply keep storing all the prices in a list and as the next() method is called, we will simply loop backwards to see till how far we can go. That is, how many prices before the current day were <= current day's price.

But think about it. The constraints say that "At most 10^4 calls will be made to next." So, in the worst case scenario, our reverse loop may run till the 0th index in each next() call. So now you can imagine the complexity. Hence, for some large test cases, this approach will give TLE in Python.

## **APPROACH #2 - USE A STACK TO OPTIMIZE**

Since all we want is to check how many prices before today were <= current day's price. So, what if we have already figured out how many prices were <= the price of yesterday? In that case, if the yesterday's price is <= current day's price, we know that we will cover all the prices that yesterday's price spanned over.

And here, we can make use of a Stack because this is simply the problem of "NEAREST GREATER VALUE ON LEFT".

We will use our stack to keep only the useful values. That is, we will keep only those prices in the stack that are greater than the current day's price. And we will remove all those that are smaller or equal. So that, we can quickly find out how many days are there before current day where price is <= current day's price.

Take this example - 

		Suppose, first price is 100. Since it is the first price, its span is simply 1.
		
		list = [100]
		stack = [0] ---> We will keep the indices in the stack
		
		Next, we have 80.
		Our stack is not empty, so we want to remove all the useless values first.
		That is, all those values that are <= 80. Since are not any such value, we remove nothing.
		
		span is 1 only.
		
		We also put the index of 80 in the stack as it might be a useful value for some future price.
		
		list = [100,80]
		stack = [0,1]
		
		Next, we have 60. Again, the same case. Its span is also 1 only so return 1.
		
		list = [100,80,60]
		stack = [0,1,2]
		
		Next, we have 70.
		
		We see that top of stack has index 2. This index has value "60" in the list so it is <= 70.
		
		Hence, we remove this one as it is useless now that we have 70, a bigger price. 
		
		Next, we get to index 1. At this index, we have "80". Since 80 is not <= 70, we stop.
		
		Hence, the index at which we stopped as 2. Which means, all the values after index 2 are <= 70.
		
		span = 2
		
		list = [100,80,60,70]
		stack = [0,1,3] ---> Since we popped 2 already
		
		
		Next, we have 60 again. Since top of stack has index = 3 and at index = 3 we have 70, no removal happens.
		Span = 1
		
		list = [100,80,60,70,60]
		stack = [0,1,3,4]
		
		Next, we have "75". Here, as we can see, both the index "3" and index "4" will get removed from stack.
		
		And the index on top will be "1" after all the removals. Which means, all values after index 1 are <= 75.
		
		So, span = how many values are there after index 1 (including itself) => 4
		
		list = [100,80,60,70,60,75]
		stack = [0,1,5]
		
		Finally, we have "85". Here, we will remove the indices "1" and "5" form stack.
		
		So stack will be like [0] and since the top index is 0, it means all values after index 0 are <= 85
		
		So span => 6 since there are 6 values after index 0 (including 85)
		

And that's how we will use a stack to optimize our code.


## **APPROACH #3 - USE A STACK ONLY (NO EXTRA LIST)**

There is one more way to use a Stack to solve this problem.

We can turn the useless values into useful values by also keeping track of what was the span of them.

In that way, we will need to extra list to keep all the prices and only one stack will be used.

Let's take the same example as before.

		Suppose, first price is 100. Since it is the first price, its span is simply 1 since stack is empty.
		
		This time, we will keep a pair in the stack -> (price, span)
		So, for 100, our stack looks like - [(100,1)]
		
		Next, we have 80.
		Our stack is not empty, so we want to remove all the useless values first.
		But as we remove those values, we will also use their "span" value to add to our current day's span.
		
		Here, there is no useless value at all so, for 80, the span remains 1 only.
		
		stack = [(100,1), (80,1)]
		
		Next, we have 60. Again, the same case. Its span is also 1 only so return 1.
		
		stack = [(100,1), (80,1), (60,1)]
		
		Next, we have 70.
		
		Now we see that we have one useless value "60". And since its span is 1, we can add this span to the span of 70.
		
		Since it makes sense that is 60 is <= 70, then all the values on which 60 spanned over are also <= 70.
		
		span = 2.
		
		Now the top of stack has value 80 but since it is greater than 70, we stop. 
		
		stack = [(100,1), (80,1), (70, 2)]

		Next, we have 60 again. Since top of stack has 70 and 70 > 60, no removal happes.
		Span = 1
		
		stack = [(100,1), (80,1), (70, 2), (60,1)]
		
		Next, we have "75". Here, as we can see the top two values are useless values.
		So, as we remove them, we will also take their span values and add to the current day's span.
		
		Span = Itself + 2 + 1 => 4
		
		stack = [(100,1), (80,1), (75, 4)]
		
		Finally, we have "85"
		
		Since both 75 and 80 are <=  85, both are removed from stack and also their spans are added to current day's span.
		
		Span = Itself + 4 + 1 => 6
		
		stack = [(100,1), (85,6)]
		
And in this way, we did not have to use a separate list to keep track of prices.