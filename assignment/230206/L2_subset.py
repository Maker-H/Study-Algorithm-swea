import sys

sys.stdin = open('L2_subset.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    A = list(map(int, input().split()))
    result = 0
    for sub_num in range(1 << N):
        sub_sum = 0
        for idx in range(N):
            if sub_num & (1 << idx):
                val = A[idx]
                sub_sum += val

        if sub_sum == 0 and sub_num != 0:
            break

    if sub_sum == 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')