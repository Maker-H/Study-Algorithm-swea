import sys
sys.stdin = open("L1_sample_input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    H, W = tuple(map(int, input().split()))

    print(f'#{test_case}')

    cnt = 0
    for _ in range(H):
        tmp = " ".join(list(map(str, range(1 + W*cnt, W+1 + W*cnt))))
        cnt += 1
        print(tmp)

