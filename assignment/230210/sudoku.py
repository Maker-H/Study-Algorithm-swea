T = int(input())

for test_case in range(1, T+1):
    sudoku = [input().split() for _ in range(9)]

    isdouble = False
    for f in range(9):
        verify_row = [0 for _ in range(9)]
        verify_col = [0 for _ in range(9)]

        for s in range(9):
            verify_row[s] = sudoku[f][s]
            verify_col[s] = sudoku[s][f]
        if len(set(verify_row)) != 9 or len(set(verify_col)) != 9:
            isdouble = True

    for f in range(0, 9, 3):
        for s in range(0, 9, 3):
            box = [0 for _ in range(9)]
            box_idx = 0
            for df in range(f, f+3):
                for ds in range(s, s+3):
                    box[box_idx] = sudoku[df][ds]
                    box_idx += 1
            if len(set(box)) != 9:
                isdouble = True

    if isdouble:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')
