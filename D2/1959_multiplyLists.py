
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
            print('#',repeat, 'sum', BIG[tmp_b_idx] * SMALL[tmp_s_idx], 'big', BIG[tmp_b_idx], 'small', SMALL[tmp_s_idx],'tmp_b', tmp_b_idx, 'tmp_S', tmp_s_idx)
            tmp_b_idx += 1
            tmp_s_idx += 1
            # TODO
            if tmp_b_idx == len(BIG)+1 and tmp_s_idx == len(SMALL) :
                isContinue = False
                break

        b_idx += 1
        sums.append(sum)
        
    print(f'#{test_case} {max(sums)}')






