#9.2. Даны массивы A и B одинакового размера 10. Вывести исходные массивы.
# Поменять местами их содержимое и вывести в начале элементы преобразованного массива A,
# а затем — элементы преобразованного массива B.

import random

def cr(a, b):
    for i in range(10):
        a.append(random.randint(-10, 10))
    for j in range(10):
        b.append(random.randint(-10, 10))


def pr(a, b):
    for i in a:
        print(i, end=' ')
    print()
    for j in b:
        print(j, end=' ')

def main():
    a = []
    b = []
    cr(a, b)
    pr(a, b)

main()


