from collections import deque

pipe_path = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
# 현재의 길이 다음 길과 연결되어야 한다
connect = {0: 1, 1: 0, 2: 3, 3: 2}
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(start_f, start_s, L):
    cnt = 1
    Q = deque()
    visited = [[0] * M for _ in range(N)]

    Q.append([start_f, start_s])
    visited[start_f][start_s] = 1

    while Q:
        f, s = Q.popleft()

        if visited[f][s] == L:
            return cnt

        for k in pipe_path[pipes[f][s]]:
            nf = f + dx[k]
            ns = s + dy[k]
            if 0 <= nf < N and 0 <= ns < M and visited[nf][ns] == 0 and connect[k] in pipe_path[pipes[nf][ns]]:
                cnt += 1
                visited[nf][ns] = visited[f][s] + 1
                Q.append([nf, ns])
    return cnt

T = int(input())

for test_case in range(1, T+1):
    N, M, start_f, start_s, L = map(int, input().split())
    pipes = []
    for _ in range(N):
        pipes.append(list(map(int, input().split())))


    cnt = bfs(start_f, start_s, L)
    print(f'#{test_case} {cnt}')