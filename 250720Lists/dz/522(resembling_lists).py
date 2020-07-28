#Два массива называются похожими, если совпадают множества чисел, встречающихся в этих массивах.

#Требуется написать программу, которая определит: похожи ли два заданных массива.

import random

def create(a, b, n, m):
    for i in range(n):
        a.append(random.randint(0, 2))

    for j in range(m):
        b.append(random.randint(0, 2))

def pr(a, b):
    for i in a:
        print(i, end = ' ')
    print()
    for j in b:
        print(j, end = ' ')
    print()

def compare(a, b):
    if set(a) == set(b):
        return True
    else:
        return False


def main():
    n = int(input('введите количество элементов первого списка '))
    m = int(input('введите количество элементов второго списка '))
    a = []
    b = []
    create(a, b, n, m)
    pr(a, b)
    c = compare(a, b)
    if c:
        print('Множества похожи')
    else:
        print('множества не похожи')

main()
