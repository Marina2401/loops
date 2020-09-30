#1. Упорядочить по возрастанию элементы каждой строки матрицы размером n х m.


import random

def order(a, n):
    for i in range(n):
        a[i].sort()


def main():
    n = int(input('Введите количество строк матрицы '))
    m = int(input('Введите количество столбцов матрицы '))

    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(random.randint(-10, 10))
        a.append(b)

    for i in range(n):
        for j in range(m):
            print(a[i][j], end='\t')
        print()

    order(a, n)
    for i in range(n):
        for j in range(m):
            print(a[i][j], end='\t')
        print()

main()

