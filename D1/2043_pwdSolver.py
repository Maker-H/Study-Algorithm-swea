# Increases by 1 from the given number K to confirms the password

endLine, start = input().split()

endLine = int(endLine)
start = int(start)

count = 0
hasAnswer = False

for num in range(start, 1000):
    count += 1      
    if num == endLine:
        hasAnswer = True
        break
        

if hasAnswer == False:
    for num in range(0, start):
        count += 1
        if num == endLine:
            break

print(count)
