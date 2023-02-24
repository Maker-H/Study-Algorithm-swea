def search_once(node):
    s = tree[node][2]
    p = []

    while s != 0:
        p.append(s)
        s = tree[s][2]

    return p

def findA(p1, p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j]:
                return p1[i]

def preorder(node):
    global cnt

    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])


T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    tmp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]

    for i in range(E):
        p, c = tmp[2*i], tmp[2*i + 1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c

        tree[c][2] = p

    p1 = search_once(n1)
    p2 = search_once(n2)
    print()

    # 가까운 공통조상 찾기
    CA = findA(p1, p2)
    cnt = 0
    preorder(CA)
    print(f'#{tc} {CA} {cnt}')