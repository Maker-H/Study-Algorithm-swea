T = int(input())

for tc in range(1, T+1):
    I = input().split()
    stack = []
    flag = False
    for c in I:
        if c == '.':
            break
        elif c.isdigit():
            stack.append(int(c))
        elif c == '/' or c == '+' or c == '-' or c == '*':
            if len(stack) <= 1:
                flag = True
                break
            if c == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) // int(a))
            elif c == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) + int(a))
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) - int(a))
            elif c == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) * int(a))

    if flag == True or len(stack) > 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')
