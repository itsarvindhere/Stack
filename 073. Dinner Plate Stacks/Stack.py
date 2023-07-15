from heapq import heappop, heappush


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # A list to maintain the stacks
        self.stacks = []
        
        # We need a way to keep track of which is the leftmost index of a stack 
        # that has less than "capacity" elements
        # We may think of using a list only but think about what if we pop from any index
        # Now, the stack at that index may or may not be the leftmost that we have to push into
        # So we again have to reorder our whole list so that the leftmost index is always on the top
        # That is not efficient
        
        # What if there is a data structure that automatically takes care of this reordering?
        # So that as we push an index to it, it will automatically order all indices so that the top is always the smallest
        # Well, that's something a minHeap can do
        self.minHeap = []
        
        # Set to keep track of what all indices are already in the heap
        # So that we are not pushing them again
        self.indicesInHeap = set()


    def push(self, val: int) -> None:
        
        # If the leftmost index in minHeap is invalid (which is also the smallest value in this minHeap)
        # Then all indices are useless so reset the minHeap
        if self.minHeap and self.minHeap[0] > len(self.stacks) - 1: self.minHeap = []
        
        # If there are no stacks yet (Initially)
        # OR there is no existing stack in which we can push
        # In both cases, we will have to add in a new stack to the list
        if not self.stacks or not self.minHeap:
            newStack = []
            newStack.append(val)
            self.stacks.append(newStack)
            
            # If stack size is already equal to capacity
            # Then next time we have to push, we have to push val in a whole new stack
            # Otherwise, we can put the index of current stack in the heap
            if len(newStack) < self.capacity: 
                heappush(self.minHeap, len(self.stacks) - 1)
                
                # Also add this index to the set
                # To keep track of indices that are already added in the minHeap
                self.indicesInHeap.add(len(self.stacks) - 1)
                
        # Otherwise
        else:
            # Get the index of leftmost stack with size < capactiy
            leftmostIdx = self.minHeap[0]
            
            # Push the value in that stack
            self.stacks[leftmostIdx].append(val)
            
            # If the size of that stack is now equal to capacity, it is now full
            # So we can pop it from the heap
            # And as we remove it from the heap, we also remove it from the set
            if len(self.stacks[leftmostIdx]) == self.capacity: self.indicesInHeap.remove(heappop(self.minHeap))
        
    def pop(self) -> int:
        
        # If there are no stacks, return -1
        # Also, if the rightmost stack is empty, return -1
        if not (self.stacks and self.stacks[-1]): return -1
        
        # Otherwise, pop from the rightmost non-empty stack
        poppedVal = self.stacks[-1].pop()
        
        # Remove all the empty stacks at the end of the list of stacks
        while self.stacks and not self.stacks[-1]: self.stacks.pop()
            
        # At this point, if we have a stack at the end that has less elements than its capacity
        # Then, we can put its indexin the heap if that index is not already present
        if self.stacks and len(self.stacks[-1]) < self.capacity:
            if (len(self.stacks) - 1) not in self.indicesInHeap:
                heappush(self.minHeap, len(self.stacks) - 1)
                self.indicesInHeap.add(len(self.stacks) - 1)
            
        # Return the popped value
        return poppedVal
        

    def popAtStack(self, index: int) -> int:
        
        # If the index is not valid for the list of stacks
        # Or, if at the "index", the stack is already empty
        # Return -1
        if index >= len(self.stacks) or not self.stacks[index]: return -1
        
        # Pop from the stack at "index"
        poppedVal = self.stacks[index].pop()
        
        # Remove the rightmost stack is it is empty
        # Because chances are that "index" that is passed to this method
        # Is the last index of the list of stacks
        if self.stacks and not self.stacks[-1]: self.stacks.pop()
            
        # Otherwise, this stack now has less elements than its capacity
        # So we can put its index in the heap as well
        # But only if its index is not already present in the heap
        elif index not in self.indicesInHeap: 
            heappush(self.minHeap, index)
            self.indicesInHeap.add(index)
        
        # Return the popped value
        return poppedVal
    

D = DinnerPlates(2)
print("Push Operation -> ", D.push(1))
print("Push Operation -> ", D.push(2))
print("Push Operation -> ", D.push(3))
print("Push Operation -> ", D.push(4))
print("Push Operation -> ", D.push(5))

print("Pop at Index Operation -> ", D.popAtStack(0))

print("Push Operation -> ", D.push(20))
print("Push Operation -> ", D.push(21))

print("Pop at Index Operation -> ", D.popAtStack(0))
print("Pop at Index Operation -> ", D.popAtStack(2))

print("Pop Operation -> ", D.pop())
print("Pop Operation -> ", D.pop())
print("Pop Operation -> ", D.pop())
print("Pop Operation -> ", D.pop())
print("Pop Operation -> ", D.pop())


