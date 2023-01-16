T = int(input())

answer = ''
for num in range(T, -1, -1):
    answer = answer + str(num) + ' '

print(answer)