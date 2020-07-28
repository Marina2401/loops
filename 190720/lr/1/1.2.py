#1.2. В массиве действительных чисел все нулевые элементы заменить на среднее арифметическое всех элементов
# массива.

import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def avg(a, n):
    s = 0
    for i in a:
        s = s + i
    avg = s//n
    return avg

def change(a, n):
    av = avg(a, n)
    i = 0
    while i < n:
        if a[i] == 0 and av != 0:
            a[i] = av
        else:
            i += 1
    return a

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    g = avg(a, n)
    print()
    print('Среднее арифметическое всех элементов ', g)
    c = change(a, n)
    if c == a:
        print('нет нулевых элементов в заданном списке')
    else:
        print(c)


main()

