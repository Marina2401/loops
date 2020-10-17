#12.2. Дана действительная матрица размером n х m.
# Требуется преобразовать матрицу: поэлементно вычесть последнюю строку из всех строк, кроме последней.

import random

def str(a, m, n):
    p = []
    for i in range(m-1):
        f = []
        for j in range(n):
            a[i][j] = p[i][j] - p[m][j]
            f.append(a)
        p.append(f)

    return p

def main():
    n = int(input('введите количество столбцов '))
    m = int(input('введите количество строк '))
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            b.append(random.randint(0, 10))
        a.append(b)

    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

    s = str(a, m, n)
    print(s)

main()