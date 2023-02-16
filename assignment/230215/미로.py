def dfs(f, s):
    global flag

    if maze[f][s] == 3:
        flag = 1
        return

    maze[f][s] = 9

    df = [-1, 0, 0, 1]
    ds = [0, 1, -1, 0]

    for idx in range(4):
        nf = f + df[idx]
        ns = s + ds[idx]

        if 0 <= nf < maze_size and 0 <= ns < maze_size:
            if maze[nf][ns] == 0 or maze[nf][ns] == 3:
                dfs(nf, ns)



T = int(input())

for tc in range(1, T+1):
    maze_size = int(input())
    maze = []
    flag = 0

    for _ in range(maze_size):
        maze.append(list(map(int, input())))

    sf = ss = -1
    for f in range(maze_size):
        for s in range(maze_size):
            if maze[f][s] == 2:
                sf = f
                ss = s

    dfs(sf, ss)

    print(f'#{tc} {flag}')