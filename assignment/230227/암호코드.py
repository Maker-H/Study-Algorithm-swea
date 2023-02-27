pwd = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    i = 56
    codes = []
    for _ in range(N):
        tmp = list(input().rstrip('0'))
        if '1' in tmp:
            codes = tmp[(len(tmp)-56):(len(tmp))]


    start = 0
    end = 6
    odd = 0
    even = 0
    for code in range(8):
        tmp = codes[start + (code * 7): end + (code * 7) + 1]
        tmp = "".join(tmp)
        if code % 2 == 0:
            # print(tmp, pwd[tmp])
            odd += pwd[tmp]
        elif code % 2 == 1:
            # print(tmp, pwd[tmp])
            even += pwd[tmp]

    if (odd * 3 + even) % 10 == 0:
        print(f'#{test_case} {odd + even}')
    else:
        print(f'#{test_case} 0')




