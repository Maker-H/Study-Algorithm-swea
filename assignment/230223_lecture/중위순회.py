T = 10

def inorder(v):
    global ans
    if v <= N:
        inorder(2*v)
        ans += tree[v]
        ans.append(tree[v])
        inorder(2*v + 1)


for tc in range(1, T+1):
    N = int(input())
    tree = [''] * (N+1)

    for i in range(N):
        tmp = list(input().split())
        idx = int(tmp[0])
        tree[idx] = tmp[1]
    ans = ''
    inorder(1)
    print(f'#{tc}', ''.join(ans))
