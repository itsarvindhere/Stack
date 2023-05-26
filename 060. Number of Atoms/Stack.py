def countOfAtoms(formula: str) -> str:
        # Length of the formula
        n = len(formula)
        
        # A dictionary to keep track of the count of each atom
        freq = {}
        
        # Since in a formula, we can have parenthesis
        # We can make use of stack to correctly evaluate a formula inside a parenthesis
        stack = []
        
        # Loop over the formula
        i = 0
        while i < n:
            
            # If it is an uppercase character
            if formula[i].isupper():
                element = [formula[i]]
                
                # This marks the beginning of an element's symbol
                # So, we will first figure out the full symbol of this element
                # before we push it to the stack
                i += 1
            
                while i < n and formula[i].islower():
                    element.append(formula[i])
                    i += 1
                    
                # At this point, we have the element's full symbol
                stack.append("".join(element))
                
                # If there is a number after it, then continue
                # But if not, we can put "1" 
                if i < n and not formula[i].isnumeric(): stack.append("1")
                
            # If it is a closing parenthesis
            elif formula[i] == ")":
                i += 1
                # Now, we want to move backwards to evaluate the formula inside the parenthesis
                # But we also need to think of the fact that there might be a number after this closing bracket
                number = 0
                while i < n and formula[i].isnumeric():
                    number = (number * 10) + int(formula[i])
                    i += 1
                    
                if number == 0: number = 1
                    
                # And now that we have the number we go backwards
                # Till we reach the opening bracket
                evaluatedFormula = []
                
                while stack and stack[-1] != "(":
                    # If it is a number
                    if stack[-1].isnumeric():
                        evaluatedFormula.append(str(int(stack.pop()) * number))
                    else:
                        evaluatedFormula.append(stack.pop())
                        
                # At this point, we will point to the opening bracket
                stack.pop()
                
                # And we can push back the evaluated formula in stack
                for element in reversed(evaluatedFormula): stack.append(element)
                
            # If it is a digit or an opening bracket
            else: 
                # IF there is a digit in stack and current character is also a digit
                # Then instead of adding it as a new value in stack
                # Concatenate current digit with previous digit
                if stack and stack[-1].isnumeric() and formula[i].isnumeric(): stack[-1] += formula[i]
                else: stack.append(formula[i])
                i += 1
        
        # For the last character
        # For example, for formulas where last character does not have any number after it
        # We can add "1" for it
        if not stack[-1].isnumeric(): stack.append("1")
            
        # Now it's time to fill the dictionary with count
        while stack:
            # Number
            count = int(stack.pop())
            
            # Element
            element = stack.pop()
            freq[element] = freq.get(element,0) + count
            
        # Final output
        output = []
        
        for key in sorted(list(freq.keys())):
            output.append(key)
            
            # If count is 1, no need to put the count in output
            if freq[key] > 1: output.append(str(freq[key]))
        
        return "".join(output)



formula = "Mg(OH)2"

print("Output ->", countOfAtoms(formula))