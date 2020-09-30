#1. Определить, является ли заданная целая квадратная матрица n-го порядка симметричной
#(относительно главной диагонали).

import random

def symmetry(a, n):
    for i in range(n):
        for j in range(i+1, n):
            if a[i][j] != a[j][i]:
                return False
    #return True

def main():
    n = int(input('Введите порядок матрицы '))

    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(0, 2))
        a.append(b)

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()

    s = symmetry(a, n)
    if not s:
        print('Не является')
    else:
        print('Является')

main()