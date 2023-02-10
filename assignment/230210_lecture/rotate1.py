

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_t = list(map(list(map(list, zip(*arr)))))
    a1 = [[0] * N for _ in range(N)]
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]

    # [2] 전치 배열과 읽는 방향에 따른 처리
    print(f'#{test_case}')
    for i in range(N):
        print(f'{"".join(arr_t[i][::-1])} {"".join(arr_t[N-1-i])}')
