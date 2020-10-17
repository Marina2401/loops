#12.1. Для заданной квадратной матрицы найти такие k, что k-я строка матрицы совпадает с k-м столбцом.

import random
def pr(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()
    print()

def find_k(a):
    find = False
    for i in range(len(a)):
        check = True
        for j in range(len(a)):
            if a[i][j] != a[j][i]:
                check = False
                break
        if check == True:
            print(i)
            find = True
    if find == False:
        print('Нет таких строк')

def main():
    n = int(input('Введите порядок матрицы n '))

    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(int(input('Введите число ')))
        a.append(b)
    pr(a, n)
    find_k(a)

main()