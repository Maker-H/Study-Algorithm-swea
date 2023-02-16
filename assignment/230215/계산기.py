import sys
sys.stdin = open('계산기.txt', 'r')


T = 10

for tc in range(1, T+1):
    I_len = int(input())
    I = list(input())
    ans = []
    operator = []



    for c in I:
        if c.isdigit():
            ans.append(c)
        elif c == '(':
            operator.append(c)
        elif c == ')':
            tmp = operator[-1]
            while tmp != '(':
                ans.append(operator.pop())
                tmp = operator[-1]
            operator.pop()
        elif c == '+' or c == '-':
            if len(operator) != 0 and (operator[-1] == '*' or operator[-1] == '/'):
                ans.append(operator.pop())
            elif len(operator) != 0 and (operator[-1] == '+' or operator[-1] == '-'):
                ans.append(operator.pop())
            operator.append(c)
        elif c == '/' or c == '*':
            if len(operator) != 0 and (operator[-1] == '*' or operator[-1] == '/'):
                ans.append(operator.pop())
            operator.append(c)

    for idx in range(len(operator)-1, -1, -1):
        ans.append(operator[idx])

    stack = []
    for c in ans:
        if c.isdigit():
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

    print(f'#{tc} {stack[0]}')
