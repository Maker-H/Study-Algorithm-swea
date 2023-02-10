

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a1 = [[0] * N for _ in range(N)]
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]

    print(f'#{test_case}')
    for a, b, c in zip(a1, a2, a3):
        print(f'{"".join(a1)} {"".join(a2)} {"".join(a3)}')