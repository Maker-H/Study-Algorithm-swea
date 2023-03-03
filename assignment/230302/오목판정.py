
def check_five():
    for f in range(N):
        for s in range(N):
            if game[f][s] == 'o':
                for k in range(8):
                    cnt = 1
                    for go in range(1, 5):
                        nf = f + dx[k] * go
                        ns = s + dy[k] * go

                        if 0 <= nf < N and 0 <= ns < N and game[nf][ns] == '.':
                            is_dot = True
                            break
                        if 0 <= nf < N and 0 <= ns < N and game[nf][ns] == 'o':
                            cnt += 1
                        if not (0 <= nf < N and 0 <= ns < N):
                            break


                    if cnt == 5:
                        return True
    return False

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    game = []
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]


    for _ in range(N):
        game.append(input())

    if check_five():
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')


