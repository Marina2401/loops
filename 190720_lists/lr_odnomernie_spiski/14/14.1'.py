#1. Найти максимальный элемент численного массива и поменять его местами с минимальным.
#Что делать, если минимальных или максимальных несколько?

import random
import sys

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def ma(a, n):
    max = -sys.maxsize
    i = 0
    e = 0
    while i < n:
        if a[i] > max:
            max = a[i]
            e = i
        i += 1
    return e

def mi(a, n):
    min = sys.maxsize
    j = 0
    f = 0
    while j < n:
        if a[j] < min:
            min = a[j]
            f = j
        j += 1
    return f

def main():
    n = int(input('Введите количество элементов списка '))
    a = []
    cr(a, n)
    pr(a)
    print()
    m1 = ma(a, n)
    m2 = mi(a, n)
    a[m1], a[m2] = a[m2], a[m1]
    print(a)

main()