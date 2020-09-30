#2. Дан одномерный массив целого типа. Получить другой массив, состоящий только из нечетных чисел
# исходного массива или сообщить, что таких чисел нет. Полученный массив вывести в порядке убывания
# элементов.

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def odd(a, b, n):
    i = 0
    while i < n:
        if a[i] % 2 == 1:
            b.append(a[i])
        i += 1
    b.sort(reverse=True)
    return b


def main():
    n = int(input('введите количество элементов '))
    a = []
    b = []
    cr(a, n)
    pr(a)
    print()
    o = odd(a, b, n)
    if b == []:
        print('В списке а нечетных чисел нет')
    else:
        print(o)

main()
