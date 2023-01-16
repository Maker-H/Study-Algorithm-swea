# Calculate the sum of each digit

T = int(input())

isEnd = True
sum = 0
while isEnd:
    
    sum = sum + T % 10
    T = T // 10

    if T == 0:
        break

print(sum)