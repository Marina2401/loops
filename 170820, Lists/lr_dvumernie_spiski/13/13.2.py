#13.2 Найти наибольший и наименьший элементы прямоугольной матрицы и поменять их местами.

import random

def change(a, n):
    ma = -20
    i_ma = 0
    j_ma = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > ma:
                ma = a[i][j]
                i_ma = i
                j_ma = j

    mi = 20
    i_mi = 0
    j_mi = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] < mi:
                mi = a[i][j]
                i_mi = i
                j_mi = j
    a[i_mi][j_mi], a[i_ma][j_ma] = a[i_ma][j_ma], a[i_mi][j_mi]


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
            print(a[i][j], end=' ')
        print()
    print()

    change(a, n)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

main()