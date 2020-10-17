#10.1. Найти максимальный среди всех элементов тех строк заданной матрицы, которые упорядочены
# (либо по возрастанию, либо по убыванию).

import random

def pr(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

def order(a, n):
    j = 0
    i = 0
    k = 0
    while j < n-1:
        if a[i][j] < a[i][j+1]:
            i = k
        j += 1
    return a[k]

def main():
    n = int(input('Введите порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(-10, 10))
        a.append(b)

    pr(a, n)
    order(a, n)

main()