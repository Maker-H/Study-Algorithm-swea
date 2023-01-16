#Scissors is 1, Rock is 2, Paper is 3
#If A wins, print A, and if B wins, print B.

a, b = input().split()

a = int(a)
b = int(b)

result = a - b

if result == 1 or result == -2:
    print('A')
else:
    print('B')

