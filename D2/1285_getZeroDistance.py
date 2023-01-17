# People stand where the number 100,000 is written and try to throw a stone as close to zero as possible.
# Numbers range is from -100,000 to 100,000
# Print an integer number, separated by a single space, indicating the difference in distance between the point where the stone landed closest to zero and the number of people who threw it that way.

T = int(input())

for test_case in range(T):
    
    people_num = input()
    scores = input().split()
    
    zeroBase_scores = []
    for score in scores:
        score = int(score)

        if score < 0:
            score = -score
        
        zeroBase_scores.append(score)
    
    max = max(zeroBase_scores)
    count = 0
    #count the number of person whoes score is max
    for score in zeroBase_scores:
        if score == max:
            count += 1
    
    #print answer
    print(f'#{test_case+1} {max} {count}')

