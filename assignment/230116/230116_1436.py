arr = []

index = 0
for num in range(10):
    if num%2 == 0  or num%7 == 0:
        arr.append(num)
        index += 1

no_double = set(arr)
no_double_answer = list(no_double)

print(sum(no_double_answer))