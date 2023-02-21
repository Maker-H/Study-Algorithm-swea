def bfs(f, s, N):
    Q = []
    Q.append([f, s])


    while Q:
        v = Q.pop(0)

        f = v[0]
        s = v[1]

        if arr[f][s] == 3:
            return True

        arr[f][s] = 9

        for idx in range(4):
            nf = f + df[idx]
            ns = s + ds[idx]

            if 0 <= nf < N and 0 <= ns < N and arr[nf][ns] != 1 and arr[nf][ns] != 9:
                Q.append([nf, ns])
    return False

T = 10

for test_case in range(1, T+1):
    input()
    N = 16
    arr = []
    df = [0, 0, 1, -1]
    ds = [1, -1, 0, 0]
    for _ in range(N):
        arr.append(list(map(int,list(input()))))

    is_possible = bfs(1,1, N)

    if is_possible:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
