# coding=utf-8
#8.2. Задана квадратная матрица. Получить транспонированную матрицу
# (перевернутую относительно главной диагонали) и вывести на экран.

import random

def main():
    n = int(input('Введите порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(0, 9))
        a.append(b)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()
    print()

    for i in range(n):
        for j in range(i + 1, n):
            t = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = t
    print()

    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()
    print()

main()