#2. Дан одномерный массив из 15 элементов. Элементам массива меньше 10 присвоить нулевые значения,
# а элементам больше 20 присвоить 1. Вывести на экран монитора первоначальный и преобразованный массивы
# в строчку.


#Если числа от 10 до 20 - оставляет тот же список! не знаю, как написать для этого сулчая, что
#все числа от 10 до 20

import random

def cr(a):
    for i in range(15):
        a.append(random.randint(10, 20))

def pr(a):
    for i in a:
        print(i, end=' ')
    print()

def twenty(a):
    find = False
    for i in range(15):
        if a[i] < 10:
            find = True
            a[i] = 0
        elif a[i] > 20:
            a[i] = 1
            find = True
    return find

def main():
    a = []
    cr(a)
    pr(a)
    b = all(10 <= i <= 20 for i in a)
    t = twenty(a)
    if t == True:
        pr(a)
    else:
        print('список остался тот же')

main()