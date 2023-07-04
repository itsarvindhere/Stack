def isValid(code: str) -> bool:
        # Replace the <![CDATA[ with something that won't appear in normal text
        # So, let's replace it with a "?"
        # Just to avoid some extra lines of code :D
        code = code.replace("<![CDATA[", "?")
        
        # If the first tag is CDATA that's not valid at all
        if code[0] == "?": return False
        
        # Length of the input string
        n = len(code)
        
        # Stack to keep track of opening tags
        # So that when a closing tag is encountered, we can check if it is valid
        stack = []
        
        # Loop over the Input String
        i = 0
        while i < n:
            
            # If it is a "<"
            # Then all characters until the next ">" will be part of the TAG_NAME
            if code[i] == "<":
                
                # To check if it is a closing tag
                isClosingTag = False
                
                # We will keep the tagName in a list
                # So that we can later convert it to a string
                # It is an efficient approach than using an empty string and then concatenate to that
                tagName = []
                
                # To skip including the "<" when we construct the tag name
                i += 1
                
                # It is also possible that this is a closing tag so it will start with "</"
                if i < n and code[i] == "/":
                    isClosingTag = True
                    i += 1
                
                # Now we get the characters in our Tag Name
                while i < n and code[i] != ">":
                    tagName.append(code[i])
                    i += 1
                    
                # If tagname has length less than 1 or more than 9, it is not valid
                if len(tagName) < 1 or len(tagName) > 9: return False
                
                # Conver the tagname from list to the string
                tagName = "".join(tagName)
                
                # It is a valid TAG_NAME only if all characters are uppercase
                if tagName.isalpha() and tagName.isupper():
                    
                    # If this is a closing tag, then it should have a respective opening tag on top of stack
                    if isClosingTag: 
                        # If the tag on top of stack is same, it is a valid pair
                        if stack and stack[-1] == tagName: 
                            stack.pop()
                            
                            # But, if we are not at the last tag in the input string and stack is already empty
                            # Then this is not a valid string
                            # Consider test cases such as "<A></A><B></B>"
                            # Basically, we want that there is one parent tag that encloses everything
                            # Just like how we have the <html> tag
                            if i != n - 1 and not stack: return False
                            
                        # Otherwise, this is an invalid pairing
                        else: return False
                        
                    # If this is an opening tag, just put it in the stack
                    # Along with the index at which tagName ends
                    else: stack.append(tagName)
                    
                # Otherwise, we can return False straight away since tag name is invalid
                else: return False
            
            # If it is a "?" that indices beginning of a "CDATA" tag
            elif code[i] == "?":
                
                # Move past the opening CDATA tag
                i += 1
                
                # Go till the end of this CDATA tag
                # Since there can be anything inside CDATA that parser needs not to check if valid or invalid
                while (i + 2 < n) and not (code[i] == "]" and code[i + 1] == "]" and code[i + 2] == ">"): i += 1
                                    
                # At this point, we should now have a "]]>" that indicates the closing of this CDATA tag
                if i + 2 < n and code[i] == "]" and code[i + 1] == "]" and code[i + 2] == ">": i += 3   
                    
            # For everything else
            else: 
                
                # If stack is empty then this is not a valid case"
                # Take scenarios when there are no tags around content e.g. "1234"
                if i != n - 1 and not stack: return False
                
                i += 1
                
        # Finally, after all the operations, the stack should be empty for a valid input
        return not stack


code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

print('Is Valid? -> ', isValid(code))