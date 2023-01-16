# If the amount of water used per month is 'W', choose a company with a lower rate and print the rate.

T = int(input())
for test_case in range(T):
    a_price, b_defaultPrice, b_poit, b_literPrice, waterLiter = input().split()
    
    a_price = int(a_price)
    b_defaultPrice = int(b_defaultPrice)
    b_poit = int(b_poit)
    b_literPrice = int(b_literPrice)
    waterLiter = int(waterLiter)

    B = 0
    A = a_price * waterLiter
    
    if b_poit >= waterLiter:
        B = b_defaultPrice
    else:
        B = b_defaultPrice + (waterLiter - b_poit) * b_literPrice

    answer = 0
    if A <= B:
        answer = A
    else:
        answer = B

    print(f'#{test_case+1} {answer}')