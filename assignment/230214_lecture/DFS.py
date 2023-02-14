# 7vertex 8 edge
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(v):
    # 방문처리
    visited[v] = 1
    print(v, end=' ')

    # 시작정점의 인접한 모든 정점에 대해서 - for
    # 방문 안 한 정점이면 재귀호출
    for w in range(1, V+1):
        if adj_mat[v][w] == 1 and visited[w] == 0:
            dfs(w)



V, E = map(int, input().split())
adj_mat = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
tmp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접행렬에 저장
for i in range(E):
    # 쌍을 저장
    s, e = tmp[2*i], tmp[2*i+1]

    # 방향성이 없으니까 양 쪽 둘 다 넣어서 전치행렬 만들어줌
    adj_mat[s][e] = adj_mat[e][s] = 1

dfs(1)