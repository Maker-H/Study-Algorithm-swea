def bfs(v, N):
    visited = [0] * (N+1)# visited 생성
    q = [v]        # 큐 생성
            # 시작점 인큐
    visited[v] = 1        # 시작점 인큐 표시
    while q: # 큐가 비어있지 않으면
        t = q.pop(0) # 디큐
        print(t, end = ' ')
        for v in adjL[t]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = visited[t] + 1





V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjL= [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1, V) # 시작 정점점