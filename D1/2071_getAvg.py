# Enter 10 numbers and print the average value

T = int(input())

for test_case in range(1, T + 1):
    nums = input().split(' ')
    
    sum = 0
    for num in nums:
        sum = sum + int(num)
    
    phrase = '#' + str(test_case)
    print(phrase, round(sum/10))