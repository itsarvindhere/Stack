from math import ceil
def minSwaps(s):
        
    openBrackets = 0
    closeBrackets = 0
        
    for c in s:
            
        # If we encounter a closing bracket
        if c == "]":
            # See whether we have an opening bracket to match with
            if openBrackets != 0: openBrackets -= 1
            else: closeBrackets += 1
            
        # If we encounter an opening bracket
        else: openBrackets += 1
        
    return ceil(closeBrackets / 2)

s = "]]][[["
print("Minimum Swaps Required -> ", minSwaps(s))