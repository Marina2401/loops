#5. Удалить последние два элемента.
#6. Удалить элементы, стоящие на нечетных местах
#7. Посчитать количество положительных, которые идут после отрицательных.

import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-100, 100))

def pr(a):
    for i in a:
        print(i, end=' ')

def dl1(a):
    a = a[:-2]
    return a

def dl2(a):
    a = a[::2]
    return a

# def dl3(a, n):
#     ct = 0
#     for i in range(0, n):
#         if a[i] < 0 and a[i+1] > 0:
#             ct = ct + 1
#     return ct

def main():
    n = int(input('Введите количество элементов, большее 2, '))
    a = []
    cr(a, n)
    pr(a)
    d = dl1(a)
    print()
    d2 = dl2(a)
    # d3 = dl3(a, n)
    print()
    print(d)
    print()

    print(d2)
    print()
    # print(d3)

main()