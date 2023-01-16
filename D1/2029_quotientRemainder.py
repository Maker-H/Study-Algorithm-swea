# Print the quotient and remainder when a is divided by b.

T = int(input())

for test_case in range(T):
    point, compare = input().split()
    
    point = int(point)
    compare = int(compare)

    quotient = point // compare
    remainder = point % compare

    print(f'#{test_case+1} {quotient} {remainder}')
