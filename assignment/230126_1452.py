# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

def salt_amout(density, salt_water):
    return salt_water * density * 0.01

def get_water_and_salt(input_str):
    salt, water = input_str.split()
    
    tmp_idx = 0
    for idx in range(len(salt)):
        if salt[idx] == '%':
            tmp_idx = idx
        else:
            tmp_idx = len(salt)
    salt = salt[:tmp_idx]

    for idx in range(len(water)):
        if water[idx] == 'g':
            tmp_idx = idx
        else:
            tmp_idx = len(water)
    water = int(water[:tmp_idx])

    return int(salt), int(water)



is_done = False
cnt = 1
total_salt = 0
total_water = 0
density, water = get_water_and_salt(input(f'#{cnt} 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: '))

while not is_done:
    total_salt += salt_amout(density, water)
    total_water += water
    user_input = input(f'#{cnt} 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
    cnt += 1
    if cnt == 5: 
        break
    if user_input == 'DONE':
        break

total_density = round(total_salt / total_water * 100, 2)

print(f'{total_density}% {total_water}g')

    
    


