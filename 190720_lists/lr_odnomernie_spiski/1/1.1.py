#1. Дан одномерный массив, состоящий из N целочисленных элементов.
# Ввести массив с клавиатуры. Найти максимальный элемент.
# Вывести массив на экран в обратном порядке.

import random
import sys
def cr(a, n):
    for i in range(n):
        a.append(int(input()))
    return a

def ma(a):
    ma = -sys.maxsize
    for i in a:
        if i > ma:
            ma = i
    return ma

def op(a, n):
    for i in range(n, 0, -1):
        print(a[i-1], end=' ')


def main():
    n = int(input('Введите количество элементов списка '))
    a = []
    c = cr(a, n)
    print(c)
    m = ma(a)
    print(f'Максимальный элемент {m}')
    op(a, n)

main()
