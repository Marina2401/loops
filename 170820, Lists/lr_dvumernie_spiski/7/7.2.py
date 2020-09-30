#7.2 Для заданной квадратной матрицы сформировать одномерный массив из ее диагональных
# элементов. Найти след матрицы, просуммировав элементы одномерного массива.
# Преобразовать исходную матрицу по правилу: четные строки разделить на полученное значение,
# нечетные оставить без изменения.

import random


def cr(a, n):
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(-10, 10))
        a.append(b)
    return a

def pr(a, n):
    for i in range(n):
        for j in range(len(a)):
            print(a[i][j], end='\t')
        print()
    print()

def diag(a, n):
    b = []
    for i in range(n):
        b.append(a[i][i])
    return b

def trace(a, n):
    s = 0
    for i in range(n):
        s = s + a[i][i]
    return s



def main():
    n = int(input('введите порядок матрицы '))
    a = []
    cr(a, n)
    pr(a, n)
    d = diag(a, n)
    print(f'Элементы главной диагонали {d}')
    t = trace(a, n)
    print(f'След матрицы: {t}')

    for i in range(0, n, 2):
        for j in range(n):
            a[i][j] = a[i][j]/t
    pr(a, n)
main()


