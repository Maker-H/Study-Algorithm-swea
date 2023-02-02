import  sys

def count_station(charge_run, stations):
    # 버스 출발
    charge_cnt = 0
    prev_charge_station = 0
    double_prev_charge_station = 0
    triple_prev_charge_station = 0
    end_point = len(stations) - 1

    for current_station in range(1, len(stations)):

        # 정류장 만나면 충전부터 한다
        if stations[current_station] == 1:
            charge_cnt += 1

        # 종점이면
        elif current_station == end_point:

            # 이전 이전 정류장에서 종점을 올 수 있으면 그 이전 정류장에 설 이유가 없다
            if current_station - double_prev_charge_station <= charge_run:
                charge_cnt -= 1
                return charge_cnt
            else:
                return charge_cnt


            # TODO : 이전 정류장에서 못오면 어떻게 해야될까
            if current_station - prev_charge_station >= charge_run:
                return 0
            # 이전 정류장에서 올 수 있으면
            else:


        else:
            # 충전소 아니면 지나친다
            continue


        # 바로 이전 충전했던 정류장에서 도착할 수 있는지 확인한다
        if prev_charge_station != 0:
            # 도착할 수 있으면 여기 정류장에서 충전하자
            if current_station - prev_charge_station <= charge_run:
                pass
            # 도착 못하면 여기서 충전해야 한다
            else:
                return 0

        # 바로 이전 정류장에서 충전하지 않아도 이전이전 정류장에서 도착할 수 있는지 확인한다
        if prev_charge_station != 0:
            # 도착할 수 있으면 그 이전에서 충전하지 않아도 되었음으로 -1
            if current_station - double_prev_charge_station <= charge_run:
                charge_cnt -= 1
                prev_charge_station = current_station

            # 이전 정류장과 그 이전 정류장 수정해줘야 한다.
            # 도착못하면 그 이전 정류장 정류장에서 충전하고 도착해야 한다
            else:
                double_prev_charge_station = prev_charge_station
                prev_charge_station = current_station
        # 바로 이전 정류장에서 충전하고 도착해야 한다
        else:
            double_prev_charge_station = prev_charge_station
            prev_charge_station = current_station






sys.stdin = open('L2_electric_bus.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    charge_run, end_point, charger_num = tuple(map(int, input().split()))

    charger_stations = list(map(int, input().split()))

    #충전소 어디있는지 정류장 만들기
    stations = [0 for _ in range(end_point+1)]
    for charger_station in charger_stations:
        stations[charger_station] += 1

    print(f'#{test_case} {count_station(charge_run, stations)}')

