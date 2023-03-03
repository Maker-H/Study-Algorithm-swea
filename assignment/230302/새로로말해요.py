
T = int(input())
for test_case in range(1, T+1):
    ans = []
    max_len_tmp = 0
    for _ in range(5):
        tmp = list(input())
        ans.append(tmp)
        if len(tmp) > max_len_tmp:
            max_len_tmp = len(tmp)

    for idx in range(5):
        if len(ans[idx]) < max_len_tmp:
            for _ in range(max_len_tmp - len(ans[idx])):
                ans[idx] = ans[idx] + ['']

    re_ans = []
    for f in range(max_len_tmp):
        for s in range(5):
            re_ans.append(ans[s][f])


    print(f'#{test_case}', end=' ')
    for a in re_ans:
        for c in a:
            if c != '':
                print(c, end='')

    print()