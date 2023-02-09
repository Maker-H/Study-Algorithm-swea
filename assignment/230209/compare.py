T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = list(input())
    str1_len = len(str1)
    str2_len = len(str2)

    for main_idx in range(str2_len - str1_len +1):
        tmp = ''
        for compare_idx in range(str1_len):
            tmp += str2[main_idx + compare_idx]
        if tmp == str1:
            print(f'#{tc} {1}')
            break

    if tmp != str1:
        print(f'#{tc} 0')