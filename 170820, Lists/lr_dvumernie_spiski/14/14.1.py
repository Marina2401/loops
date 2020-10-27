#13.1. Задана квадратная матрица. Переставить строку с максимальным элементом на главной диагонали
# со строкой с заданным номером m.

import random

def max(a, n):
    ma = -20
    i_ma = 0
    for i in range(n):
        if a[i][i] > ma:
            ma = a[i][i]
            i_ma = i
    return i_ma

def change(a, n, m):
    mx = max(a, n)
    for j in range(n):
        a[m][j], a[mx][j] = a[mx][j], a[m][j]

def main():
    n = int(input('Введите порядок матрицы '))
    m = int(input('введите номер строки '))
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

    change(a, n, m)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()
main()