#11.1Найти наибольший элемент списка, который делится на 2 без остатка и вывести его на экран.

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
    while i < n:
        if a[i] > max and a[i] % 2 == 0:
            max = a[i]
        i += 1
    return max

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    mx = ma(a, n)
    if mx == -sys.maxsize:
        print('Нет четных элементов')
    else:
        print('Самое большое из четных чисел', mx)

main()
