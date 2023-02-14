

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10
    a1 = 1

    for check in range(N):
        if check % 2 == 0:
            a1 = a1 * 2 - 1

        elif check % 2 == 1:
            a1 = a1 * 2 + 1

    print(f'#{tc} {a1}')
