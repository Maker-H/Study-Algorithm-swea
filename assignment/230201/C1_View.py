import sys

def get_max_building_house(current_idx, tower_map):

    four_tower = [0 for i in range(4)]

    four_tower[0] = tower_map[current_idx - 1]
    four_tower[1] = tower_map[current_idx - 2]
    four_tower[2] = tower_map[current_idx + 1]
    four_tower[3] = tower_map[current_idx + 2]

    max = 0

    for one in four_tower:
        if max < one:
            max = one

    house = tower_map[current_idx] - max

    if house < 0:
        return 0
    else:
        return house


sys.stdin = open("C1_input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    tower_map = list(map(int, input().split()))

    houses = 0
    for idx in range(2, len(tower_map) - 2):
        houses += get_max_building_house(idx, tower_map)

    print(f'#{test_case} {houses}')
