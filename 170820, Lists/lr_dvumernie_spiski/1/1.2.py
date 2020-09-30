#1.2. Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный элементы
# и поменять их с первым и последним элементами строки соответственно.


import random
n = int(input('Введите длину матрицы '))
m = int(input('Введите высоту матрицы '))
a = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(random.randint(-10, 10))
    a.append(b)

for i in range(m):
    for j in range(n):
        print(a[i][j], end='\t')
    print()

for i in range(m):
    maximum = a[i][0]
    minimum = a[i][0]
    j_max = 0
    j_min = 0
    for j in range(n):
        if a[i][j] > maximum:
            maximum = a[i][j]
            j_max = j
        if a[i][j] < minimum:
            minimum = a[i][j]
            j_min = j
    a[i][j_max], a[i][0] = a[i][0], maximum
    a[i][j_min], a[i][n-1] = a[i][n-1], minimum

print()
for i in range(m):
    for j in range(n):
        print(a[i][j], end='\t')
    print()




