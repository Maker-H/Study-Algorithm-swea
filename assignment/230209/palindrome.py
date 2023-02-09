import sys

def is_palindrome(s):
    flag = True
    s_len = len(s)
    for i in range(s_len // 2):
        if s[i] == s[s_len-1 -i]:
            pass
        else:
            flag = False
            break

    return flag

sys.stdin = open('palindrome.txt', 'r')

T = 10
for tc in range(1, T+1):
    palin_len = int(input())
    my_map = [list(input()) for _ in range(8)]

    cnt = 0

    for f in range(8):
        for s in range(8-palin_len+1):
            tmp_row_word = ''
            tmp_col_word = ''
            for ds in range(palin_len):
                tmp_row_word += my_map[f][s+ds]
                tmp_col_word += my_map[s+ds][f]

            if is_palindrome(tmp_col_word):
                cnt += 1
            if is_palindrome(tmp_row_word):
                cnt += 1

    print(f'#{tc} {cnt}')

