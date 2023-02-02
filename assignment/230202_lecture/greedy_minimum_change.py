C = int(input())

money_units = [50000, 40000, 10000, 5000, 1000, 500, 100, 50, 10]
changes_num = [0 for _ in range(8)]

cal_user_input = C
cal_total_changes = 0
units_idx = 0

while True:
    tmp = money_units[units_idx]

    # 일단 거스름돈에 저장
    # 만약 거스름돈 처음 저장하면
    if changes_num[units_idx] == 0:
        changes_num[units_idx] = 1

    # 만약 거스름돈 첫번째 저장하는거 아니면
    elif changes_num[units_idx] != 0:
        changes_num[units_idx] += 1


    # 만약에 거스름돈이 계산한 cal_user_input보다 작으면 추가
    if tmp <= cal_user_input :
        cal_total_changes += tmp
        cal_user_input -= tmp

    # 거스름돈이 user_input보다 크면 추가했던거 빼주고 작은 단위 시작
    elif tmp > cal_user_input:
        if changes_num != 0:
            changes_num[units_idx] -= 1
        elif changes_num[units_idx] == 0:
            changes_num[units_idx] = 0

    # 만약 총 거스름돈이 C보다 모자라면 작은단위 시작 or 거스름돈 더 할 수 있음
    if cal_total_changes < C:
        # 뺀 값이 거스름돈 보다 크면 다시 거스름돈 한 번 더 추가해준다
        if C - cal_total_changes >= tmp:
            continue
        else:
            pass
    elif cal_total_changes >= C:
        break


    units_idx += 1

print(changes_num)





