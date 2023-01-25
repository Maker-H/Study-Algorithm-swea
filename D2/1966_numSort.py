# Sort the given string of numbers of length N in ascending order

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    decline = N-1
    for repeat in range(N):
        for idx in range(decline):
            if nums[idx] > nums[idx+1]:
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]

        decline -= 1
    
    answer = ''
    for num in nums:
        answer = answer + str(num) +' '
    print(f'#{test_case} {answer}')
