#дан список чисел. Определить, сколько в нём чисел, больше двух своих соседей. Крайние не учитываются.

import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def check(a, n):
    ct = 0
    j = 1
    while j < n - 1:
        if a[j-1] < a[j] and a[j+1] < a[j]:
            ct = ct + 1
        j += 1
    return ct


def main():
    n = int(input('Введите количество чисел '))
    a = []
    cr(a, n)
    pr(a)
    print()
    c = check(a, n)
    if c == 0:
        print('Ни одно число списка не больше обоих своих соседей')
    else:
        print(c)

main()
