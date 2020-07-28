#8.2. В массиве действительных чисел все нулевые элементы заменить на среднее арифметическое всех
# элементов массива.

#Как написать "Нет нулевых элементов???"

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def avg(a, n):
    i = 0
    s = 0
    while i < n:
        s = s + a[i]
        i += 1
    avg = s/n
    return avg

def change(a, n):
    c = avg(a, n)
    i = 0
    # find = False
    while i < n:
        if a[i] == 0:
            # find = True
            a[i] = c
        i += 1
    # return a

def any(a):
    for i in a:
        if i == 0:
            return True
    return False

def main():
    n = 10
    a = []
    cr(a, n)
    pr(a)
    av = avg(a, n)
    print()
    print('Среднее арифметическое всех элементов', av)
    # if ch == False:
    #     print('Нулевых элементов нет')
    # else:
    #     pr(a)

    if any(a) == True:
        change(a, n)
        pr(a)
    else:
        print('нет нулевых элементов')


main()