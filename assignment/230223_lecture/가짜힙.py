def min_value(tmp):
    min_idx = 0
    for i in range(len(tmp)):
        if tmp[min_idx] > tmp [i]:
            min_idx = i
        rst = tmp[min_idx]
    tmp[min_idx] = 99
    return tmp[min_idx]

tmp = [7, 2, 5, 3, 4, 6]
min_idx = 0
for i in range(len(tmp)):
    print(tmp(min_value(tmp)) , end='')

print()