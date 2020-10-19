#1. Задана матрица порядка n и число к. Разделить элементы k-й строки на диагональный элемент,
# расположенный в этой строке.
import random
def pr(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()
    print()

def main():
    n = int(input('Введите порядок матрицы n '))

    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(1, 10))
        a.append(b)

    pr(a, n)
#почему неправильно работает цикл: for j in range(n):
    #a[k][j] = a[k][j]//a[k][k]??

    k = int(input('введите номер строки '))
    p = a[k][k]
    j = 0
    while j < n:
        a[k][j] = a[k][j]//p
        j += 1

    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()
    print()

main()