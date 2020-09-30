#Пользователь вводит число. Определить, содержит ли список данное число x.
# Если содержит, то вывести на экран число 7145, если не содержит, то вывести на экран число 5741;

import random

def li(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))
    print(a)

def check(a, x):
    if x in a:
        return True
    else:
        return False

def main():
    n = int(input('Введите количество элементов '))
    a = []
    li(a, n)
    x = int(input('введите число '))
    c = check(a, x)
    if c == True:
        print('7145')
    else:
        print('5741')

main()