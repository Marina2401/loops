# 17*. Все отрицательные сделать положительными
import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-100, 100))

def pr(a):
    for i in a:
        print(i, end=' ')

def negpos(a, n):
    for i in range(n):
        if a[i] < 0:
            a[i] = - a[i]
    return a

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    np = negpos(a, n)
    print(np)


main()
