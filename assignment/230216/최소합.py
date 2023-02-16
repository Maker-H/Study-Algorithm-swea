def recur(n, k, total):
    global min_value

    if total > min_value:
        return

    if n == k:
        if total < min_value:
            min_value = total
        return

    for i in range(k, n):
        arr[k], arr[i] = arr[i], arr[k]
        recur(n, k+1, total + A[k][arr[k]])
        arr[k], arr[i] = arr[i], arr[k]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(range(N))
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    min_value = 5000
    recur(N, 0, 0)

    print(f'#{tc} {min_value}')