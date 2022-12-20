def calPoints(operations):
        
    record = []
        
    for operation in operations:
            
        # Record a new score that is the sum of the previous two scores
        if operation == "+": record.append(record[-1] + record[-2])
            
        # Record a new score that is the double of the previous score
        elif operation == "D": record.append(2 * record[-1])
            
        # Invalidate the previous score, removing it from the record
        elif operation == "C": record.pop()
            
        # Record this new score
        else: record.append(int(operation))
        
    # Finally, return the sum
    return sum(record)

ops = ["5","2","C","D","+"]
print("Final Score -> ", calPoints(ops))