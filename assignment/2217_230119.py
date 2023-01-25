words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

count = 0
while count != (len(words)-1):
    if words[count][-1] ==  words[count + 1][0]:
        count += 1
    else:
        print(count)
        break

# Professor
for idx in range(len(words)-1):
	if words[idx][-1] != words[idx+1][0] or words[i] in words[:idx]:
		print(f'{i+1}번째 탈락자가 탈락하였습니다')
		break
else:
	print('축하합니다. 아무도 탈락하지 않으셨습니다.')

for idx in range(len(words)-1):
	if words[idx][-1] != words[idx+1][0] or words[i] in words[:idx]:
		flag = False
		print(f'{i+1}번째 탈락자가 탈락하였습니다')
		break
if flag:
	print('축하합니다. 아무도 탈락하지 않으셨습니다.')