
def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            # 단어를 넣을 수 있는 공백
            if n == 1:
                cnt += 1
            else: # 칸없음
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]

    # arr와 arr_t로 각각 개수를 계산
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)

    print(f'#{test_case} {ans}')