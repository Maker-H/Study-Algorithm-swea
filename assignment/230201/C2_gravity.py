import  sys

sys.stdin = open('C2_gravity.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    boxes_len = int(input())
    boxes = list(map(int, input().split()))

    highest_jump = 0

    for main_idx in range(boxes_len-1):

        box_jump = 0

        for compare_idx in range(main_idx, boxes_len):
            if boxes[main_idx] > boxes[compare_idx]:
                box_jump += 1

        # 다음 main_idx로 넘어가기 전에
        if highest_jump < box_jump:
            highest_jump = box_jump

    print(f'#{test_case} {highest_jump}')

