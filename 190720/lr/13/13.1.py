#1. Дан одномерный массив целых чисел. Проверить, есть ли в нем одинаковые элементы.
# Вывести эти элементы и их индексы.
#НЕ ВЫВОДИТ ВСЕ ЭЛЕМЕНТЫ И ИХ ИНДЕКСЫ, А ТОЛЬКО НЕКОТОРЫЕ. и слово None

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def equal(a, n):

    for j in range(n-1):
        for i in range(j+1, n-1):
            if a[j] == a[i]:
                print(j, i)

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    e = equal(a, n)
    print(e)

main()