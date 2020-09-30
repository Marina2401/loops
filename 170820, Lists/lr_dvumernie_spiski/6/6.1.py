#6.1. Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и в
# каждом столбце наименьший. Вывести на экран.

import random

def ma_string(a, n):
    c = []
    for i in range(n):
        ma = a[i][0]
        for j in range(n):
            if a[i][j] > ma:
                ma = a[i][j]
        c.append(ma)
    return c

def mi_column(a, n):
    for j in range(n):
        mi = a[0][j]
        for i in range(n):
            if a[i][j] < mi:
                mi = a[i][j]
        print(mi)
    return True

def main():
    n = int(input('Введите порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(-10, 10))
        a.append(b)

    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()

    print()
    print('Минимумы по строкам:')
    m = ma_string(a, n)
    print(m)
    print()
    print('Минимумы по столбцам: ')
    mi_column(a, n)

main()
