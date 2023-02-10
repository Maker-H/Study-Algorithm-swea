import sys

sys.stdin = open('palindrome.txt', 'r')

def swap(s):
    s_len = len(s)
    for idx in range(s_len // 2):
        if s[idx] != s[s_len-1 -idx]:
            return False
    return True

T = 10
N = input()

for tc in range(1, T+1):
    map_len = 100
    my_map = [list(input()) for _ in range(map_len)]

    flag = False
    pali_max = 0
    for f in range(map_len):
        for k in range(2, map_len):
            for s in range(map_len-k):
                row_tmp = ''
                col_tmp = ''
                for ds in range(k):
                    print(f, s+ds)
                    row_tmp += my_map[f][s+ds]
                    col_tmp += my_map[s+ds][f]

                if swap(row_tmp) or swap(col_tmp):
                    if pali_max < k:
                        pali_max = k
                    else:
                        flag = True
            if flag:
                break


    print(pali_max)