import sys
sys.stdin = open("11758_sample_input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    user_inputs = list(map(int, input().split()))

    max = 0
    min = 1000001
    for num in user_inputs:
        if max < num:
            max = num
        if min > num:
            min = num

    print(f'#{test_case} {max - min}')
