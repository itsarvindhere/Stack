class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        
    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize: return
        
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack: return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        # Since in python we can use a simple list to implement stack
        # SImply increment first k elements by val
        k = min(k, len(self.stack))

        for i in range(k): self.stack[i] += val

