#Дан список и индекс элемента, который надо удалить. Представить список без этого элемента со
#сдвинутыми влево следующими за ним элементами

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def ud(a, k):
    for i in range(k, len(a)-1):
        a[i] = a[i+1]
    a.pop()

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    k = int(input('Введите индекс элемента, который надо удалить '))
    ud(a, k)
    pr(a)

if __name__ == '__main__':
    main()
