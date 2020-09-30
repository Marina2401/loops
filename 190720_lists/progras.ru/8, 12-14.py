#8. Посчитать, сколько пар из повторяющихся подряд элементов
# 12*. Найти значение самого большого элемента
# 13*. Удалить самый большой элемент
# 14*. Удалить самый маленький

import sys
import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-200, 200))

def pr(a):
    for i in a:
        print(i, end=' ')

def povt(a, n):
    ct = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            ct = ct + 1
    return ct

def f_max(a):
    b = -sys.maxsize
    for j in a:
        if j > b:
            b = j
    return b

def d_max(a):
    dm = max(a)
    a.remove(dm)
    return a

def d_min(a):
    c = sys.maxsize
    for j in a:
        if j < c:
            c = j
    a.remove(c)
    return a

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    po = povt(a, n)
    print(f'Количество пар из повторяющихся цисел, идущих подряд: {po}')
    m = f_max(a)
    print(f'Самый большой элемент {m}')
    d_m = d_max(a)
    print(f'Список без самого большого элемента {d_m}')
    am = d_min(a)
    print(f'Список без самого маленького элемента и равных ему {am}')

main()