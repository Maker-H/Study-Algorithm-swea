# N=2^a x 3^b x 5^c x 7^d x 11^e
# Get a, b, c, d, e

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    # Find if N is divided by 2
    a_count = 0
    num = 2
    while True:
        if N % num == 0:
            N = N // num
            a_count += 1
        elif N % num != 0:
            break
    
    # Find if N is divided by 3
    b_count = 0
    num = 3
    while True:
        if N % num == 0:
            N = N // num
            b_count += 1
        elif N % num != 0:
            break
    
    # Find if N is divided by 5
    c_count = 0
    num = 5
    while True:
        if N % num == 0:
            N = N // num
            c_count += 1
        elif N % num != 0:
            break
    
    # Find if N is divided by 7
    d_count = 0
    num = 7
    while True:
        if N % num == 0:
            N = N // num
            d_count += 1
        elif N % num != 0:
            break
    
    # Find if N is divided by 11
    e_count = 0
    num = 11
    while True:
        if N % num == 0:
            N = N // num
            e_count += 1
        elif N % num != 0:
            break

    print(f'#{test_case} {a_count} {b_count} {c_count} {d_count} {e_count}')
