str_input = input('문자열을 입력하세요. : ')

str_input = str_input.upper()

store = []
for idx in range(len(str_input)):
    if str_input[idx] == ' ':
        store.append(idx)

isPass = False
for idx in store:
    if str_input[idx - 1] == str_input[idx + 1]:
        isPass = True
    else:
        isPass = False

if isPass == True:
    print("Pass")
elif isPass == False:
    print("False") 
    
