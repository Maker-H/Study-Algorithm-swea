def row_nodouble_true(sudoku):
    pass

def column_nodouble_true(sudoku):
    pass

def block_nodouble_ture(sudoku):
    pass

T = int(input())
for test_case in (1, T+1):
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    for first in range(9):
        tmp = list(map(int, input().split()))
        for second in range(9):
            sudoku[first][second] = tmp[second]
    
    if row_nodouble_true(sudoku) and column_nodouble_true(sudoku) and block_nodouble_ture(sudoku):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')



