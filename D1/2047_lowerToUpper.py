# Finds all lowercase letters in the sentence given as input, converts them to uppercase letters, and prints the result.

phrase = list(input())

answer =''

for alpha in phrase:
    if alpha != '-': 
        answer = answer + str(alpha.upper())
    elif alpha == '-':
        answer = answer + '-'
print(answer) 
