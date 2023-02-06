import sys

def minmax_idx(boxes):
    box_max_val = 105
    box_max_idx = 0
    box_min_val = 0
    box_min_idx = 0
    for idx in range(len(boxes)):
        if box_min_val > boxes[idx]:
            box_min_val = boxes[idx]
            box_min_idx = idx
        if box_max_val < boxes[idx]:
            box_max_val = boxes[idx]
            box_max_idx = idx

    return (box_min_idx, box_max_idx)

sys.stdin = open('flatten.txt', 'r')

T = 10
for test_case in range(1, T+1):
    dump_num = int(input())
    boxes = list(map(int, input().split()))

    for main_idx in range(dump_num):
        min_idx, max_idx = minmax_idx(boxes)

        if boxes[max_idx] - boxes[min_idx] <= 1:
            break

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    min_idx, max_idx = minmax_idx(boxes)
    answer = boxes[max_idx] - boxes[min_idx]

    print(f'#{test_case} {answer}')
