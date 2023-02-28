def make_bin(tmp):


T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split())
    scanner = []
    codes = []

    for _ in range(N):
        tmp = input().strip('0')

        if not tmp:
            pass
        else:
            # 16진수를 2진수로 만들어서 codes에 넣는다 int로 반환
            codes.append(make_bin(tmp))





