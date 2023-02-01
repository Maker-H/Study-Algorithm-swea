import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    size, word_len = tuple(map(int, input().split()))
    word_answer = '1'* word_len
    puzzle = []
    for _ in range(size):
        puzzle.append(input().split())
    end_point = size - word_len
    cnt = 0

    
    for first_idx in range(size):
        tmp = ''
        is_continue_one = False
        is_First = True
        for second_idx in range(size):
            if puzzle[first_idx][second_idx] == '1' and is_First:
                tmp += '1'
                is_continue_one = True
                is_First = False
            elif puzzle[first_idx][second_idx] == '1' and is_continue_one and not is_First:
                tmp += '1'
                is_continue_one = True
                if tmp == word_answer:
                    break
            elif puzzle[first_idx][second_idx] == '0':
                is_continue_one = False
                tmp = ''
        if tmp == word_answer:
            cnt += 1

    for first_idx in range(size):
        is_continue_one = False
        is_First = True
        tmp = ''
        for second_idx in range(size):
            if puzzle[second_idx][first_idx] == '1' and is_First:
                tmp += '1'
                is_continue_one = True
                is_First = False
                print(f'isfirst puzzle[{second_idx}][{first_idx}]')
            elif puzzle[second_idx][first_idx] == '1' and is_continue_one and not is_First:
                tmp += '1'
                is_continue_one = True
                if tmp == word_answer:
                    break
                print(f'not is first puzzle[{second_idx}][{first_idx}]')
            elif puzzle[second_idx][first_idx] == '0':
                is_continue_one = False
                tmp =''
        print(tmp)
        if tmp == word_answer:
            cnt += 1
    
    print(f'#{test_case} {cnt}')
    