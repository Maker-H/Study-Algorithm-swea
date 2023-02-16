def printset(n, cursum):
    if cursum == 10:
        for i in range(n):
            if bit[i] == 1:
                print(arr[i], end=' ')
        print()


def powerset(n, k, cursum): # n 원소의 개수, k 현재 depth
    global cnt
    cnt += 1
    ############################
    if cursum > 10: return  # 이게 가지치기
    ############################

    if n == k:    # basis part 멈추는 부분
        printset(n, cursum)
    else:        # inductive part 유도파트
        # 포함될 때
        bit[k] = 1
        powerset(n, k+1, cursum + arr[k])
        # 포함되지 않을 때
        bit[k] = 0
        powerset(n, k + 1, cursum)

cnt = 0
arr = list(range(1, 11))
N = len(arr)
bit = [0] * N
powerset(N, 0, 0)
print(f'cnt={cnt}')