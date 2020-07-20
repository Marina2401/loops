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
    mi = sys.maxsize
    for i in range(n):
        if a[i] < mi:
            mi = a[i]
    return mi

def mi2(a, n):
    c = mi(a, n)
    a.remove(c)
    b = mi(a, n-1)
    return b

def main():
    n = int(input('Введите количество чисел '))
    a = []
    cr(a, n)
    pr(a)
    d = mi(a, n)
    e = mi2(a, n-1)
    print()
    print(d)
    print(e)

main()
