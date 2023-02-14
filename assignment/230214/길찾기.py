
def recur(v):
    visited[v] = 1

    for w in range(V):
        if v == V-1:
            global flag
            flag = 1
            return
        if adj_mat[v][w] == 1 and visited[v] != 0:
            recur(w)




T = 1

for tc in range(1, T+1):
    num, l_len = map(int, input().split())
    tmp = list(map(int, input().split()))
    V = 100
    visited = [0] * V
    adj_mat = [[0] * V for _ in range(V)]
    flag = 0

    for i in range(l_len):
        s, e = tmp[2*i], tmp[2*i + 1]
        adj_mat[s][e] = 1

    recur(0)
    print(f'#{tc} {flag}')

