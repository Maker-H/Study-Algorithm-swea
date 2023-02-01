def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    result = 0
    try:
        result = a / b
    except:
        print('0으로는 나눌 수 없습니다')
    
    return a / b