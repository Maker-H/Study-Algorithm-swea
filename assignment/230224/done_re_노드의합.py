def inorder(current):

        if current <= N and tree[current] == 0:

            right_idx = current * 2
            left_idx = current * 2 + 1

            # 오른쪽부터 순회
            inorder(right_idx)

            inorder(left_idx)

            if left_idx <= N:
                tree[current] = tree[right_idx] + tree[left_idx]
            elif right_idx <= N:
                tree[current] = tree[right_idx]

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    inorder(1)
    print(f'#{test_case} {tree[L]}')