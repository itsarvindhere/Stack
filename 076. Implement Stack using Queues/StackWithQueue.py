from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        # In a queue, we push elements from rear end
        # So, we can append elements to rear
        self.queue.append(x)
        
        # But, to pop elements or to get the element on top
        # we have to get that from front of queue
        # So, we have to rotate the queue after each push
        # Such that the element we pushed to the back is now at the front
        for i in range(len(self.queue) - 1): self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        
        # When we want to pop, we want to pop from the front
        # So, the last element pushed should be the one to be removed now
        # But, we pushed the last element from rear side
        # So, to remove from front, we have to rotate the queue
        return self.queue.popleft()

    def top(self) -> int:
        
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    

