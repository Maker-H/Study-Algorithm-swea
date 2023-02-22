def find_parent(pick, current):
    parent = tree[current][2]

    if parent == 0:
        return

    if pick == 1:
        G1_arr.append(parent)
    else:
        G2_arr.append(parent)

    find_parent(pick, parent)




def find_subtree_len(current):
    global cnt
    cnt += 1

    if tree[current][0] != 0:
        find_subtree_len(tree[current][0])

    if tree[current][1] != 0:
        find_subtree_len(tree[current][1])


T = int(input())
for test_case in range(1, T+1):
    V, E, G1, G2 = map(int, input().split())

    parents = []

    arr = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]

    for i in range(len(arr) // 2):
        p, c = arr[i*2], arr[i*2+1]

        if tree[p][0] == 0:
            tree[p][0] = c
        elif tree[p][0] != 0:
            tree[p][1] = c

        tree[c][2] = p

    G1_arr = []
    G2_arr = []
    find_parent(1, G1)
    find_parent(2, G2)

    ans_node = i = j = 0
    flag = False
    for i in range(len(G1_arr)):
        for j in range(len(G2_arr)):
            if G1_arr[i] == G2_arr[j]:
                ans_node = G1_arr[i]
                flag = True
                break

            if flag:
                break

    print(G1_arr)
    print(G2_arr)

    cnt = 0
    find_subtree_len(ans_node)

    print(f'#{test_case} {ans_node} {cnt}')

