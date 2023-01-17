orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

ice_orders = []
orders = orders.split(',')
for order in orders:
    if order[:3] == '아이스':
        ice_orders.append(order)

print(len(ice_orders))



menu = {}

for order in orders:
    if order in menu:
        menu[order] += 1
    else:
        menu[order] = 1
         

print(menu)