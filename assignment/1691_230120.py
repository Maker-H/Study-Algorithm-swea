test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

# cheating인 사람 기존 dic에서 제거하고 따로 리스트 만들어서 오름차순으로 출력
# sleeping 의 상태를 모두 solving으로 변경

cheet_students = []
students = list(test_status.items())

for student in students:
    name = student[0]
    status = student[1] 
    
    if status == 'cheating':
        tmp = {name:status}
        cheet_students.append(tmp)
        del test_status[name]
    elif status == 'sleeping':
        test_status[name] = 'solving'
        
print(cheet_students)
print(sorted(test_status.items(), key = lambda item:item[0]))