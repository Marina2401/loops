# coding=utf-8
#Требуется найти сумму

import random
from aetypes import end

n = int(input('Введите порядок матрицы '))
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(random.randint(-10, 10))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print()
