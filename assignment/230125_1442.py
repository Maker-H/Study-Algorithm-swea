# 입력 예시
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'

answer = ''
isMiddle = False
isEnd = False
for c in s:
    if not isMiddle and c.isalpha():
        answer += c
        isMiddle = True

    elif isMiddle:
        answer += c.lower()
        
        if c == '.':
            break
    

print(answer)