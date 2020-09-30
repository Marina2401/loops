#2. Дана прямоугольная матрица A[N, N].
# Переставить первый и последний столбцы местами и вывести на экран.
import random
n = int(input('Введите порядок матрицы '))
print('Исходная матрица: ')
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(random.randint(0, 9))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print('Поменяли первый и последний столбец местами:')
for i in range(n):
    a[i][0], a[i][n-1] = a[i][n-1], a[i][0]
    print(a[i])

