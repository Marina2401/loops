#7.1 Квадратная матрица, симметричная относительно главной диагонали,
# задана верхним треугольником в виде одномерного массива. Восстановить
# исходную матрицу и напечатать по строкам.

import random

def cr(a, n):
    for i in range(n):
        a.append(random.randint(-10, 10))
    return a

def pr(a):
    for i in a:
        print(i, end=' ')

def matrix(a, n):


