# 16*. Удалить все отрицательные
import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-100, 100))

def pr(a):
    for i in a:
        print(i, end=' ')

def neg(a, n):
    i = 0
    while i < n:
        if a[i] < 0:
            del a[i]
            n -= 1
        else:
            i += 1
    return a

def main():
    n = int(input('ВВедите коилчество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    ng = neg(a, n)
    print(ng)


main()

