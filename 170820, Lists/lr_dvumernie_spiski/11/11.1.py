#11.1. В данной действительной квадратной матрице порядка п найти сумму элементов строки,
# в которой расположен элемент с наименьшим значением. Предполагается, что такой элемент единственный.

import random

def pr(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end=' ')
        print()
    print()

def min_i(a):
    mi = 20
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] < mi:
                mi = a[i][j]
                i_mi = i
    return i_mi


def sum(a, n):
    p = min_i(a)
    print(p)
    s = 0
    for j in range(n):
        s = s + a[p][j]
    return s


def main():
    n = int(input('Введите порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(-10, 10))
        a.append(b)

    pr(a)

    s = sum(a, n)
    print(f'Сумма элементов строки с минимальным элементом {s}')


main()
