#3. Найти количество элементов, равных последнему элементу

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(0, 100))

def pr(a):
    for i in a:
        print(i, end=' ')

def quant(a, n):
    q = 0
    for i in a:
        if i == a[n-1]:
            q = q+1
    return q

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    q = quant(a, n)
    print()
    print(f'Количество элементов, равных {a[n-1]}, {q}')

main()