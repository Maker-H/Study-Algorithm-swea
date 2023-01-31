# professor
import random

class ClassHelper:
    def __init__(self, students):
        self.students = students
    

    def pick(self, n):
        return random.sample(self.students, n)
    
    def match_pair(self):
        random.shuffle(self.students)
        pairs = []
        pair_count = len(self.students) // 2

        for idx in range(pair_count):
            if idx == pair_count - 1:
                pair = self.students[idx*2: ]
                pairs.append(pair)
                return pairs
            
            pair = self.students[idx*2: idx*2+2]
            pairs.append(pair)



ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
