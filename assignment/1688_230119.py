students = [
    '박해피',
    '이영희',
    '조민지',
    '조민지',
    '김철수',
    '이영희',
    '이영희',
    '김해킹',
    '박해피',
    '김철수',
    '한케이',
    '강디티',
    '조민지',
    '박해피',
    '김철수',
    '이영희',
    '박해피',
    '김해킹',
    '박해피',
    '한케이',
    '강디티',
]

student_num = {}

for student in students:
    if student not in student_num:
        student_num[student] = 1
    elif student in student_num:
        student_num[student] += 1 

answer = sorted(student_num.items(), key = lambda x: x[1])

print(answer)

