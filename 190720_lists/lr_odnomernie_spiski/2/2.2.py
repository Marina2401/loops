#2. Дан массив целых чисел. Переписать все положительные элементы во второй массив,
# а остальные - в третий.

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-100, 0))

def pr(a):
    for i in a:
        print(i, end=' ')

def mas1(a, b, n):
    while True:
        for i in range(n):
            if a[i] > 0:
                b.append(a[i])
        return b

def mas2(a, c, n):
    while True:
        for i in range(n):
            if a[i] <= 0:
                c.append(a[i])
        return c

def main():
    n = int(input('Введите количество элементов '))
    a = []
    b = []
    c = []
    cr(a, n)
    pr(a)

    m1 = mas1(a, b, n)
    m2 = mas2(a, c, n)
    print()
    if not m1:
        print('Все числа меньше 0')
        print(m2)
    elif not m2:
        print(m1)
        print('Все числа больше 0')
    else:
        print(m1)
        print(m2)

main()