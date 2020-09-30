#13.2. Дан одномерный массив из 8 элементов. Заменить все элементы массива меньшие 15 их
# удвоенными значениями. Вывести на экран монитора преобразованный массив.

import random

def cr(a):
    for i in range(8):
        a.append(random.randint(-15, 30))

def pr(a):
    for i in a:
        print(i, end=' ')

def comp(a, b):
    i = 0
    while i < 8:
        if a[i] < 15:
            a[i] = 2 * a[i]
            b.append(a[i])
        i += 1
    return b

def main():
    a = []
    cr(a)
    pr(a)
    print()
    b = []
    c = comp(a, b)
    if not c:
        print('в исходном списке нет элементов меньше 15')
    else:
        print(c)

main()