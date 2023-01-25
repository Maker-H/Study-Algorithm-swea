word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

sum_1 = 0
for word in word1:
    sum_1 += ord(word)

sum_2 = 0
for word in word2:
    sum_2 += ord(word)

answer = word1 if sum_1 > sum_2 else word2

print(answer)

