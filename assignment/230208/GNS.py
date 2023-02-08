import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
ali_planet = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0,'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN': 0}

for test_case in range(1, T+1):
    drop, words_len = tuple(input().split())
    words_len = int(words_len)

    words = input().split()

    for word in words:
        if word in ali_planet:
            ali_planet[word] += 1
        else:
            pass

    print(f'#{test_case}')
    for word, repeat in ali_planet.items():
        for _ in range(repeat):
            print(word, end=' ')
    print()
