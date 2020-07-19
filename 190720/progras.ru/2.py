# Найти сумму элементов, которые больше первого элемента

import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(1, 100))

def pr(a):
    for i in a:
        print(i, end=' ')

def sum(a):
    s = 0
    for i in a:
        if i > a[0]:
            s = s + i
    return s

def main():
    n = int(input('введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    b = sum(a)
    print()
    print(f'Сумма элементов, больших {a[0]}, {b}')

main()

