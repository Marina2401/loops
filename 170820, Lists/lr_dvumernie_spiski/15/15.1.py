#15.1. Определить номера строк матрицы R[M, N], хотя бы один элемент которых равен с,
# и элементы этих строк умножить на d.

import random

def num(a, n, m, c, d):
    for i in range(n):
        # for j in range(m):
        if c in a[i]:
            # if a[i][j] == c:
            #     i_num = i
            for k in range(m):
                a[i][k] = d * a[i][k]

def main():
    n = int(input('введите количество строк '))
    m = int(input('введите количество столбцов '))
    c = int(input('введите число '))
    d = int(input(f'введите число, на которое надо умножить элементы строк, где встретились элементы c {c}, '))

    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(random.randint(0, 10))
        a.append(b)

    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()
    print()

    num(a, n, m, c, d)

    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()
    print()

main()