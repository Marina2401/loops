#1. Дан одномерный массив из 10 целых чисел. Вывести пары отрицательных чисел, стоящих рядом.

#не могу избавиться от слова True!!!

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def neg(a, n):
    num = False
    i = 0
    while i < n - 1:
        if a[i] < 0 and a[i+1] < 0:
            num = True
            print(a[i], a[i+1])
        i += 1
    return num


def main():
    n = 10
    a = []
    cr(a, n)
    pr(a)
    print()
    ne = neg(a, n)
    if not ne:
        print('В исходном списке нет отрицательных чисел, стоящих рядом')


main()
