# Count the amount that is a multiple of N
# At least how many times i have to count to see all the digits from 0 to 9 in each digit of the previously counted numbers?
T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    origin_num = num
    zeroToNine = []
    is_not_enough = True
    count = 1
    multiple = 2
    #check if zeroToNine has all number in range 0~9
    while is_not_enough:
        
        
        # Divides the number in units(1's digit)
        is_more_then_onedigit = True
        tmp_num = num
        
        while is_more_then_onedigit:
            
            remainder = tmp_num % 10
            zeroToNine.append(remainder)
            tmp_num = tmp_num // 10

            if tmp_num == 0:
                is_more_then_onedigit = False


        zeroToNine = set(zeroToNine)
        zeroToNine = sorted(list(zeroToNine))
        tmp = ''.join(str(i) for i in zeroToNine)
        print(count, num)
       
        if tmp == '0123456789':
            break
        
        count += 1
        num = origin_num * multiple
        multiple += 1
        
    print(f'#{test_case} {num}')
    

