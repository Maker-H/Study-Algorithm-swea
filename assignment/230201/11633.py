import sys
sys.stdin = open("11633_sample_input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    N , M = tuple(map(int, input().split()))
    user_list = list(map(int, input().split()))

    sum_list = [0 for i in range(N - M + 1)]
    for idx in range(N - M + 1):
        user_sum = 0
        for main_idx in range(idx, idx+M):
            user_sum += user_list[main_idx]
        sum_list[idx] = user_sum

    max = sum_list[0]
    min = sum_list[0]
    for one in sum_list:
        if max < one:
            max = one
        if min > one:
            min = one

    print(f'#{test_case} {max-min}')
