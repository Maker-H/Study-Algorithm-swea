def permutation(current, total_len, per_sum):
    global total_min

    if per_sum >= total_min:
        return

    if current == total_len:
        if per_sum < total_min:
            total_min = per_sum
        return

    for i in range(current, total_len):
        arr_idx[current], arr_idx[i] = arr_idx[i], arr_idx[current]
        permutation(current+1, total_len, per_sum + arr[current][arr_idx[current]])
        arr_idx[current], arr_idx[i] = arr_idx[i], arr_idx[current]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    total_min = 10 * 10
    arr_idx = list(range(N))

    permutation(0, N, 0)

    print(f'#{test_case} {total_min}')