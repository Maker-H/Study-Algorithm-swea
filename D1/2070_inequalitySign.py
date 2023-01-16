# Receives two numbers, compares their sizes, and prints an equal or inequality sign

T = int(input())

for test_case in range(1, T + 1):
	nums = input().split()
	phrase = '#' + str(test_case)

	a = int(nums[0])
	b = int(nums[1])
	if a < b:
		print(phrase ,'<')
	elif a == b:
		print(phrase, '=')
	elif a > b:
		print(phrase, '>')