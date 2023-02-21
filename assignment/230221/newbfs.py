from collections import deque

def bfs(v):
    global cnt

    # enQ +visitied
    Q = deque()
    Q.append(v)
    visited[v] = 1

    # Q가 비어있지 않은 동안
    while Q:
        # v = deQ
        v = Q.popleft()
        # 하고싶은 일 하기
        print(v, end=' ')
        cnt += 1

        # v에 인접한 정점 중에서 방문안한 정점이면
        for w in adj[v]:

            if not visited[w]:
                # enQ + visited 설정
                Q.append(w)
                visited[w] = visited[v] + 1



V, E = map(int, input().split())
tmp = list(map(int, input().split()))
adj = {i:[] for i in range(1, V+1)}
visited = [0] * (V+1)

for i in range(E):
    s, e = tmp[2*i], tmp[2*i+1]
    adj[e].append(s)
    adj[s].append(e)
print(adj)
cnt = 0

bfs(0)
print(f'\ncnt={cnt}, visited={visited}')