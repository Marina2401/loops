#15.1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран эти значения.

#ВОЗВРАЩАЕТ НЕ ВСЕ

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def comp(a, n):
    while True:
        for i in range(n - 2):
            for j in range(i+1, n-1):
                if a[i] == a[j]:
                    return a[i], a[j]

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    c = comp(a, n)
    print(c)

main()