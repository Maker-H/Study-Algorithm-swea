T = int(input())

for test_case in range(1, T+1):
    str1 = list(set(list(input())))
    str2 = list(input())

    answer = {}
    for target in str1:
        if target not in answer:
            cnt = 0
            for c in str2:
                if c == target:
                    cnt += 1
            answer[target] = cnt
        elif target in answer:
            answer[target] += 1

    num_max = 0
    for num in answer.values():
        if num > num_max:
            num_max = num

    print(f'#{test_case} {num_max}')

