#2. Переставить в одномерном массиве минимальный элемент и максимальный.

#Что делать, если минимальных или максимальных элементов несколько?

def ma(a):
    max = -100000
    c = 0
    for i in range(7):
        if a[i] > max:
            max = a[i]
            c = i
    return c

def mi(a):
    min = 100000
    d = 0
    for i in range(7):
        if a[i] < min:
            min = a[i]
            d = i
    return d

def main():
    a = []
    for i in range(7):
        a.append(int(input('введите элемент списка ')))
    print(a)
    print()
    m1 = ma(a)
    m2 = mi(a)
    a[m1], a[m2] = a[m2], a[m1]
    print(a)


main()
