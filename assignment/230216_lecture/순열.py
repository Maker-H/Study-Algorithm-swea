def perm(n, k): #n number of element, k depth
    if n == k:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]




arr = [1, 2, 3]
N = len(arr)
perm(N, 0)
