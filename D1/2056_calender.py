# An 8-digit date is given as input
# If date is valid print in ”YYYY/MM/DD” format,
# If the date is not valid, print -1

T = int(input())

correctDate = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for count in range(T):
    origin = input()
    phrase = int(origin)
    year = phrase // 10000
    date = phrase % 100
    month = (phrase % 10000) // 100
    flag = False

    for monthTmp in range(1, len(correctDate), 1):
        if monthTmp == month and date <= correctDate[monthTmp]:
            flag = True
    if flag:
        print(f'#{count+1} {origin[0:4]}/{origin[4:6]}/{origin[6:8]}') 
    else:
        print(f'#{count+1} -1')
        
            