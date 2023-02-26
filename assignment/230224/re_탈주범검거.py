from collections import deque


def bfs(f, s, time):
    Q = deque()
    place = 1
    Q.append([f, s, 1])
    
    while Q:
        f, s, start_time = Q.popleft()
        
        if start_time == L:
            return place

        tmp = pipes[f][s]
        pipes[f][s] = 0
        for dx, dy in location.get(tmp):
            nf = f + dx
            ns = s + dy
            if 0 <= nf < N and 0 <= ns < M and pipes[nf][ns] != 0:
                Q.append([nf, ns, start_time + 1])
                place += 1


T =  int(input())
location = {1:[[1, 0], [-1, 0], [0, -1], [0, 1]] \
            ,2:[[1, 0], [-1, 0]] \
            ,3 : [[0, 1], [0, -1]] \
            , 4: [[-1, 0], [0, 1]] \
            , 5 : [[0, 1], [1, 0]] \
            , 6: [[0, -1], [1, 0]] \
            , 7:[[-1, 0], [0, -1]]}

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    pipes = []
    for _ in range(N):
        pipes.append(list(map(int, input().split())))
    
    print(f'#{test_case} {bfs(R, C, L)}')