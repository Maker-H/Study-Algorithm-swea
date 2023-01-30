# Receives two input times consisting of hours and minutes.h_sum
# Print the sum of them as hours and minutes

import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    h1, m1, h2, m2 = tuple(map(int,input().split()))

    h_sum = h1 + h2
    m_sum = m1 + m2

    h_sum = h_sum + (m_sum // 60)
    m_sum = m_sum % 60

    
    h_sum = h_sum % 12

    if h_sum == 0:
        h_sum = 12
    print(f'#{test_case} {h_sum} {m_sum}')



