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
    s2 = 0
    i = 0
    while i < n:
        if a[0] > a[-1]:
            data = a[0]
            del a[0]
        else:
            data = a[-1]
            del a[-1]
        pr(a)
        if i % 2 == 0:
            s1 = s1 + data
        else:
            s2 = s2 + data
        i += 1
    return s1, s2


def main():
    n = int(input('Введите количество чисел '))
    a = []
    create(a, n)
    pr(a)
    su1, su2 = sum1(a, n)

    print(su1, su2)

main()
