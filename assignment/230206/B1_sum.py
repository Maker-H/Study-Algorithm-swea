import sys
sys.stdin = open('B1_sum.txt', 'r')



for test_case in range(1, 11):
    T = int(input())
    Arr = [[0]*100 for _ in range(100)]

    result = [0] * 202

    # 배열 입력 받기
    for f in range(100):
        Arr[f] = list(map(int, input().split()))

    for f in range(100):
        r_sum = 0
        c_sum = 0
        for s in range(100):
            r_sum += Arr[f][s]
            c_sum += Arr[s][f]
        result[f] = r_sum
        result[201 - f] = c_sum

    max = 0

    for idx in range(202):
        if max < result[idx]:
            max = result[idx]

    print(f'#{test_case} {max}')