T = int(input())

for tc in range(1, T+1):
    I = list(input())
    stack = []
    top = -1

    for c in I:
        if top == -1:
            stack.append(c)
            top += 1

        elif top != -1:
            if stack[top] == c:
                stack.pop()
                top -= 1
                pass

            elif stack[top] != c:
                stack.append(c)
                top += 1

    print(f'{tc} {top + 1}')
