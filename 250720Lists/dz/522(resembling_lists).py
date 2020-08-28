#Два массива называются похожими, если совпадают множества чисел, встречающихся в этих массивах.

#Требуется написать программу, которая определит: похожи ли два заданных массива.

import random

def create(a, n):
    for i in range(n):
        num = int(input('Введите элемент '))
        a.append(num)

def pr(a):
    for i in a:
        print(i, end=' ')
    print()


def compare(a, b):
    for i in a:
        if i not in b:
            return False
    for j in b:
        if j not in a:
            return False
    return True


# def compare(a, b):
#     if set(a) == set(b):
#         return True
#     else:
#         return False


def main():
    n = int(input('введите количество элементов первого списка '))
    m = int(input('введите количество элементов второго списка '))
    a = []
    b = []
    create(a, n)
    pr(a)
    create(b, m)
    pr(b)
    c = compare(a, b)
    if c:
        print('Множества похожи')
    else:
        print('множества не похожи')

main()
