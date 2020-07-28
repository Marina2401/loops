#2. Дан одномерный массив из 8 элементов. Заменить все элементы массива меньшие 15 их удвоенными значениями.
# Вывести на экран монитора преобразованный массив.

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(0, 30))

def pr(a):
    for i in a:
        print(i, end=' ')

def fifteen(a, b, n):
    i = 0
    while i < n:
        if a[i] < 15:
            a[i] = 2 * a[i]
            b.append(a[i])
        i += 1
    return b

def main():
    n = int(input('введите количество элементов '))
    a = []
    b = []
    cr(a, n)
    pr(a)
    print()
    f = fifteen(a, b, n)
    if not f:
        print('В исходном списке нет элементов меньше 15')
    else:
        print(f)

main()
