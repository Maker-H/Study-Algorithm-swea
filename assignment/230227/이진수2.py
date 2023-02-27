T = int(input())

for test_case in range(1, T+1):
    N = float(input())

    ans = ''

    cnt = 0
    while N != 0:
        cnt += 1

        if cnt == 13:
            break

        N = N * 2
        if int(N) == 1:
            ans += '1'
            N -= 1
        elif int(N) == 0:
            ans += '0'

    if cnt == 13:
        print(f'#{test_case} overflow')
    else:
        print(f'#{test_case} {ans}')