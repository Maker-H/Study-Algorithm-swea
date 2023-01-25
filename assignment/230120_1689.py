# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

S = input().split()

answer = []
earlier = 0
for num in S:
    num = int(num)

    if num != earlier:
        answer.append(num)
        earlier = num
    elif num == earlier:
        pass

print(answer)