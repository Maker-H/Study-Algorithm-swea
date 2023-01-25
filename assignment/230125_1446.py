# fn_d(91) 
# 출력 예시 
# 101

def fn_d(origin):
    num_sum = 0
    N = origin
    while True:
        num_sum += N % 10
        N = N // 10
        if N == 0:
            break
    return num_sum + origin 

def is_selfnumber(N):
    for i in range(N):
        if fn_d(i) == N:
            return False
        else:
            pass
    return True

    
