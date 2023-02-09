T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for f in range(N):
        for s in range(N-M+1):
            flag = 1
            for ds in range(M//2):
                if arr[f][s+ds] != arr[f][(s+M-1) - ds]:
                    flag = 0
                    break
            if flag:
                for ds in range(M):
                    print(arr[f][s+ds], end='')

