#10.1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение,
# иначе сообщение об их отсутствии.

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def check(a, n):
    i = 0
    b = []
    while i < n:
        for j in range(i+1, n):
            if a[i] == a[j]:
                b.append(a[i])
        i += 1
    return b

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    c = check(a, n)
    if len(c) == 0:
        print('Нет одинаковых элементов')
    else:
        pr(c)

main()