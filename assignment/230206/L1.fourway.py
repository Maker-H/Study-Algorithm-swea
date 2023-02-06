import sys

def abs(n):
    if n < 0:
        return -n
    else:
        return n

sys.stdin = open('L1.fourway.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for f in range(N):
        for s in range(N):
            for df, ds in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                df = f + df
                ds = s + ds
                if df == -1 or ds == -1 or df == N or ds == N:
                    pass
                else:
                    # print(f, s, df, ds)
                    result += abs(A[df][ds] - A[f][s])


    print(f'#{test_case} {result}')
