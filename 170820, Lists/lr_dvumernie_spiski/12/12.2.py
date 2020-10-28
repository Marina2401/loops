#12.2. Дана действительная матрица размером n х m.
# Требуется преобразовать матрицу: поэлементно вычесть последнюю строку из всех строк, кроме последней.

import random

def string(a, m, n):
    for i in range(m-1):
        for j in range(n):
            a[i][j] = a[i][j] - a[m-1][j]



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

    string(a, m, n)
    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

main()