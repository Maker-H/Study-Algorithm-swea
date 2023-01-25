# N is the amount of money to be returned to the customer
# Print how many of each type of money are needed to return the minimum number of change.

money = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cost = N
    for change in money.keys():
        change_num = cost // change
        money[change] = change_num
        cost = cost - (change * change_num)

    answer = ''
    for ch in money.values():
        answer = answer + str(ch)+ ' '
    print(f'#{test_case}')
    print(answer)
