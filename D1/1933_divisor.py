# An integer N is given as input
# Print all divisors of an integer N in ascending order

T = int(input())
answer = ''
for num in range(1, T+1):
    if T % num == 0:
        answer = answer + str(num) + ' '

print(answer)