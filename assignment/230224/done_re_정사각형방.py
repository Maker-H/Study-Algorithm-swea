def dfs(start_f, start_s):
    global max_cnt
    global cnt

    for k in range(4):
        nf = start_f + dx[k]
        ns = start_s + dy[k]

        if 0 <= nf < N and 0 <= ns < N:
            if rooms[nf][ns] == rooms[start_f][start_s] + 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
                dfs(nf, ns)
    else:
        return



T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    rooms = []
    for _ in range(N):
        rooms.append(list(map(int, input().split())))
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    
    ans = []
    total_max = 0
    total_max_room = 0
    for f in range(N):
        for s in range(N):
            max_cnt = 1
            cnt = 1
            dfs(f, s)
            if max_cnt > total_max:
                total_max = max_cnt
                total_max_room = rooms[f][s]
            if max_cnt == total_max:
                if rooms[f][s] < total_max_room:
                    total_max_room = rooms[f][s]



    print(f'#{test_case} {total_max_room} {total_max}')

