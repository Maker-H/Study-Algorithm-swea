
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    killer = []

    for _ in range(N):
        killer.append(list(map(int, input().split())))

    cross_dx = [0, 0, 1, -1]
    cross_dy = [1, -1, 0, 0]

    dg_dx = [1, 1, -1, -1]
    dg_dy = [-1, 1, 1, -1]
    ans = []

    for f in range(N):
        for s in range(N):
            cross_sum = killer[f][s]
            dg_sum = killer[f][s]
            for k in range(4):
                for go in range(1, M):
                    cross_nf = f + cross_dx[k] * go
                    cross_ns = s + cross_dy[k] * go
                    dg_nf = f + dg_dx[k] * go
                    dg_ns = s + dg_dy[k] * go

                    if 0 <= cross_nf < N and 0 <= cross_ns < N:
                        cross_sum += killer[cross_nf][cross_ns]
                    if 0 <= dg_nf < N and 0 <= dg_ns < N:
                        dg_sum += killer[dg_nf][dg_ns]
            ans.append(cross_sum)
            ans.append(dg_sum)


    print(f'#{test_case} {max(ans)}')