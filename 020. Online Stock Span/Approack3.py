class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # If there are prices in the stack
        # Then just keep looking at the price on top and if it is <= current day's price
        # Then we can take its span and add it to current day's price
        # Because if it is <= current day's price, ofcourse all the values it spans over will also be <= current day's price
        while self.stack and self.stack[-1][0] <= price: span += self.stack.pop()[1]

        # Push the current day's price and its span in the stack
        # As it might be useful for calculating any future price's span
        self.stack.append((price, span))

        return span

obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))