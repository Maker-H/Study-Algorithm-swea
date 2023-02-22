def inorder(current):

    if current != 0:
        inorder(tree[current][0])


        print(tree[current][3], end='')
        
        inorder(tree[current][1])

T = 10

for test_case in range(1, T+1):
    N = int(input())

    tree = [[0] * 4 for _ in range(N+1)]

    for _ in range(N):
        tmp = ['0'] * 4
        I = input().split()

        for i in range(len(I)):
            tmp[i] = I[i]

        current, ch, left, right = map(lambda x: int(x) if x.isdigit() else x, tmp)

        tree[current][0] = left
        tree[current][1] = right
        tree[current][3] = ch

        tree[left][2] = current
        tree[right][3] = current

    print(f'#{test_case}', end=' ')
    inorder(1)

    print()