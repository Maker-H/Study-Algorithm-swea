def find_max_idx (s, e):
    mx = 0
    mx_idx = -1
    for i in range(s, e+1):
        if arr[i] > mx:
            mx = arr[i]
            mx_idx = i

    return (s, mx_idx)

def profit(s, e):
    arr_sum = 0
    if s == e:
        return 0

    for i in range(s, e):
        arr_sum = arr_sum + arr[e] - arr[i]

    return arr_sum

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mx_idx = 0
    total_sum = 0

    while mx_idx < N:
        mn_idx, mx_idx = find_max_idx(mx_idx, N - 1)

        total_sum += profit(mn_idx, mx_idx)

        mx_idx += 1

    print(f'#{tc} {total_sum}')