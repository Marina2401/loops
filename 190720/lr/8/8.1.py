#8.1. Найдите сумму и произведение элементов списка. Результаты вывести на экран.

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def s(a, n):
    sum = 0
    i = 0
    while i < n:
        sum = sum + a[i]
        i += 1
    return sum

def pro(a, n):
    p = 1
    i = 0
    while i < n:
        p = p * a[i]
        i += 1
    return p

def main():
    n = 10
    a = []
    cr(a, n)
    pr(a)
    su = s(a, n)
    prod = pro(a, n)
    print()
    print('Сумма всех элементов', su)
    print('Произведение всех элементов', prod)

main()