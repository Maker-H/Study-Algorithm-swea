from collections import deque

T = 1
for test_case in range(1, T+1):
    n = int(input())

    lst = list(map(int, input().split()))
    D = deque()

    for idx in range(8):
        D.append([lst[idx], idx])

    cnt = 1
    while True:

        val = D.popleft()

        if val[0] - cnt <= 0:
            val[0] = 0
        else:
            val[0] = val[0] - cnt
        D.append([val[0], val[1]])

        cnt += 1
        if cnt == 6:
            cnt = 1

        if val[0] == 0:
            break




    print(f'#{test_case} {" ".join(list( map(lambda x : str(x[0]), D )))}')