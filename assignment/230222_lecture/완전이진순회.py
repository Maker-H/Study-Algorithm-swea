def preorder(v):
    if v <= last:
        print(tree[v])
        preorder(2*v) # 왼쪽
        preorder(2*v + 1) # 오른쪽


tree = [0, 1, 2, 3, 4, 5, 6, 7]
last = 7
preorder(1)