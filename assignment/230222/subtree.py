
def go(root):
    global cnt
    cnt +=1

    if tree[root][0]:
        go(tree[root][0])
    if tree[root][1]:
        go(tree[root][1])

T = int(input())

for test_case in range(1,T+1):
    E, R = map(int, input().split())
    L = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(E+2)]

    for i in range(E):
        p, c = L[i*2], L[i*2 + 1]

        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c

    cnt = 0
    go(R)

    print(f'#{test_case} {cnt}')