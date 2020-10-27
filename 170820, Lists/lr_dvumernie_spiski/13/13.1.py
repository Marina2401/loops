# coding=utf-8
#13.1. Определить наименьший элемент каждой четной строки матрицы А[М, N].

import random

def min(a, n, m):
    for i in range(0, n, 2):
        mi = a[i][0]
        for j in range(m):
            if a[i][j] < mi:
                mi = a[i][j]
        print(mi)
    return True

def main():
    n = int(input('Введите количество строк матрицы '))
    m = int(input('введите количество столбцов '))
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(random.randint(-10, 10))
        a.append(b)

    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()
    print()

    min(a, n, m)



main()