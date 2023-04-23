from collections import defaultdict
class FreqStack:

    def __init__(self):
        # Dictionary to keep the frequency
        self.freq = {}
        
        # Dictionary to keep track of what elements have what frequency
        self.freqList = defaultdict(list)
        
        # What is the maximum frequency at any point
        self.maxFreq = 0

    def push(self, val: int) -> None:
        # Update the frequency
        self.freq[val] = self.freq.get(val, 0) + 1
        
        # Update the max frequency
        self.maxFreq = max(self.maxFreq, self.freq[val])
        
        # Update the list in frequency Map
        self.freqList[self.freq[val]].append(val)
        

    def pop(self) -> int:
        # Whatever is the maximum frequency at this point
        # Remove that particular element which has this frequency        
        # Note that we have a list maintained for each frequency
        # So, we know that the last element pushed will be the most recent
        # So that case is also covered
        removedVal = self.freqList[self.maxFreq].pop()
        
        # Only reduce the maxFreq if for current maxFreq, there are no elements left in freqList
        if not self.freqList[self.maxFreq]: self.maxFreq -= 1
                
        # Also reduce its frequency from the dicitonary
        self.freq[removedVal] -= 1
        
        # No need to keep it if frequency is already 0
        if self.freq[removedVal] == 0: self.freq.pop(removedVal)
        
        # Return the popped value
        return removedVal
    

freqStack = FreqStack();
freqStack.push(5); 
freqStack.push(7); 
freqStack.push(5); 
freqStack.push(7); 
freqStack.push(4); 
freqStack.push(5); 

print("Popped Element is -> ", freqStack.pop())
print("Popped Element is -> ", freqStack.pop())
print("Popped Element is -> ", freqStack.pop())
print("Popped Element is -> ", freqStack.pop())