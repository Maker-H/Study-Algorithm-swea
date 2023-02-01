# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(user_input):
    user_input = user_input.replace('-','')
    birth_date = user_input[:6]
    back_num = user_input[6:]
    
    cover = '*' * len(back_num)
    
    return birth_date + cover




print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))