T = int(input())

for test_case in range(1, T+1):
    stick = list(input())

    stack = []
    ans = 0
    idx = 0
    for c in stick:

        if c == '(':
            stack.append('(')
        elif c == ')':
            if stick[idx-1] == '(':
                stack.pop()
                ans += len(stack)
            elif stick[idx-1] == ')':
                stack.pop()
                ans += 1
        idx += 1

    print(f'#{test_case} {ans}')