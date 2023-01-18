# Original text is compromised with width 10 text
# The text which compressed original has alphabet and the number of alphabet on it 
# ex)A 5 -> AAAAAA
# Get info of compressed text and convert it to original

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    text = []
    # Start reading condition and make text
    for line in range(N):
        alphabet, alpha_repeat = input().split()
        alpha_repeat = int(alpha_repeat)

        # Add alphabet in list for n(alpha_repeat) times
        for add_a in range(alpha_repeat):
            text.append(alphabet)

    if len(text) % 10 == 0 :
        text_line = (len(text) // 10)
    elif len(text) % 10 != 0:
        text_line = (len(text) // 10) + 1

    # Print eachline
    first_slice = 0
    last_slice = 10
    print(f'#{test_case}')
    for line in range(text_line):
        tmp_text = text[first_slice:last_slice]
        print(''.join(tmp_text))
        first_slice += 10
        last_slice += 10
        
