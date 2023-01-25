# Can freely move BIG or SMALL list to make the numbers face each other.
# It should not go beyond either end of the longer side.
# Print maximum when multiply opposite numbers and add them all up.

T = int(input())

for test_case in range(1, T+1):
    N, M = tuple(map(int, input().split()))

    if N > M:
        BIG = list(map(int, input().split()))
        SMALL = list(map(int, input().split()))
    elif N < M:
        SMALL = list(map(int, input().split()))
        BIG = list(map(int, input().split()))
    
    sums = []
    b_idx = 0 
    s_idx = 0

    isContinue = True
    while isContinue:
        sum = 0
        tmp_b_idx = b_idx 
        tmp_s_idx = s_idx

        for repeat in range(len(SMALL)):
            sum += (BIG[tmp_b_idx] * SMALL[tmp_s_idx])
            tmp_b_idx += 1
            tmp_s_idx += 1
            # If end of index break
            if tmp_b_idx == len(BIG) and tmp_s_idx == len(SMALL):
                isContinue = False
                break
    
        sums.append(sum)
        # If I reach the end and do b_idx += 1 operaition, it goes out of index range
        if isContinue:
            b_idx += 1
        
    print(f'#{test_case} {max(sums)}')






