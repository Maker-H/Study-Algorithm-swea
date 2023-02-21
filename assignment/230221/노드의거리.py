def bfs(S, E):
    Q = []
    Q.append(S)
    visited[S] = 0

    while Q:
        v = Q.pop(0)

        if v == E:
            return

        for w in tree[v]:
            if visited[w] == -1:
                Q.append(w)
                visited[w] = visited[v] + 1



T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())

    tree = {node:[] for node in range(1, V+1)}
    visited = [-1] * (V + 1)

    for _ in range(E):
        n1, n2 = map(int, input().split())
        tree[n1] += [n2]
        tree[n2] += [n1]


    S, E =  map(int, input().split())

    bfs(S, E)
    if visited[E] == -1:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {visited[E]}')
