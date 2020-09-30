# Найти сумму всех элементов списка
import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(1, 100))

def pr(a):
    for i in a:
        print(i, end=' ')

def sum(a):
    s = 0
    i = 0
    for i in a:
        s = s + i
    return s

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    b = sum(a)
    print(f'Сумма всех элементов {b}')

main()