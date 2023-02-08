T = int(input())

for test_case in range(1, T+1):
    snail_size = int(input())
    snail = [[0] * snail_size for _ in range(snail_size)]

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0], ] # 좌, 하, 우, 상

    delta_idx = 0
    val = 1
    f = s = 0
    while True:
        if val == snail_size * snail_size + 1:
            break
        if f != snail_size and s != snail_size and f != -1 and s != -1 and snail[f][s] == 0:
            snail[f][s] = val
            f = f + delta[delta_idx][0]
            s = s + delta[delta_idx][1]
            val += 1

        else:
            f = f - delta[delta_idx][0]
            s = s - delta[delta_idx][1]

            delta_idx = (delta_idx + 1) % 4
            f = f + delta[delta_idx][0]
            s = s + delta[delta_idx][1]

    print(f'#{test_case}')
    for oneline in snail:
        print(*oneline)