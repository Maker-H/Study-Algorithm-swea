participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

answer = participants[:]


for idx in range(len(participants)):
    for inneridx in range(idx+1, len(participants)):
        if participants[idx] == participants[inneridx]:
            answer.remove(participants[idx])
            answer.remove(participants[idx])


print(answer)