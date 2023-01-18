fruit_basket = input().split(',')

fresh_fruit_basket = []
for fruit in fruit_basket:
    fruit = fruit.lower()
    fruit = fruit.replace('rotten', '')
    
    fruit = fruit.strip()
    fresh_fruit_basket.append(fruit)

print(fresh_fruit_basket)
