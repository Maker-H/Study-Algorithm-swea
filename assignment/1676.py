# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

menu = 50000
vat = menu * 0.15
total = vat + menu

print(f'스테이크 {menu:>9,}')
print(f'+ VAT {vat:>10,}')
print(f'총계 ₩ {total:>10,}')
