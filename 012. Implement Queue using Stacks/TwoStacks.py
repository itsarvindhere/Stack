class MyQueue:

    def __init__(self):
        self.stack1, self.stack2 = [],[]
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:          
        self.fillSecondStack()
                
        # Pop the top and return
        return self.stack2.pop()

    def peek(self) -> int:
        self.fillSecondStack()
        
        # Return the top of stack2 (Do not pop it)
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
    
    def fillSecondStack(self) -> None:
         # If the second stack is empty
        # Then fill it with the elements of stack1
        # Such that at the end, the elements pushed first is at the top of stack2
        if not self.stack2:
            while self.stack1: 
                self.stack2.append(self.stack1.pop())


queue = MyQueue()

print(queue.push(1))
print(queue.push(2))
print(queue.peek())
print(queue.pop())
print(queue.empty())