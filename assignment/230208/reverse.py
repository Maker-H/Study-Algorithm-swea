import copy

def swap_is_same(S):
    new_S = list(S)
    S = copy.copy(new_S)
    for idx in range(len(S)//2):
        new_S[idx], new_S[len(S)-1 - idx] = new_S[len(S)-1 -idx] , new_S[idx]

    if S == new_S:
        return True
    else:
        return False

T = int(input())

for test_case in range(1, T+1):
    map_size, string_size = tuple(map(int, input().split()))

    my_map = [list(input()) for _ in range(map_size)]

    col_row_repeat = map_size - string_size + 1

    answer = ''

    for f in range(map_size):
        for s in range(col_row_repeat):
            row_tmp = ''
            col_tmp = ''

            for ds in range(s, s+string_size):
                row_tmp += my_map[f][ds]
                col_tmp += my_map[ds][f]

            if swap_is_same(row_tmp):
                answer = row_tmp
                break
            elif swap_is_same(col_tmp):
                answer = col_tmp
                break


    print(f'#{test_case} {answer}')
