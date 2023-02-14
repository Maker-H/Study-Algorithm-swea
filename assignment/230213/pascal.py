T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = []

    for level in range(N):
        tmp = [1]
        for idx in range(level):
            if level > 1 and 0 < idx < len(pascal[level-1]):
                tmp.append(pascal[level-1][idx] + pascal[level-1][idx-1])

        if level == 0:
            pass
        else:
            tmp.append(1)
        pascal.append(tmp)

    print(f'#{tc}')
    for line in pascal:
        print(" ".join(map(str, line)))
