def clumsy(n: int) -> int:
        # For values till 4
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 6
        if n == 4: return 7
        
        # For values above 4
        remainder = n % 4
        
        # If remainder is 0. e.g. values like -> 8, 12, 16, 20
        if remainder == 0: return n + 1
        
        # If remainder is 3. e.g. values like -> 7, 11, 15, 19
        if remainder == 3: return n - 1
        
        # For all other values such as -> 5,6,9,10
        return n + 2


n = 10
print("Clumsy Factorial is -> ", clumsy(n))