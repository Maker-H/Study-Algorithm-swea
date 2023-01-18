determine_year = int(input())

answer = False
if determine_year % 400 == 0:
    answer = True
elif determine_year % 4 == 0 and determine_year % 100 != 0:
    answer = True

print(answer)