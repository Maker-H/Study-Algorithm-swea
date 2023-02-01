import sys


sys.stdin = open("C1_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tower_map = list(map(int, input().split()))

    for idx in range(len(tower_map)+1):
        if 1 <= tower_map[idx]:
            hight = idx - (1의 idx) -1





