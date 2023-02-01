def count_vowels(user_input):
    cnt = 0
    for char in user_input:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            cnt += 1
    return cnt


print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3
