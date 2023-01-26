from collections import deque
def decodeString(s):
        
    # Length of Given string
    n = len(s)
        
    # Stack
    stack = []
        
    i = 0
    while i < n:
            
        # Until we do not encounter a closing bracket
        # Keep pushing the characters to the stack
        while i < n and s[i] != "]":
            stack.append(s[i])
            i += 1
            
        # At this point, i may point to a closing bracket
        # We want the whole word in between this closing bracket and its corresponding opening bracket
        word = deque([])
        while stack and stack[-1] != "[": word.appendleft(stack.pop())
            
        # If stack is not empty, it means we have an opening bracket so remove it
        if stack: stack.pop()
            
        # Now, we want to find what is the value by which we have to repeat this word
        times = deque([])
            
        # This time, we will keep gathering the characters if they are numeric
        while stack and stack[-1].isnumeric(): times.appendleft(stack.pop())
            
        # And now, get the number
        if times: times = int("".join(times))
        else: times = 1
            
        # Now simply push back the word created
        stack.append("".join(word) * times)
            
        i += 1
        
    return "".join(stack)


s = "2[abc]3[cd]ef"

print("Output -> ", decodeString(s))