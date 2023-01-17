T = int(input())

for test_case in range(1, T+1):
    num = int(input())

    isStillRunning = True
    zeroToNine = [num]
    count = 0
    #check if zeroToNine has all number in range 0~9
    while True:
        zeroToNine.append(num)
        zeroToNine = set(zeroToNine)
        zeroToNine = sorted(zeroToNine)
        zeroToNine = str(zeroToNine)
        
        num *= 2
        count += 1

        if zeroToNine == '0123456789':
            break
        
    print(f'#{test_case} {count}')
    

