import sys
sys.stdin = open('balloon.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = tuple(map(int, input().split()))

    balloon_map = [list(map(int, input().split())) for _ in range(N)]

    result = [0 for _ in range(M*N)]
    idx = 0
    for f in range(N):
        for s in range(M):
            balloon_sum = 0
            for df, ds in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                df = f + df
                ds = s + ds
                if df == -1 or ds == -1 or df >= N or ds >= M:
                    pass
                else:
                    balloon_sum += balloon_map[df][ds]
            result[idx] = balloon_sum
            idx += 1
    max = 0
    for idx in range(N*M):
        if max < result[idx]:
            max = result[idx]

    print(f'#{test_case} {max}')
