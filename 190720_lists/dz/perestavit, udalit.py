#Переставить список в обратном порядке. Удалить все максимальные элементы.
import random
import sys
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')
    print()

def pr2(a, n):
    for i in range(len(a)//2):
        temp = a[i]
        a[i] = a[n-1-i]
        a[n-1-i] = temp

def ma(a):
    ma = -sys.maxsize
    for i in a:
        if i > ma:
            ma = i
    return ma

def pr3(a, n):
    k = ma(a)
    i = 0
    while i < n:
        if a[i] == k:
            del a[i]
            n -= 1
        else:
            i += 1

def main():
    n = int(input('Введите количество элементов списка '))
    a = []
    cr(a, n)
    pr(a)
    #m = ma(a)
    #print()
    pr2(a, n)
    pr(a)
    pr3(a, n)
    pr(a)

main()