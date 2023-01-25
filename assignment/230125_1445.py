# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar

date = {'년': 0, '월': 0, '일': 0, '요일': ''}
days_of_week = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}

my_year = int(input())

while True:
    if calendar.isleap(my_year):
        my_year = int(input())
    else: 
        break

text_cal = calendar.TextCalendar()
print(text_cal.formatyear(my_year))

date_keys = list(date.keys())
date_keys.pop()

for key in date_keys:
    date[key] = int(input())

day_of_week = calendar.weekday(date.get('년'), date.get('월'), date.get('일')) 
if day_of_week == 0:
    print('경고 월요일입니다')

date['요일'] = days_of_week[day_of_week]

print(date)
