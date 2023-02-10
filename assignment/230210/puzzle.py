import sys
sys.stdin = open('puzzle.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    puzzle_size, word_len = tuple(map(int, input().split()))
    puzzle = [input().split() for _ in range(puzzle_size)]


    cnt = 0
    for f in range(puzzle_size):
        col_tmp = word_len
        row_tmp = word_len
        for s in range(puzzle_size):
            if puzzle[f][s] == '1':
                row_tmp -= 1
            elif puzzle[f][s] == '0':
                if row_tmp == 0:
                    cnt += 1
                row_tmp = word_len


            if puzzle[s][f] == '1':
                col_tmp -= 1
            elif puzzle[s][f] == '0':
                if col_tmp == 0:
                    cnt += 1
                col_tmp = word_len

        if row_tmp == 0:
            cnt += 1
            row_tmp = word_len
        if col_tmp == 0:
            cnt += 1
            col_tmp = word_len

    print(f'#{test_case} {cnt}')
