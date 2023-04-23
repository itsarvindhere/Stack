class FreqStack:

    def __init__(self):
        # Dictionary to keep track of frequency of each element
        self.freq = {}
        
        # What is the maximum frequency
        self.maxFreq = 0
        
        # Stack
        self.stack = []

    def push(self, val: int) -> None:
        # Update the frequency
        self.freq[val] = self.freq.get(val, 0) + 1
        
        # Update the max frequency as well
        self.maxFreq = max(self.maxFreq, self.freq[val])
        
        # Push to stack - (value, flag to indicate if we have already popped this value)
        self.stack.append([val,False])

    def pop(self) -> int:
        # We want to pop the element with the maximum frequency
        valuePopped = self.stack[-1][0]
        
        # Length of the stack
        n = len(self.stack)
        
        for i in range(n - 1, -1, -1):
            # If this value has already been popped before, skip
            if self.stack[i][1]: continue
            
            # If this value has the maximum frequency
            if self.freq[self.stack[i][0]] == self.maxFreq: 
                valuePopped = self.stack[i][0]
                self.freq[self.stack[i][0]] -= 1
                
                # Update the flag to indicate that this value has been popped
                self.stack[i][1] = True
                
                break
        
        # Update the maxFreq
        self.maxFreq = max(self.freq.values())
        
        return valuePopped
    

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