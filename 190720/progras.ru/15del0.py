# 15*. Удалить все элементы, равные нулю

import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(0, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def nol(a, n):
    while True:
        i = 0
        while i < n:
            if a[i] == 0:
                del a[i]
                n -= 1
            else:
                i += 1
        return a

def main():
    n = int(input('Введите количество чисел списка '))
    a = []
    cr(a, n)
    pr(a)
    print()
    nul = nol(a, n)
    print(nul)

main()