#9.1. Для целочисленной квадратной матрицы найти число элементов, кратных k,
# и наибольший из этих элементов.

import random
n = int(input('Введите порядок матрицы '))
k = int(input('Введите число k '))
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(random.randint(1, 10))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j], end='\t')
    print()

count = 0
for i in range(n):
    for j in range(n):
        if a[i][j] % k == 0:
            count += 1

ma = 1
for i in range(n):
    for j in range(n):
        if a[i][j] % k == 0 and a[i][j] > ma:
            ma = a[i][j]

print(f'Число элементов, кратных {k}, {count}')
print()
print(f'Максимальное из них {ma}')
