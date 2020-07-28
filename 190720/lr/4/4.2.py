##2. Дан одномерный массив целого типа. Получить другой массив, состоящий только из нечетных чисел исходного
# массива или сообщить, что таких чисел нет. Полученный массив вывести в порядке убывания элементов.

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def pr2(a, n):
    i = 0
    while i < n:
        if a[i] % 2 == 0:
            del a[i]
            n -= 1
        else:
            i += 1

    a.sort(reverse=True)
    return a

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    p = pr2(a, n)
    if not p:
        print('Нечетных чисел нет в исходном списке')
    else:
        print(p)

main()