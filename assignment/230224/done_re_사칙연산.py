def postorder(current):
    if current <= N:
        if len(tree[current]) == 3:
            right = tree[current][1]
            left = tree[current][2]

            if right <= N:
                postorder(right)

            if left <= N:
                postorder(left)

            if right <= N and left <= N:
                if tree[current][0] == '-':
                    tree[current][0] = tree[right][0] - tree[left][0]
                if tree[current][0] == '*':

                    tree[current][0] = tree[right][0] * tree[left][0]
                if tree[current][0] == '/':
                    tree[current][0] = tree[right][0] / tree[left][0]
                if tree[current][0] == '+':
                    tree[current][0] = tree[right][0] + tree[left][0]


T = 10

for test_case in range(1, T+1):
    N = int(input())
    tree = [[] for _ in range(N+1)]

    for _ in range(N):
        tmp = list(input().split())
        v = int(tmp[0])
        # 연산자 있으면
        if len(tmp) == 4:
            tree[v].append(tmp[1])
            tree[v].append(int(tmp[2]))
            tree[v].append(int(tmp[3]))

        # 연산자 없으면
        else:
            tree[v].append(int(tmp[1]))

    postorder(1)
    print(f'#{test_case} {int(tree[1][0])}')