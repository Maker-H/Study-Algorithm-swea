def recur(s, e):
    if e-s == 1:
        return game(s, e)
    elif s == e:
        return s
    elif s != e:
        return game(recur(s, (s+e) // 2), recur((s+e) // 2 + 1, e))

def game(s, e):
    if card[s] == card[e]:
        return s
    elif card[s] != 3 and card[e] != 3:
        return s if card[s] > card[e] else e

    elif card[e] == 3 and card[s] == 1:
        return s
    elif card[s] == 3 and card[e] == 1:
        return e

    elif card[e] == 3 and card[s] == 2:
        return e
    elif card[s] == 3 and card[e] == 2:
        return s


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    card = list(map(int, input().split()))


    ans = recur(0, N-1)

    print(f'#{test_case} {ans+1}')