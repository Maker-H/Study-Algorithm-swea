def push(item):
    global  top
    top += 1
    if top == N:
        print('overflow')
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('undeflow')
        return 0
    else:
        rst = stack[top]
        top -= 1
        return rst

stack = [0] * 10
N = len(stack)
top = -1
push(10)
push(20)

top += 1
stack[top] = 20

print(stack)