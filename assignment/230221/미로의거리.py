def bfs(goal_f, goal_s, N):

    Q = []
    Q.append([goal_f, goal_s, 0])


    while Q:
        tmp = Q.pop(0)
        if arr[tmp[0]][tmp[1]] == 3:
            return tmp[2]

        arr[tmp[0]][tmp[1]] = 9

        for idx in range(4):
            nf = tmp[0] + df[idx]
            ns = tmp[1] + ds[idx]

            if 0 <= nf < N and 0 <= ns < N and arr[nf][ns] != 1 and arr[nf][ns] != 9:
                Q.append([nf, ns, tmp[2]+1])

    return 1



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    df = [-1, 0, 0, 1]
    ds = [0, 1, -1, 0]

    arr = []

    for _ in range(N):
        arr.append(list(map(int, list(input()))))

    flag = False
    goal_f = None
    goal_s = None

    for f in range(N):
        for s in range(N):
            if arr[f][s] == 2:
                goal_s = s
                goal_f = f
                flag = True
                break
        if flag:
            break

    cnt = bfs(goal_f, goal_s, N)

    print(f'#{test_case} {cnt-1}')