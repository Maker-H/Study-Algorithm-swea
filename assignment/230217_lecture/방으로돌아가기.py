T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnts = [0] * 200

    for _ in range(N):
        s, e = map(int, input().split())
        for i in range((s - 1) // 2, (e - 1) // 2 + 1):
            cnts[i] += 1

    ans = max(cnts)

    print(f'#{tc} {ans}')


# ----------------------- 위는 잘못된 제출------ 모두 0?, 모두 mx?, 음수포함?, 정렬x?, 경계에만 값?


for tc in range(1, T + 1):
    N = int(input())
    cnts = [0] * 200

    for _ in range(N):
        s, e = map(int, input().split())

        if s > e:
            s, e = e, s

        for i in range((s - 1) // 2, (e - 1) // 2 + 1):
            cnts[i] += 1

    ans = max(cnts)

    print(f'#{tc} {ans}')