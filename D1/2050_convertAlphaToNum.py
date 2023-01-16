# Receive a string of alphabets and convert each alphabet to a number from 1 to 26 and print it.

phrase = list(input())

upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

answer = ''

for alpha in phrase:
    for num in range(0, len(upper)+1):
        if upper[num] == alpha:
            answer = answer+ str(num+1) + ' '
            break

print(answer)