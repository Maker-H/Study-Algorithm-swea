import sys

sys.stdin = open('L3_subset_sum.txt', 'r')
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for test_case in range(1, T+1):
    N, K = tuple(map(int, input().split()))
    a_len = 12
    total_cnt = 0
    for num in range(1 << 12):
        cnt = 0
        sub_sum = 0
        for idx in range(12):
            if num & (1 << idx):
                cnt += 1
                sub_sum += A[idx]
        if cnt == N and sub_sum == K:
            total_cnt += 1


    print(f'#{test_case} {total_cnt}')
