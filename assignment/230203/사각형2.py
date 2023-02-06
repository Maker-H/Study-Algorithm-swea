
T = int(input())

for test_case in range(1, T+1):
    L = L_tmp =int(input())
    sq = [[0 for _ in range(L)] for _ in range(L)]

    alpha = [0 for _ in range(26)]
    tmp = ord('A')
    for idx in range(26):
        alpha[idx] = chr(tmp)
        tmp += 1

    blank_idx = 0

    alpha_idx = 0
    for second_idx in range(L-1, -1, -1):
        for first_idx_1 in range(0, blank_idx):
            sq[first_idx_1][second_idx] = ' '

        for first_idx_2 in range(blank_idx, L):
            if alpha_idx > 25:
                alpha_idx = alpha_idx % 26
            sq[first_idx_2][second_idx] = alpha[alpha_idx] + ' '
            alpha_idx += L_tmp
            L_tmp -= 1



        L_tmp = L
        blank_idx += 1
        alpha_idx = blank_idx



    print(f'#{test_case}')
    for idx in range(L):
        print("".join(list(map(str, sq[idx]))))

