words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

count = 0
while count != (len(words)-1):
    if words[count][-1] ==  words[count + 1][0]:
        count += 1
    else:
        print(count)
        break
    
    