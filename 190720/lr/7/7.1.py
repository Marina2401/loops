#1. Дан массив целых чисел. Найти сумму элементов с четными номерами и произведение элементов
# с нечетными номерами. Вывести сумму и произведение.

import random

def cr(a,n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def sum(a, n):
    sum = 0
    i = 0
    while i < n:
        if i % 2 == 0:
            sum = sum + a[i]
        i += 1
    return sum

def pro(a, n):
    pro = 1
    i = 0
    while i < n:
        if i % 2 != 0:
            pro = pro * a[i]
        i += 1
    return pro

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    s = sum(a, n)
    print()
    print(s)
    p = pro(a, n)
    print(p)

main()