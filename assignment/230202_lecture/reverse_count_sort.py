I = [0, 4, 1, 3, 1, 2, 4, 1]
S = [0 for _ in range(len(I))]
C = [0 for _ in range(5)]

for idx in range(len(I)):
    C[I[idx]] += 1

# 누적합 구하기
for idx in range(len(C)-1, ):
    C[idx] = C[idx] + C[idx - 1]

for idx in range(0, range(0, len(I))):
    # counts안의 원소를 인덱스화 (인덱스는 무조건 -1이다)
    C[I[idx]] -= 1
    S[C[I[idx]]] = I[idx]

print(S)
