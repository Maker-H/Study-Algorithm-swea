from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    arr = []

    # pop()으로 뽑을 수 있게 역순으로 정렬
    for idx in range(M-1, -1, -1):
        e = [tmp[idx], idx+1]
        arr.append(e)

    D = deque()
    # 화덕의 크기 만큼 넣기
    for _ in range(N):
        D.append(arr.pop())

    while len(D) != 1:

        t = D.popleft()
        val = t[0]

        if val != 0:
            D.append([val // 2, t[1]])

        elif val == 0 and len(arr) != 0:
            D.appendleft(arr.pop())

        elif val == 0 and len(arr) == 0:
            pass

    print(f'#{test_case} {D.pop()[1]}')

