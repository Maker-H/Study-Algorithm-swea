import sys
sys.stdin = open('specialsort.txt', 'r')
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    have_to_sort = list(map(int, input().split()))
    answer = [0] * N
    for main_i in range(N-1):
        maxmax = 0
        minmin = 101
        # 큰 수 정렬
        if main_i % 2 == 0:
            tmp = 0
            for compare_i in range(main_i+1, N):
                if maxmax < have_to_sort[compare_i]:
                    maxmax = have_to_sort[compare_i]
                    tmp = compare_i
            if have_to_sort[main_i] < have_to_sort[tmp]:
                have_to_sort[main_i], have_to_sort[tmp] = have_to_sort[tmp], have_to_sort[main_i]


        # 작은 수 정렬
        elif main_i % 2 == 1:
            tmp = 0
            for compare_i in range(main_i+1, N):
                if minmin > have_to_sort[compare_i]:
                    minmin = have_to_sort[compare_i]
                    tmp = compare_i
            if have_to_sort[main_i] > have_to_sort[tmp]:
                have_to_sort[main_i], have_to_sort[tmp] = have_to_sort[tmp], have_to_sort[main_i]

    print(f'#{test_case} {" ".join(list(map(str, have_to_sort[:10])))}')