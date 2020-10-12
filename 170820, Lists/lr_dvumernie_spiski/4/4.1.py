#4.1. Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой
# элементов. Вывести на печать найденные строки и суммы их элементов.


import random
import math

def str(a, n, m):
    mi = 100000
    ma = -100000
    for i in range(n):
        s1 = 0
        for j in range(m):
            s1 = s1 + a[i][j]
        if s1 > ma:
            ma = s1
            e = i
        if s1 < mi:
            mi = s1
            d = i
    print(f'Максимальная сумма {ma}')
    print('Строка с максимальной суммой:')
    for j in range(m):
        print(a[e][j], end='\t')
    print()

    print('Строка с минимальной суммой:')
    for j in range(m):
        print(a[d][j], end='\t')
    print()
    print(f'Минимальная сумма: {mi}')
    print()

    return True

def main():
    n = int(input('Введите количество строк матрицы '))
    m = int(input('Введите количество столбцов матрицы '))

    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(random.randint(0, 10))
        a.append(b)

    for i in range(n):
        for j in range(m):
            print(a[i][j], end='\t')
        print()

    print()

    str(a, n, m)


main()