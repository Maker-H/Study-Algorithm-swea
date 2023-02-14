T = 10
for tc in range(1, T+1):
    num, S = input().split()
    num = int(num)
    S = list(S)
    stack = []
    top = -1

    for c in S:
        if top == -1:
            stack.append(c)
            top += 1
        else:
            if c == stack[top]:
                stack.pop()
                top -= 1
            else:
                stack.append(c)
                top += 1

    print(f'#{tc} {"".join(stack)}')