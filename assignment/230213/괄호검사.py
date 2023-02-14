T = int(input())

for test_case in range(1, T+1):
    I = list(input())

    stack = []
    size = -1
    answer = 1

    for c in I:
        if c == '{':
            stack.append('{')
            size += 1

        elif c =='(':
            stack.append('(')
            size += 1

        elif c == '}':
            if size == -1:
                answer = 0
                break

            elif stack[size] == '{':
                stack.pop()
                size -= 1

            elif stack[size] == '(':
                answer = 0
                break


        elif c == ')':
            if size == -1:
                answer = 0
                break

            elif stack[size] == '(':
                stack.pop()
                size -= 1

            elif stack[size] == '{':
                answer = 0
                break

    if size != -1:
        answer = 0
    print(f'#{test_case} {answer}')