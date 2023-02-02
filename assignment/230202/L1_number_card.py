import sys

sys.stdin = open('L1_number_card.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    card_num = int(input())
    sorted_cards = [0 for _ in range(10)]

    cards = int(input())

    while cards != 0:
        sorted_cards[cards % 10] += 1
        cards = cards // 10

    hightest_card_num = -1
    highest_card_val = -1
    max = -1

    for card_idx in range(len(sorted_cards)):
        max_tmp = sorted_cards[card_idx]

        if max_tmp >= max:
            max = max_tmp
            hightest_card_num = sorted_cards[card_idx]
            highest_card_val = card_idx


    print(f'#{test_case} {highest_card_val} {hightest_card_num}')
