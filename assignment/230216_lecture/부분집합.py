def printset(n):
    for i in range(n):
        if bit[i]:
            sum += arr[i]

    if sum == 10:
        for i in range(n):
            if bit[i]:
                print(arr[i], end=' ')
        print()


def powerset(n, k): # n 원소의 개수, k 현재 depth
    if n == k:    # basis part 멈추는 부분
        print(bit, end=' ')
        for i in range(n):
            if bit[i] == 1:
                print(arr[i], end=' ')
        print()


    else:        # inductive part 유도파트
        # 포함될 때
        bit[k] = 1
        powerset(n, k+1)
        # 포함되지 않을 때
        bit[k] = 0
        powerset(n, k + 1)


arr = [1, 2, 3]
N = len(arr)
bit = [0] * N
powerset(N, 0)
