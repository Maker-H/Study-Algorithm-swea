'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(v):
    if v != 0:
        print(v, end=' ')
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):
    if v != 0 :
        inorder(tree[v][0])
        print(v, end=' ')
        inorder(tree[v][1])

def postorder(v):
    if v != 0 :
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end=' ')

V = int(input())
E = V - 1
# 인접리스트
tree = [[0] * 3 for _ in range(V+1)]
temp = list(map(int, input().split()))

for i in range(E):
    p, c = temp[i*2], temp[i*2+1]  # 부모, 자식

    if tree[p][0] == 0: # 왼쪽자식이 없으면
        tree[p][0] = c
    else:
        tree[p][1] = c

    tree[c][2] = p

for t in tree:
    print(*t)

preorder(1); print()
inorder(1); print()
postorder(1); print()
