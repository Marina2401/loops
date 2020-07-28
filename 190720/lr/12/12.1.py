#1. Найти наименьший нечетный элемент списка и вывести его на экран.

import random
import sys

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def mi(a, n):
    m3 = sys.maxsize
    i = 0
    while i < n:
        if a[i] % 2 == 1 and a[i] < m3:
            m3 = a[i]
        i += 1
    return m3

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    m = mi(a, n)
    if m == sys.maxsize:
        print('нечетных элементов нет')
    else:
        print(m)
main()
