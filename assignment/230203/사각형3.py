
T = int(input())

for test_case in range(1, T+1):
    H, W = list(map(int, input().split()))
    sq = [[0 for _ in range(W)] for _ in range(H)]

    cnt = 1
    for first_idx in range(H):
        for second_idx in range(W):
            if first_idx % 2 == 0:
                sq[first_idx][second_idx] = cnt
            elif first_idx % 2 == 1:
                sq[first_idx][W - second_idx - 1] = cnt
            cnt += 1

    print(f'#{test_case}')
    for idx in range(H):
        print(" ".join(list(map(str, sq[idx]))))

