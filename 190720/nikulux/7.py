#Поменять местами самый большой и самый маленький элементы списка;
import sys
import random

def li(a, n):
    for i in range(n):
        a.append(random.randint(-100, 100))
    print(a)

def ma(a, n):
    max = -sys.maxsize
    i = 0
    while i < n:
        if a[i] > max:
            max = a[i]
            b = i
        i += 2
    return b

def mi(a, n):
    min = sys.maxsize
    i = 0
    while i < n:
        if a[i] < min:
            min = a[i]
            c = i
        i += 1
    return c

def main():
    n = int(input('введите количество элементов '))
    a = []
    li(a, n)
    m1 = ma(a, n)
    m2 = mi(a, n)
    if m1 == m2:
        print('Все элементы одинаковые')
    else:
        a[m1], a[m2] = a[m2], a[m1]
        print(a)

main()

