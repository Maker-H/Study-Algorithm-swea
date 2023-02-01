orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

converted_orders = list(orders.split(','))

print(len(converted_orders))
converted_orders = set(converted_orders)
converted_orders = list(converted_orders)


converted_orders.sort(reverse=True)


print(converted_orders)