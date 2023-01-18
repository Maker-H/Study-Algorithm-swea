answer = 0
water_total = 0
salt_total = 0
count = 0
isAnswer = False

while True:
    if count == 5:
        break

    inputs = []
    inputs = input("농도와 소금물의 양을 띄워서 입력해주세요").split()


    
    if inputs[-1] == 'DONE':
        isAnswer = True
        break
    else:
        salt_water, density  = tuple(map(int, inputs))
        count +=1
    
    water_total += salt_water
    salt_total += (density/100) * salt_water



if isAnswer:
    print(salt_total)
    answer = (salt_total/water_total) * 100
    print(answer)
    print(f'농도 :{round(answer, 2)} 양 : {water_total}')
    



