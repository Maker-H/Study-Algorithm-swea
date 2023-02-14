

def recur(v):
    visited[v] = 1

    for w in range(1, V+1):
        if adj_mat[v][w] == 1 and v != ans_e:
            recur(w)
        if v == ans_e:
            global flag
            flag = 1
            return 0



T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())

    flag = 0
    visited = [0] * (V+1)
    adj_mat = [[0] * (V+1) for _ in range(V+1)]

    for idx in range(E):
        s, e = map(int, input().split())
        adj_mat[s][e] = 1


    ans_s, ans_e = map(int, input().split())
    recur(ans_s)
    print(f'#{tc} {flag}')