#Требуется поменять местами максимальный и минимальный элемент списка.(Предполагается, что все элементы
# списка различны)

#КАК ОТДЕЛЬНО ВЫВЕСТИ ЭКСТРЕМУМЫ И ИХ ИНДЕКСЫ???

import random
import sys
def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def mi(a, n):
    mi = sys.maxsize
    j = 0
    while j < n:
        if a[j] < mi:
            mi = a[j]
            b = j
        j += 1
    return b

def ma(a, n):
    ma = -sys.maxsize
    i = 0
    while i < n:
        if a[i] > ma:
            ma = a[i]
            c = i
        i += 1
    return c

def main():
    n = int(input('Введите количество чисел '))
    a = []
    cr(a, n)
    pr(a)
    m1 = ma(a, n)
    m2 = mi(a, n)
    print()
    print(f'Максимальный элемент {a[m1]}, '
          f'минимальный элемент {a[m2]} ')
    temp = a[m1]
    a[m1] = a[m2]
    a[m2] = temp
    #a[m1], a[m2] = a[m2], a[m1]
    pr(a)
main()


