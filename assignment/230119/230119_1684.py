pwd = ""

isSame = False
count = 0
while isSame == False: 
    if input() == pwd:
        isSame = True
    count += 1
    if count == 3:
        break


