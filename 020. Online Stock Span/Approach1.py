class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        
        n = len(self.prices)
        
        span = 1
        
        for i in range(n - 1, -1 , -1):
            if self.prices[i] <= price: span += 1
            else: break
                
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

