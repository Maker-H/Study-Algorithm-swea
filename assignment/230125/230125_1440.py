import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list

def winning_card_1_is_p1_win(p1, p2):
    # 카드 숫자부터 비교
    
    is_number_same = False
    if p1[1] == p2[1]:
        is_number_same = True
    elif p1[1] != p2[1]:
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J']
        if numbers.index(p1[1]) > numbers.index(p2[1]):
            return 1
        elif numbers.index(p1[1]) < numbers.index(p2[1]):
            return 2

    # 문양 비교
    if is_number_same:
        shape = ["clover", "heart", "diamond", "spade"] 
        if numbers.index(p1[0]) > numbers.index(p2[0]):
            return 1
        elif numbers.index(p1[0]) < numbers.index(p2[0]):
            return 2

    else: 
        return 0

trump_card_list = making_card_list()
winning_player = ''
win_cnt = 0
win_p1 = 0
win_p2 = 0


while True:
    p1 = random.choice(trump_card_list)
    trump_card_list.remove(p1)
    p2 = random.choice(trump_card_list)
    result = winning_card_1_is_p1_win(p1, p2)
    if result == 1:
        winning_player = 'player1 win'
        win_cnt += 1
        win_p1 += 1 
    elif result == 2:
        winning_player = 'player2 win'
        win_cnt += 1
        win_p2 += 1 
    elif result == 0:
        pass
    print(f'{p1} {p2} {winning_player}')
    if win_p1 == 6 or win_p2 == 6:
        break

final_win = ''
if win_p1 > win_p2:
    final_win = 'Finally player1 win'
elif win_p1 < win_p2:
    final_win = 'Finally player2 win'

print(f'{win_p1}:{win_p2} {final_win}')