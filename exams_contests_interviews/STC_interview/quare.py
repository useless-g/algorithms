"""
Дана последовательность чисел - арифметическая прогрессия.
Из неё вынули два числа и перемешали последовательность.
Найти эти 2 числа.

"""


import random

a = [i for i in range(1, 100 + 1)]
n = len(a)
print(a)
b = [i for i in range(1, 100 + 1)]
random.shuffle(b)
b.pop()
b.pop()
print(b)

z1 = (n + 1) * n // 2
print("Сумма арифметической прогрессии = ", z1)

z2 = n*(n+1)*(2*n+1)//6
print("Полная сумма квадратов = ", z2)

z3 = sum(b)
print("Частичная сумма = ", z3)

z4 = 0
for i in b:
    z4 += i*i
print("Частичная сумма квадратов = ", z4)

z1 = z1 - z3  # первое свободное значение = полная сумма - частичная сумма
z2 = z2 - z4  # второе свободное значение = полная сумма квадратов - частичная сумма квадратов
print('z1,z2 =', z1, z2)


"""
x+y=z1
x^2+y^2=z2
x=z1-y
(z1-y)^2 + y^2 = z2
z1^2 - 2z1y + 2y^2 - z2 = 0
2y^2 - 2z1y + z1^2-z2 = 0
"""
D = (2*z1)**2 - 4*2*(z1**2-z2)
print(D)
y1 = (2*z1 + D**(1/2))//4
y2 = (2*z1 - D**(1/2))//4
x1 = z1 - y1
x2 = z1 - y2
print("y1,y2", int(y1), int(y2))
print("x1,x2", int(x1), int(x2))
x1 = int(x1)
x2 = int(x2)
x, y = min(x1,x2), max(x1,x2)
print("Smart answer is: ", x, y)

print("Dumb answer is:", end=' ')
for i in a:
    if i not in b:
        print(i, end=' ')