#11.2Дан одномерный массив целого типа. Получить другой массив, состоящий только из четных чисел
# исходного массива, меньше 10, или сообщить, что таких чисел нет.
# Полученный массив вывести в порядке возрастания элементов.
#НЕ ЗНАЮ, КАК СДЕЛАТЬ НАДПИСЬ С УСЛОВИЕМ "ТАКИХ ЧИСЕЛ НЕТ"

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-15, 15))

def pr(a):
    for i in a:
        print(i, end=' ')

def ba(a, b, n):
    for i in range(n):
        if a[i] % 2 == 0 and a[i] < 10:
            b.append(a[i])
    return b

def main():
    n = int(input('Введите количество элементов '))
    a = []
    b = []
    cr(a, n)
    pr(a)
    print()
    mas2 = ba(a, b, n)
    if not mas2:
        print('нет четных чисел меньше 10 в исходном списке')
    else:
        print(mas2)

main()
