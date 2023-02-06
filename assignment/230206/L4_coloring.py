import sys
sys.stdin = open('L4_coloring.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    Arr = [[0]*10 for _ in range(10)]

    for color in range(N):
        fx, fy , sx, sy, c = tuple(map(int, input().split()))

        # 한 좌표에 대해 색칠하기
        for f in range(fx, sx+1):
            for s in range(fy, sy+1):
                if Arr[f][s] == 0:
                    Arr[f][s] = c
                elif c == 1 and Arr[f][s] == 2:
                    Arr[f][s] += c
                elif c == 2 and Arr[f][s] == 1:
                    Arr[f][s] += c

    cnt = 0
    for f in range(10):
        for s in range(10):
            if Arr[f][s] == 3:
                cnt += 1

    print(f'#{test_case} {cnt}')

