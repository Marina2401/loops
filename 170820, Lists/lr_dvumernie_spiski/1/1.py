#1. Вычислить сумму и число положительных элементов матрицы A[N, N], находящихся над
# главной диагональю.
import random
n = int(input('Введите размер матрицы '))
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(random.randint(-10, 10))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j], end = '\t')
    print()

count = 0
sum = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i][j] > 0:
            count += 1
            sum = sum + a[i][j]

print(count, sum)


