#1. Дан массив целых чисел. Найти максимальный элемент массива и его порядковый номер.

import random
import sys

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def m(a, n):
    max = -sys.maxsize
    i = 0
    pos = 0
    while i < n:
        if a[i] > max:
            max = a[i]
            pos = i
        i += 1
    return max, pos

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    ma = m(a, n)
    print('Самый большой элемент ', ma)

main()