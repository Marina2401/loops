#Найти 2 минимальных элемента
import random
import sys
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def mi(a, n):
    mi1 = sys.maxsize
    ind = 0
    for i in range(n):
        if a[i] < mi1:
            mi1 = a[i]
            ind = i
    mi2 = sys.maxsize
    for i in range(n):
        if a[i] < mi2 and i != ind:
            mi2 = a[i]

    return mi1, mi2


def main():
    n = int(input('Введите количество чисел '))
    a = []
    cr(a, n)
    pr(a)
    d, e = mi(a, n)
    print()
    print(d, e)

main()
