# The numbers from 1 to N*N are arranged clockwise.
# Take an integer N as input and print a snail of size N.


# Get current location by tuple and set goal by G
def goRight(snail, current, G):
    l, r = current

    count = snail[l][r]
    for move in range(G):
        r += 1
        count += 1
        snail[l][r] = count

    return (l, r)
        

def goLeft(snail, current, G):
    l, r = current

    count = snail[l][r]
    for move in range(G):
        r -= 1
        count += 1
        snail[l][r] = count

    return (l, r)
    
def goUp(snail, current, G):
    l, r = current

    count = snail[l][r]
    for move in range(G):
        l -= 1
        count += 1
        snail[l][r] = count

    return (l, r) 

def goDown(snail, current, G):
    l, r = current

    count = snail[l][r]
    for move in range(G):
        l += 1
        count += 1
        snail[l][r] = count

    return (l, r)

def my_print(test_case, snail):
    print(f'#{test_case}')
    for oneline in snail:
        tmp = " ".join(list(map(str, oneline)))
        print(tmp)
            
# -------------------------------------------------------------

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    snail_N = N

    # Initialize snail list
    snail = [[0 for j in range(N)] for i in range(N)]
    snail[0][0] = 1
    first_location = (0, 0)

    # Have to move Right by 'arraySize -1'
    snail_N -= 1

    # Have to move R first and loop by DLUR 
    location = goRight(snail, first_location, snail_N)
    while True:
        if snail_N == 0 :
            break
        location = goDown(snail, location, snail_N)
        location = goLeft(snail, location, snail_N)
        snail_N -= 1
        
        if snail_N == 0 :
            break
        location = goUp(snail, location, snail_N)
        location = goRight(snail, location, snail_N)
        snail_N -= 1

    my_print(test_case, snail)
    
