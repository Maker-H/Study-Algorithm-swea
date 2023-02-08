T = int(input())

for test_case in range(1, T+1):
    total_page, a_target, b_target = tuple(map(int, input().split()))

    # a 찾기
    start = 1
    end = total_page
    a_cnt = 1
    c = (start + end) // 2

    while c != a_target:
        if c < a_target:
            start = c
        elif c > a_target:
            end = c

        c = (start + end) // 2
        a_cnt += 1


    # a 찾기
    start = 1
    end = total_page
    b_cnt = 1
    c = (start + end) // 2

    while c != b_target:
        if c < b_target:
            start = c
        elif c > b_target:
            end = c

        c = (start + end) // 2
        b_cnt += 1


    if a_cnt > b_cnt:
        print(f'#{test_case} B')
    elif a_cnt < b_cnt:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')