#15.2. Среди тех строк целочисленной матрицы, которые содержат только нечетные элементы,
# найти строку с максимальной суммой модулей элементов.

import random

def odd(a, n):
    max_sum = 0
    max_raw = -1
    for i in range(n):
        flag = True
        for j in range(n):
            if a[i][j] % 2 == 0:
                flag = False
                break

        if flag == True:
            sum = 0
            for j in range(n):
                sum = sum + abs(a[i][j])
            if sum > max_sum:
                max_sum = sum
                max_raw = i
    return max_raw


def main():
    n = int(input('Введите порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(-10, 10))
        a.append(b)

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

    max_raw = odd(a, n)
    if max_raw == -1:
        print('Таких строк нет')
    else:
        print(max_raw)

main()