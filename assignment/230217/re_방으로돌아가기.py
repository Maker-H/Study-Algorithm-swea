T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = []
    for _ in range(N):
        s, e = map(int, input().split())
        room.append([s, e])

    cnt = 1
    for i in range(N):
        for j in range(i+1, N):
            first = room[i][1]
            second = room[j][0]
            if first % 2 == 1:
                first += 1
            if second % 2 == 1:
                second += 1

            if first >= second:
                cnt += 1

            if cnt >= N:
                cnt = N
                break

    print(f'#{tc} {cnt}')
