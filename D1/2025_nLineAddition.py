# print the sum of all numbers from 1 to the given number. 

T = int(input())
sum = 0
for num in range(1, T+1):
    sum += num
print(sum)