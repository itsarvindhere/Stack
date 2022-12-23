from collections import Counter, deque
def countStudents(students, sandwiches):
        
        students = deque(students)
        
        # So that if we want to grab the top value, we can do sandwiches[-1]
        # And to remove, we can then simply use pop() which is O(1) operation for the last element of a list
        sandwiches.reverse()
        
        # To keep track of 1s and 0s in students list
        counter = Counter(students)
        
        while students and sandwiches:
            
            # If the preferences matches
            if students[0] == sandwiches[-1]: 
                # Reduce the count
                counter[students[0]] -= 1
                
                # Student takes the sandwich and leaves
                sandwiches.pop()
                students.popleft()
            else: 
                # If there are no students with preference same as frontSandwich
                # Then it means, we can break. Otherwise an endless loop will start
                if counter[sandwiches[-1]] == 0: break
                
                # Move the front student to the end of the queue
                students.append(students.popleft())

        return len(sandwiches)


    
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

print("Students unable to eat -> ", countStudents(students, sandwiches))