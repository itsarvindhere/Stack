def calPoints(operations):
        
    record = []
        
    # Output to return
    finalSum = 0
        
    for operation in operations:
            
        # Record a new score that is the sum of the previous two scores
        if operation == "+": 
            s = record[-1] + record[-2]
            finalSum += s
            record.append(s)
            
        # Record a new score that is the double of the previous score
        elif operation == "D":
            double = 2 * record[-1]
            finalSum += double
            record.append(double)
            
        # Invalidate the previous score, removing it from the record
        elif operation == "C":
            finalSum -= record[-1]
            record.pop()
        # Record this new score
        else: 
            x = int(operation)
            finalSum += x
            record.append(x)
        
    # Finally, return the sum
    return finalSum

ops = ["5","2","C","D","+"]
print("Final Score -> ", calPoints(ops))