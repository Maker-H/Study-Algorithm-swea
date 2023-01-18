# The value of acceleration is additionally given [acceleration (1) or deceleration (2)] 
# Write a program that calculates the distance traveled for N seconds when all N commands given as input are executed
# Restriction : If the speed to decelerate is greater than the current speed, the speed becomes 0 m/s.

T = int(input())
SECOND = 1
for test_case in range(1, T+1):
    total_distance = 0
    # Get the numbur of command line
    command_line_num = int(input())
    
    acceleration = 0
    # Get each command line
    for time in range(1, command_line_num + 1):
        # Set speend and command
        tmp = list(map(int, input().split()))
        command = tmp[0]
        if command != 0:
            speed = tmp[1]

        # Set acceleration
        if command == 0:
            pass
        elif command == 1:
            acceleration += speed
        elif command == 2:
            # Restriction
            if speed > acceleration:
                speed = 0
            elif acceleration >= speed:
                acceleration -= speed
        # Get distance
        total_distance += acceleration * SECOND



    # Print each test cases total distance
    print(f'#{test_case} {total_distance}')


    