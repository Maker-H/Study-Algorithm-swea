T = int(input())

def find_position(arr, pos):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == pos:
                return i, j


def dfs(x, y):

    if arr[x][y] == 3:
        global flag
        flag = 1
        return

    arr[x][y] = 9 # 1로 막아도 되는데 디버깅을 위해서 체크


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스 체크
        if nx < 0 or nx == N: continue
        elif ny < 0 or ny == N: continue

        # 방문 체크
        elif arr[nx][ny] == 9: continue

        # 벽 체크
        elif arr[nx][ny] == 1: continue

        dfs(nx, ny)



dx = [0, 1, 0, 1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sx, sy = find_position(arr, 2)
    flag = 0

    dfs(sx, sy)
    print(f'#{tc} {flag}')