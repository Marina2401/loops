#1. Дан одномерный массив, состоящий из N целочисленных элементов. Ввести массив с клавиатуры.
# Найти минимальный элемент. Вывести индекс минимального элемента на экран.
#
import sys
def cr(a, n):
    for i in range(n):
        a.append(int(input('Введите элемент списка ')))
    return a

def mi(a, n):
    mi = sys.maxsize
    i = 0
    pos = 0
    while i < n:
        if a[i] < mi:
            mi = a[i]
            pos = i
        i += 1
    return mi, pos

def main():
    n = int(input('Введите количество элементов '))
    a = []
    c = cr(a, n)
    print(c)
    m = mi(a, n)
    print(f'min = {m}')

main()



