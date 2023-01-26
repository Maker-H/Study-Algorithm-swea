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