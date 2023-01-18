blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_info = {}
for type in blood_types:
    if type not in blood_info:
        blood_info[type] = 1
    elif type in blood_info:
        blood_info[type] += 1

print(blood_info) 