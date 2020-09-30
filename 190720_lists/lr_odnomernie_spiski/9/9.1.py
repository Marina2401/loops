#9.1. Дан одномерный массив, состоящий из N вещественных элементов.
# Ввести массив с клавиатуры. Найти и вывести минимальный по модулю элемент.
# Вывести массив на экран в обратном порядке.

def mi(a, n):
    s = 10000
    i = 0
    while i < n:
        if abs(a[i]) < s:
            s = abs(a[i])
        i += 1
    return s

def obra(a, n):
    a.reverse()
    print(a)

def main():
    a = []
    n = int(input('Введите количество элементов '))
    for i in range(n):
        a.append(int(input('Введите элемент ')))
    print(a)
    print()
    obra(a, n)
    print()
    m = mi(a, n)
    print('Минимальный по модулю ', m)

main()
