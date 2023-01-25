# N is given in the first line of each test case.
# The next N lines give an N x N matrix.
# Print a array rotated by 90 degrees, 180 degrees, and 270 degrees.
# The output has space between the rotated shapes.

# rotate 90 degrees 
def rotate(N, before_rotate):
    rotate_arr = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            rotate_arr[x][y] = before_rotate[N-1-y][x]
    return rotate_arr

# store arr element as test format
def new_format_arr(answer, row_idx, N, rotated_arr):
    one_row = ''
    for x in range(N):
        for y in range(N):
            one_row += str(rotated_arr[x][y])
        answer[x][row_idx] = one_row
        one_row = ''
    return answer

# fill in the inputs in default arr
def fill_in(default_arr, tmp_inputs, cnt):
    for idx in range(len(tmp_inputs)):
        default_arr[cnt][idx] = tmp_inputs[idx]

    return default_arr

# print arr prettier
def print_arr(N, answer):
    row = ''
    for x in range(N):
        for y in range(3):
           row = row + str(answer[x][y]) + ' '
        print(row)
        row =''


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    default_arr = [[0 for _ in range(N)] for _ in range(N)]
    
    cnt = 0
    for repeat in range(N):
        tmp_inputs = list(map(int, input().split()))
        default_arr = fill_in(default_arr, tmp_inputs, cnt)
        cnt += 1

    rotated_arr = default_arr
    answer = [[0 for _ in range(N)] for _ in range(N)]
    for repeat in range(3):
        rotated_arr = rotate(N, rotated_arr)
        answer = new_format_arr(answer, repeat, N, rotated_arr)
   
    print(f'#{test_case}')
    print_arr(N, answer)
    