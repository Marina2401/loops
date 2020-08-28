# Дана последовательность из чисел от 0 до 9.
# требуется посчитать, сколько раз в ней встречается каждая цифра.

import random

def create(a, n):
    for i in range(n):
        a.append(random.randint(0, 9000))

def pr(a):
    for i in a:
        print(i, end=' ')
    print()

def quant(a):
    for j in range(9000):
        if a.count(j) != 0:
            print(f'{j}:{a.count(j)}')

def main():
    n = int(input('введите количество чисел последовательности '))
    a = []
    create(a, n)
    pr(a)
    quant(a)

main()
