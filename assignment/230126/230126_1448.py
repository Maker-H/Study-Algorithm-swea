def highest_price(grain_lst):
    grain_lst = sorted(grain_lst, key = lambda x: x[1], reverse=True)
    return grain_lst[0][0]



grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
print(highest_price(grain_lst))