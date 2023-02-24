import sys
sys.setrecursionlimit(10 ** 5)
def inorder(current, level):
    global cnt

    if current <= N and current != -1:
        node_level[current] = level

        left = tree[current][0]
        right = tree[current][1]

        if left != -1:
            inorder(left, level + 1)

        # 레벨 안에 제일 작은 값보다 더 작으면 더해주기
        if right_min[node_level[current]] > cnt:
            right_min[node_level[current]] = cnt

        if left_max[node_level[current]] < cnt:
            left_max[node_level[current]] = cnt

        cnt += 1

        if right != -1:
            inorder(right, level + 1)

    else:
        return 0

N = int(sys.stdin.readline())

# 노드의 레벨 표기하는 인덱스
node_level = [0] * (N + 1)
is_root = [-1] * (N + 1)
tree = [[-1] * 2 for _ in range(N + 1)]

for _ in range(N):
    V, R, L = map(int, sys.stdin.readline().split())
    tree[V][0] = R
    tree[V][1] = L

    is_root[R] = 1
    is_root[L] = 1


root = 0
for i in range(len(is_root)):
    if is_root[i] == -1:
        root = i
print(root)

cnt = 1
right_min = [N + 1] * (N + 1)
left_max = [0] * (N + 1)
inorder(root, 1)

ans = 0
ans_idx = 0
for i in range(1, N+1):
    diff = left_max[i] - right_min[i] + 1

    if diff > ans:
        ans = diff
        ans_idx = i


print(ans_idx, ans)




