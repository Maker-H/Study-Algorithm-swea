from collections import Counter

def using_for(user_input):
    answer = 0
    for c in str(user_input):
        answer += int(c)
    return answer

def not_using_for(user_input):
    c = Counter(str(user_input))
    return sum(list(map(int, list(c.keys()))))

# sum_of_digit(3904) # 16
print(not_using_for(3904))
print(using_for(3904))
