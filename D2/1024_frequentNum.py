# Print the most frequent number

T = int(input())


for test_case in range(T):
    #start one test case
    case = input()
    scores = [0 for i in range(101)]
    students = list(input().split())
  
    for score in students:
        score = int(score)
        scores[score] += 1

    max = 0
    answer = 0
    for index in range(len(scores)):
        if max <= scores[index]:
            max = scores[index]
            answer = index

    print(f'#{case} {answer}')
