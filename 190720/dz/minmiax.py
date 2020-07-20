#Требуется поменять местами максимальный и минимальный элемент списка.(Предполагается, что все элементы
# списка различны)

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
    for j in range(n):
        if a[j] < mi:
            mi = a[j]
    return mi

def ma(a, n):
    ma = -sys.maxsize
    for i in range(n):
        if a[i] > ma:
            ma = a[i]
    return ma

def main():
    n = int(input('Введите количество чисел '))
    a = []
    cr(a, n)
    pr(a)
    b = ma(a, n)
    c = mi(a, n)
    print()
    print(f'Максимальный элемент {b}')
    print(f'Минимальный элемент {c}')
    print()
    d = a.index(max(a))
    e = a.index(min(a))
    a[d], a[e] = a[e], a[d]
    print(a)
main()


