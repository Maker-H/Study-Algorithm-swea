T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    game = [[0] * (N + 1) for _ in range(N + 1)]
    setpoint = N // 2
    game[setpoint][setpoint] = 2
    game[setpoint + 1][setpoint + 1] = 2
    game[setpoint + 1][setpoint] = 1
    game[setpoint][setpoint + 1] = 1

    dx = [1, -1, 0, 0, 1, -1, 1, -1 ]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    cnt = 0
    for _ in range(M):
        f, s, rock = map(int, input().split())
        game[f][s] = rock
        cnt += 1
        for k in range(8):
            for spread in range(1, N):
                nf = f + dx[k] * spread
                ns = s + dy[k] * spread

                
                if 0 <= nf < (N+1) and 0 <= ns < (N+1):
                    if game[nf][ns] == 0:
                        break

                    elif game[nf][ns] == rock:
                        tmp_f = f
                        tmp_s = s
                        while tmp_f != nf or tmp_s != ns:
                            game[tmp_f][tmp_s] = rock
                            tmp_f += dx[k]
                            tmp_s += dy[k]
                        break

        if cnt == (N+1)**2:
            break

    black_sum = 0
    white_sum = 0
    for f in range(N+1):
        for s in range(N+1):
            if game[f][s] == 1:
                black_sum += 1
            elif game[f][s] == 2:
                white_sum += 1
    
    print(f'#{test_case} {black_sum} {white_sum}')

        

