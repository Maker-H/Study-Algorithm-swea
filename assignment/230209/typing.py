T = int(input())

for tc in range(1, T+1):
    main, compare = tuple(input().split())

    main = list(main)
    main_len = len(main)
    compare_len = len(compare)

    cnt = 0
    flag = compare_len

    main_idx = 0
    while main_idx <= main_len - compare_len:
        tmp = ''
        for idx in range(compare_len):
            tmp += main[main_idx + idx]
        if tmp == compare:
            main_idx += compare_len
            cnt += 1

        else:
            main_idx += 1
    answer = main_len - (cnt*compare_len) + cnt
    print(f'#{tc} {answer}')