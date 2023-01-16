s = int(input('숫자를 입력해주세요 : '))

flag = True

answer = 0
while flag :
    remainder = s % 10
    s = s // 10
    answer += remainder 
    
    if s == 0:
        flag = False


print(answer)