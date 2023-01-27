# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

def group_anagrams(user_inputs):
    answer = {}
    for user_input in user_inputs:
        sorted_tmp = "".join(sorted(user_input))
        
        if sorted_tmp not in answer:
            answer[sorted_tmp] = [user_input]
        elif sorted_tmp in answer:
            answer[sorted_tmp].append(sorted_tmp)
    
    return list(answer.values())

user_inputs = ['eat','tea','tan','ate','nat','bat']
print(group_anagrams(user_inputs))



#professor
def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        # 1
        anagrams.setdefault(key, [])
        anagrams[key].append(word)

        # 2
        if not anagrams.get(key):
            anagrams[key] = []
        anagrams[key].append(word)
