# When scores array are given as input, print the median


T = int(input())
nums = input().split()

max = 0
for repeat in range(len(nums) - 1, 0, -1):
    for innerIndex in range(repeat):
        n1 = int(nums[innerIndex])
        n2 = int(nums[innerIndex + 1])

        if n1 < n2:
            tmp = nums[innerIndex + 1]
            nums[innerIndex + 1] = nums[innerIndex]
            nums[innerIndex] = tmp

print(nums[T // 2])