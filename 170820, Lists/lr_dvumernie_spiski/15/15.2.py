#15.2. Среди тех строк целочисленной матрицы, которые содержат только нечетные элементы,
# найти строку с максимальной суммой модулей элементов.

import random

def odd(a, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] % 2 == 0:
                return False


def sum(a, n):
    o = odd(a, n)
    s = 0
    sm = 0
    if o == True:
        for i in range(n):
            for j in range(n):
                s = s + abs(a[i][j])



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
            print(a[i][j], end=' ')
        print()
    print()


main()