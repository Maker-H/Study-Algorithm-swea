def count(arr):
    mx = 0
    for lst in arr:
        cnt = 0
        for one in lst:
            if one == 1:
                cnt += 1
                if cnt > mx:
                    mx = cnt
            elif one == 0:
                cnt = 0
    return mx



T = int(input())
for tc in range(1, T+1):
    num_of_row, num_of_col = map(int, input().split())
    ground = []
    for _ in range(num_of_row):
        ground.append(list(map(int, input().split())))
    ro_ground = list(map(list, zip(*ground)))

    ground_max = count(ground)
    ro_ground_max = count(ro_ground)

    ans = 0
    if ro_ground_max > ground_max:
        ans = ro_ground_max
    else:
        ans = ground_max

    print(f'#{tc} {ans}')