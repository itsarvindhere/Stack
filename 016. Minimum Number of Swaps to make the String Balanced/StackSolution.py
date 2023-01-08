from math import ceil
def minSwaps(s):
        
    openBrackets = []
    closeBrackets = []
        
    for c in s:
            
        # If we encounter a closing bracket
        if c == "]":
            # See whether stack has an opening bracket to match with
            if openBrackets: openBrackets.pop()
            else: closeBrackets.append(c)
            
        # If we encounter an opening bracket
        else: openBrackets.append(c)
        
    return ceil(len(closeBrackets) / 2)

s = "]]][[["
print("Minimum Swaps Required -> ", minSwaps(s))