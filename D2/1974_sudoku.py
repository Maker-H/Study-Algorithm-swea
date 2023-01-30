# When the numbers of a 9 X 9 Sudoku puzzle are given as input, if there are no overlapping numbers, 
# print 1 as the correct answer, otherwise print 0.

import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input.txt", "r")

def row_nodouble_true(sudoku):
    for first in range(len(sudoku)):
        row_len = len(sudoku[first])
        nodouble_len = len(set(sudoku[first]))


        if row_len != nodouble_len:
            return False
    return True

def column_nodouble_true(sudoku):
    tmp_column = []
    for first in range(len(sudoku)):
        for second in range(len(sudoku)):
            tmp_column.append(sudoku[second][first]) 

        column_len = len(tmp_column)
        nodouble_len = len(set(tmp_column))

        if column_len != nodouble_len:
            return False
        
        tmp_column = []
    return True


def block_nodouble_ture(sudoku):
    position = (0, 0)

    while True:
        is_no_double = one_block_check_double(sudoku=sudoku, position=position)
        
        if is_no_double == False:
            return False

        f_idx, s_idx = position
        if f_idx == 6 and s_idx == 6:
            break
        elif s_idx != 6:
            s_idx += 3
        elif s_idx == 6:
            s_idx = 0
            f_idx += 3

        position = (f_idx, s_idx)

    return True

def one_block_check_double(sudoku, position):
    f_idx , s_idx = position
    one_block = []
    for first in range(f_idx, f_idx+3):
        for second in range(s_idx, s_idx+3):
            one_block.append(sudoku[first][second])
            
    block_len = len(one_block)
    nodouble_len = len(set(one_block))

    if block_len == nodouble_len:
        return True
    elif block_len != nodouble_len:
        return False



T = int(input())

for test_case in range(1, T+1):
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    for first in range(9):
        tmp = list(map(int, input().split()))
        for second in range(9):
            sudoku[first][second] = tmp[second]
    
    if row_nodouble_true(sudoku) and column_nodouble_true(sudoku) and block_nodouble_ture(sudoku):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')



