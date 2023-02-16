def game(a, b):
    if card[a] == 2 and card[a] > card[b]:
        return a
    elif card[a] == card[b]:
        return a if a < b else b
    elif card[b] == 2 and card[b] > card[a]:
        return b
    elif card[a] == 3 and card[b] == 1:
        return b
    elif card[a] == 3 and card[b] == 2:
        return a
    elif card[b] == 3 and card[a] == 1:
        return a
    elif card[b] == 3 and card[a] == 2:
        return b


def re(s, e):
    if s == e:
        return s
    elif e-s == 1:
        return game(s, e)
    else:
        return game(re(s, (s+e)//2), re((s+e)//2 + 1, e))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{tc} {re(0, N-1)+1}')