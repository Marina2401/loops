#требуется написать игру, где каждый игрок вычеркивает из списка большее число либо слева, либо справа. за
#каждое вычеркивание игроки получают баллы - ту цифру, что вычеркнуты.
#игра длится, пока есть числа. следует выдать количество суммарное очков первого и второго игрока.

import random
import math

def create(a, n):
    for i in range(n):
        a.append(random.randint(0, 10))

def pr(a):
    for i in a:
        print(i, end=' ')
    print()

def sum1(a, n):
    s1 = 0
    i = 0
    while i < math.ceil(n/2):
        if a[i] > a[n-1-i]:
            s1 = s1 + a[i]
            del a[i]
        else:
            s1 = s1 + a[n-1-i]
            del a[n-1-i]
        n -= 2
    return s1

def sum2(a, n):
    s2 = 0
    j = 1
    while j < math.ceil((n-1)/2):
        if a[j] > a[n-1-j]:
            s2 = s2 + a[j]
            del a[j]
        else:
            s2 = s2 + a[n-1-j]
            del a[n-1-j]
        n -= 2
    return s2


def main():
    n = int(input('Введите количество чисел '))
    a = []
    create(a, n)
    pr(a)
    su1 = sum1(a, n)
    su2 = sum2(a, n)

    print(su1, su2)

main()
