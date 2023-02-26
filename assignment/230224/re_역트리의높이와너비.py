import sys

def inorder(current, level):
    global max_level 

    if current != -1:

        if max_level < level:
            max_level = level

        left = tree[current][0]
        right = tree[current][1]

        inorder(left, level + 1)
        
        ans.append([level, current])

        inorder(right, level + 1)
    
    return



N = int(sys.stdin.readline())

tree = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
# 노드 정리
for _ in range(N):
    current, left, right = map(int, sys.stdin.readline().split())

    tree[current] = [left, right]

    # out of range 뜨지 않게
    if left != -1:
        parents[left] = 1
    
    if right != -1:
        parents[right] = 1


# root 구하기
for i in range(1, N + 1):
    if parents[i] == 0:
        root = i
        break

ans = []
max_level = 0
cnt = 1
inorder(root, 1)

ans_level = 0
total_max = 0
for i in range(1, max_level + 1):
    L = 0
    R = len(ans) - 1

    while ans[L][0] != i:
        L += 1
    while ans[R][0] != i:
        R -= 1
    
    tmp = R - L + 1

    if tmp > total_max:
        total_max = tmp
        ans_level = i
print(max_level)

print(ans_level, total_max)





