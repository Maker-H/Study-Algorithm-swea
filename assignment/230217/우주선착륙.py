
T = int(input())

for test_case in range(1, T+1):
    num_of_row, num_of_col = map(int, input().split())

    site = []
    for _ in range(num_of_row):
        site.append(list(map(int, input().split())))

    delta =((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)) # 시계방향

    ans = 0
    for f in range(num_of_row):
        for s in range(num_of_col):
            cnt = 0
            for idx in range(8):
                nf = f + delta[idx][0]
                ns = s + delta[idx][1]

                if 0 <= nf < num_of_row and 0 <= ns < num_of_col:
                    if site[f][s] > site[nf][ns]:
                        cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{test_case} {ans}')