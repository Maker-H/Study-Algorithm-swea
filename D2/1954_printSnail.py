# Get current location by tuple and set goal by R
def goRight(snail, current, R):
    l, r = current

    count = snail[l][r]
    for move in range(R):
        r += 1
        count += 1
        snail[l][r] = count

    return (l, r)
        

def goLeft(snail, current, R):
    l, r = current

    count = snail[l][r]
    for move in range(R):
        r -= 1
        count += 1
        snail[l][r] = count

    return (l, r)
    
def goUp(snail, current, R):
    l, r = current

    count = snail[l][r]
    for move in range(R):
        l -= 1
        count += 1
        snail[l][r] = count

    return (l, r) 

def goDown(snail, current, R):
    l, r = current

    count = snail[l][r]
    for move in range(R):
        l += 1
        count += 1
        snail[l][r] = count

    return (l, r)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    snail_N = N
    snail = [[0 for j in range(N)] for i in range(N)]

    first_location = (0, 0)

    snail_N -= 1
    location = goRight(snail, first_location, snail_N)
    for i in range(snail_N // 2):
        if snail_N == 0 :
            break
        locaton = goDown(snail, location, 2)
        locaion = goLeft(snail, location, 2)
        snail_N -= 1
        
        if snail_N == 0 :
            break
        locaton = goUp(snail, location, 1)
        locaion = goRight(snail, location, 1)
        snail_N -= 1

    print(snail)
    # # N = 4일때
    # location = goRight(snail, first_location, 3)
    # locaiton = goDown(location, 3)
    # location = goLeft(location, 3)
    # locaiton = goUp(location, 2)
    # location = goRight(location,2)
    # locaiton = goDown(location, 1)
    # location = goLeft(location, 1)
    
    
    #howEnd??

