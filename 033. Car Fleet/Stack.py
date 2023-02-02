def carFleet(target: int, position, speed):
    # Length of the list(s)
    n = len(position)
        
    # Convert each value in a pair - (position, speed)
    time = [[position[i], speed[i]] for i in range(n) ]
        
    # Sort by the position
    time.sort()
        
    # Now, convert each position value into a time value
    # That is, what is the time required to reach target
    # Time = distance/speed
    # Here, distance = target-position
    for i in range(n): time[i] = (target - time[i][0]) / time[i][1]
            
    # Since it is a one-lane road, it means, if a car is going fast
    # And want to reach the target without having to slow down,
    # the cars next to it should move at same or greater speed
    # Otherwise, it will have to slow down and match the slower car's speed
    # And that will result in a fleet
    # And that fleet will take same time as the slower car takes
    fleets = []

    # We will loop in opposite direction, that is, right to left
    for i in range(n - 1, -1, -1):
        # If the car on right takes less than to reach destination than current car
        # It means, there won't be any need to slow down
        # Hence, this current car is a fleet in its own
        if not fleets or (fleets and fleets[-1] < time[i]): fleets.append(time[i])

    return len(fleets)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print("Fleet Count -> ", carFleet(target, position, speed))