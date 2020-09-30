#4.2. Дана квадратная матрица A[N, N], Записать на место отрицательных элементов матрицы нули,
# а на место положительных — единицы. Вывести на печать нижнюю треугольную матрицу в
# общепринятом виде.

import random
n = int(input('введите порядок матрицы '))
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(random.randint(-10, 10))
    a.append(b)
    
for i in range(n):
    for j in range(n):
        print(a[i][j], end='\t')
    print()

print()
for i in range(n):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        elif a[i][j] > 0:
            a[i][j] = 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end='\t')
    print()

