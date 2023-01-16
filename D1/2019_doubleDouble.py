# print number multiplied by 2 from 1 to the given number of times.
T = int(input())

answer = ''
result = 1
for num in range(T+1):
    answer = answer + str(result) + ' '
    result *= 2

print(answer)