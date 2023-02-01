def hanoi(num_len, *k):
    tower = []
    for one in k:
        tower.append(one)
    
    sort_tower = []

    sort_convert = 0
    tower_convert = 0

    if len(sort_tower) == 0:
        pass
    else:
        sort_convert = ord(sort_tower[-1])

    if len(tower) == 0:
        pass
    else:
        tower_convert = ord(tower[-1])

    if sort_convert > tower_convert:
        


# 예시 
#TODO : 하노이
hanoi(3, 'A', 'C', 'B')

# A번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 2번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 3번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 2번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 C번 기둥에 옮긴다.
