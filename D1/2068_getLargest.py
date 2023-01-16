# Get 10 numbers as input and print the largest number among them.

T = int(input())

for test_case in range(1, T + 1):
    phrase = '#' + str(test_case)
    nums = input().split()
    
    max = int(nums[0])

    index = 1
    while index < len(nums):
        num = int(nums[index])
        index += 1
        if max < num:
            max = num

    print(phrase, max)
    