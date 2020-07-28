#1. В одномерном числовом массиве D длиной n вычислить сумму элементов с нечетными индексами.
# Вывести на экран массив D, полученную сумму.


import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def s1(a, n):
    s = 0
    i = 0
    while i < n:
        if i % 2 != 0:
            s = s + a[i]
        i += 1
    return s

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    s = s1(a, n)
    print(s)

main()