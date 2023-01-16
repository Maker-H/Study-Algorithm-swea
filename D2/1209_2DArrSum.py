# Based on a given 2D array of 100X100, find the maximum among the sum of each row, sum of each column, and sum of each diagonal.


arr_size = 3

for test_case in range(10):
    T = int(input())
    originalNums = input().split()
    newNums = [[0 for i in range(arr_size)] for i in range(arr_size)]
    
    f_index = s_index = 0

    #convert str list to int list
    numIndex = 0
    for outer in range(arr_size):
        for inner in range(arr_size):
            newNums[outer][inner] = int(originalNums[numIndex])
            numIndex += 1

    row = column = []

    #calculate row
    sum = 0
    row_sum = []
    for first_i in range(arr_size):
        for second_i in range(arr_size):
            sum += newNums[first_i][second_i]
            # When second_i reaches 99, which is the last arr index, the sum calculated up to that point is stored in row_sum.
            # initialize the sum
            if second_i%99 == 0:
                row_sum.append(sum)
                sum = 0    

    #calculate column
    sum = 0
    column_sum = []
    for second_i in range(arr_size):
        for first_i in range(arr_size):
            sum += newNums[first_i][second_i]
            # When first_i reaches 99, which is the last arr index, the sum calculated up to that point is stored in colum_Sum.
            # initialize the sum
            if first_i%99 == 0:
                column_sum.append(sum)
                sum = 0  


    #calculate diagonal
    d1_sum = 0
    d2_sum = 0
    diagonal_sum = []
    for index in range(arr_size):
            d1_sum += newNums[index][index]
            d2_sum += newNums[index][(arr_size-1)-index]
            # When second_i reaches 99, which is the last arr index, the sum calculated up to that point is stored in rowSum.
            # initialize the sum
            if index == 99:
                diagonal_sum.append(d1_sum)
                diagonal_sum.append(d2_sum)
                sum = 0  

                
    answer = []
    answer.extend(d1_sum).extend(d2_sum).extend(row_sum).extend(column_sum)
    print(f'#{T} {max(answer)}')
