#1. Дан одномерный массив из 10 целых чисел.
# Найти максимальный элемент и сравнить с ним остальные элементы.
# Вывести количество меньших максимального и больших максимального элемента.

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
    while i < n:
        if a[i] > max:
            max = a[i]
        i += 1
    return max

def ct_max(a, n):
    ma = m(a, n)
    ct = 0
    for i in range(n):
        if a[i] == ma:
            ct = ct + 1
    return ct

def main():
    n = 10
    a = []
    cr(a, n)
    pr(a)
    print()
    mx = m(a, n)
    print('Максимальный элемент', mx)
    q = ct_max(a, n)
    print('Количество максимальных элементов', q)
    c = n - q
    print('Количество элементов меньше максимума', c)
    print('Количество элементов больше максимального, 0')

main()