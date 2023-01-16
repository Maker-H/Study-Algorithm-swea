# Receives 10 numbers as input, and print the value obtained by adding only odd numbers

T = int(input())

for test_case in range(1, T + 1):
	sum = 0
    #10개
	nums = input().split(' ')

	for num in  nums:
		if int(num)%2 == 1:
			sum = int(num) + sum
	phrase = '#' + str(test_case)
	print(phrase, sum)    