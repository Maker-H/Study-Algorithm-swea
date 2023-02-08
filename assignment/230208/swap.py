def swap(c):
    c = list(c)
    str_len = len(c)
    swap_len = str_len // 2
    for idx in range(swap_len):

        c[str_len-1 - idx], c[idx] = c[idx], c[str_len-1 - idx]

    return "".join(c)

T = int(input())

for test_case in range(1, T+1):
    S = input()
    swap_S = swap(S)

    if S == swap_S:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
