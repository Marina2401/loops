#1. Дана целая квадратная матрица n-го порядка. Определить, является ли она
# магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках
# и столбцах одинаковы.

import random


# for i in range(n):
#     s1 = 0
#     for j in range(n):
#         s1 = s1 + a[i][j]
#     print(i, s1)
#
# for j in range(n):
#     s2 = 0
#     for i in range(n):
#         s2 = s2 + a[i][j]
#     print(j, s2)

def check_wonderful_square(a, n):
    sum1 = 0
    for j in range(n):
        sum1 = sum1 + a[0][j]
    for i in range(1, n):
        sum2 = 0
        for j in range(n):
            sum2 = sum2 + a[i][j]
        if sum2 != sum1:
            return False

    for j in range(n):
        sum2 = 0
        for i in range(n):
            sum2 = sum2 + a[i][j]
        if sum2 != sum1:
            return False
    return True

def main():
    n = int(input('Введите порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            print('Введите элемент')
            b.append(int(input()))
        a.append(b)

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()

    c = check_wonderful_square(a, n)
    if c == True:
        print('Является')
    else:
        print('Не является')

main()
