import sys
import copy
sys.stdin = open('ledder.txt', 'r')
delta = [[0, 1], [0, -1], [1, 0]]

T = 10

for test_case in range(1, 1+T):
    N = int(input())
    my_max = 100
    ladder_map = [list(map(int, input().split())) for _ in range(my_max)]
    my_map = copy.deepcopy(ladder_map)

    start_line = ladder_map[0]
    start_points = [0 for _ in range(my_max)]
    points_idx = 0

    for idx in range(my_max):
        if start_line[idx] == 1:
            start_points[points_idx] = idx
            points_idx += 1



    for s in start_points:
        f = 0
        ms = s
        answer = s
        df = 0

        ladder_map = copy.deepcopy(my_map)

        while df != my_max-1:
            for delta_idx in range(3):
                df = f + delta[delta_idx][0]
                ds = ms + delta[delta_idx][1]
                if df != -1 and ds != -1 and df != my_max and ds != my_max:
                    if ladder_map[df][ds] == 1 and ladder_map[df][ds] != 9:
                        ladder_map[df][ds] = 9
                        f = df
                        ms = ds

                        break
                    else:
                        pass

        if ladder_map[df][ds] == 2:
            break

    print(f'#{test_case} {answer}')