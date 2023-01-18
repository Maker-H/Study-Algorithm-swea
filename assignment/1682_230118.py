infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

sum_val = 0
for info in infos:
    sum_val += info.get('age')

print(sum_val)