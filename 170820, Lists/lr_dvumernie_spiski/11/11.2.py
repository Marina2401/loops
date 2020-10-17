#11.2 Среди столбцов заданной целочисленной матрицы, содержащих только такие элементы, которые по модулю не
# больше 10, найти столбец с минимальным произведением элементов и поменять местами с соседним.

import random

def pr(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

def column(a, n):
    d = []
    for j in range(n):
        c = []
        p = 1
        for i in range(n):
            p = p * a[i][j]
        c.append(p)
        d.append(c)
    return d

def min_incolumn(a, n):
    c = column(a, n)
    min = c[0]
    l = 0
    for i in range(1, len(c)):
        if c[i] < min:
            min = c[i]
            l = i
    return l

def main():
    n = int(input('Введите порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(1, 9))
        a.append(b)

    pr(a, n)
    c1 = column(a, n)
    print(c1)

    mic = min_incolumn(a, n)
    print(mic)

    if mic == 0:
        for i in range(n-1):
            a[i][0], a[i][1] = a[i][1], a[i][0]
    elif mic == n-1:
        for i in range(n):
            a[i][n-2], a[i][n-1] = a[i][n-1], a[i][n-2]

    else:
        for i in range(n):
            a[i][mic-1], a[i][mic] = a[i][mic], a[i][mic-1]

    pr(a, n)

main()