
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        farm.append(list(map(int, input())))

    point = N // 2

    # 기준까지
    farm_sum = 0
    for f in range(point + 1):
        for s in range(point - f, point + f + 1):
            farm_sum += farm[f][s]

    for f in range(point + 1, N):
        for s in range(point - (N - f - 1), point + (N - f - 1) + 1):
            farm_sum += farm[f][s]

    print(f'#{test_case} {farm_sum}')