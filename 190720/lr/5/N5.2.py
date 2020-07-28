#2. Дан целочисленный массив размера 10. Создать новый массив,
# удалив все одинаковые элементы, оставив их 1 раз.
#НЕ ЗНАЮ, КАК СДЕЛАТЬ ЭТО ЧЕРЕЗ ЦИКЛЫ! НАШЛА РЕШЕНИЕ ТОЛЬКО ЧЕРЕЗ СЕТ И С СОРТИРОВКОЙ ПО УБЫВАНИЮ,
#КОТОРАЯ НЕ НУЖНА

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))

def pr(a):
    for i in a:
        print(i, end=' ')

def main():
    n = 10
    a = []
    cr(a, n)
    pr(a)
    print()
    print(list(set(a)))

main()