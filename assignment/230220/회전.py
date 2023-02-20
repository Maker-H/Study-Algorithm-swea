from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    D = deque(arr)
    for _ in range(M):
        D.rotate(-1)

    print(f'#{test_case} {D.popleft()}')

