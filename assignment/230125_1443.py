# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

def sum_of_repeat_number(num_list):
    add_list = []
    double_list = []

    for first_idx in range(len(num_list)):
        for second_idx in range(first_idx+1, len(num_list)):
            if num_list[first_idx] == num_list[second_idx]:
                double_list.append(num_list[first_idx])
                break
    
    double_list = list(set(double_list))

    for num in num_list:
        if num not in double_list:
            add_list.append(num)

    return sum(add_list)


num_list = [4, 4, 7, 8, 10, 4]
print(sum_of_repeat_number(num_list))
