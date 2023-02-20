T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))[::-1]

    idx = 0
    mx = arr[0]
    mx_i = 0
    total = 0
    while idx < N:
        if arr[idx] > mx:
            mx = arr[idx]
            mx_i = idx

        elif arr[idx] < mx:
            total += arr[mx_i] - arr[idx]
        idx += 1

    print(f'#{tc} {total}')