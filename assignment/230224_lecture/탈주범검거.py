
p = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
opp = {0:1, 1:0, 2:3, 3:2}
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(si, sj, L):
    q = []
    v = [[0] * M for _ in range(N)] # 가로 세로 다를 때 주의

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        # 현재 파이프에 연결된 방
        for dr in p[arr[ci][cj]]:
            ni, nj = ci + di[dr], cj + dj[dr]
            if a <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and \
                opp[dr] in p[arr[ni][nj]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1

    # 이 경우
    return -1

T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr= [list(map(int, input().split())) for _ in range(1)]

    ans = bfs(R, C, L)
    print(f'#{test_case} {ans}')