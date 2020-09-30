# 2. Дана вещественная матрица размером n х m. Переставляя ее строки и столбцы,
# добиться того, чтобы наибольший элемент (или один из них) оказался в верхнем левом углу.

import random

def printlist(a):
    for row in a:
        for elem in row:
            print(elem, end = '\t')
        print()
    print()

def maxelem(a):
    max = a[0][0]
    imax = 0
    jmax = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > max:
                max = a[i][j]
                imax = i
                jmax = j
    return imax, jmax

def turn(a, imax, jmax):
    for i in range(imax, 0, -1):
        for j in range(len(a[i])):
            a[i][j], a[i-1][j] = a[i-1][j], a[i][j]

    for j in range(jmax, 0, -1):
        for i in range(len(a)):
            a[i][j], a[i][j-1] = a[i][j-1], a[i][j]

def main():
    n = int(input('Введите ширину матрицы '))
    m = int(input('Введите высоту матрицы '))
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            b.append(random.randint(0, 100))
        a.append(b)

    printlist(a)
    imax, jmax = maxelem(a)

    turn(a, imax, jmax)
    printlist(a)


main()