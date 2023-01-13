class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # If there are prices in the stack
        # We will remove all the useless prices from the stack first
        # We are looking for the first price on left side that is greater than "price"
        # So, all the uselsss prices are the ones that are <= price
        
        while self.stack and self.prices[self.stack[-1]] <= price: self.stack.pop()
        
        # At this point, if the stack still has some values, it means, the top of stack has index of nearest greater price on left
        # So, span is simply the count of prices between the index on top of stack (excluding) and current day (including)
        if self.stack: span = len(self.prices) - self.stack[-1]
        
        # Otherwise, if the stack is empty then
        # either there was no element in the beginning or the current day's price is greater than all previous prices
        else: span += len(self.prices)
        
        # Push the index of the current day's price in the stack
        self.stack.append(len(self.prices))
        
        # Put the current day's price in the list
        self.prices.append(price)

        return span


obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))