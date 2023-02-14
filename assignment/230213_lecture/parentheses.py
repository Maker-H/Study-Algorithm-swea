'''
4
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
'''

def check_matching(data):
    I = list(data)
    global stack
    global top

    for c in I:
        if c == '(':
            stack.append('(')
            top += 1
        elif c == ')':
            if top == 0:
                return 0
            if top > 0:
                stack.pop()
                top -= 1


    if top == 0:
        return 1
    if top != 0:
        return 0

T = int(input())
for tc in range(1, T+1):
    stack = []
    top = 0
    data = input()
    print(f'#{tc} {check_matching(data)}')