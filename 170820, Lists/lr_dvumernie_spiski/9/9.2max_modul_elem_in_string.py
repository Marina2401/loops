# coding=utf-8
#9.2. В данной действительной квадратной матрице порядка n найти наибольший по модулю элемент.
# Получить квадратную матрицу порядка n — 1 путем отбрасывания из исходной матрицы строки и столбца,
# на пересечении которых расположен элемент с найденным значением.

import random
from aetypes import end

n = int(input('введите порядок матрицы '))
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(random.randint(-20, 20))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print()


ma = 0
i_ma = 0
j_ma = 0

for i in range(n):
    for j in range(i, n):
        if abs(a[i][j]) > abs(ma):
            ma = a[i][j]
            i_ma = i
            j_ma = j

print(ma, i_ma, j_ma)

for i in range(n):
    a[i].pop(j_ma)
a.pop(i_ma)

for i in range(n - 1):
    for j in range(n - 1):
        print(a[i][j], end='\t')
    print()
print()
