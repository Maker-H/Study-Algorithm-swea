T = int(input())
def preorder(v):
    global cnt
    if v != 0:
        cnt += 1
        preorder(tree[v][0])
        preorder(tree[v][1])
    return




for tc in range(1, T+1):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E)]

    for i in range(E):
        p, c = tmp[2*i], tmp[i*2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c

        tree[c][2] = p

    cnt = 0
    preorder(N)

    print(f'#{tc} {cnt}')