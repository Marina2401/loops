#6.2. Дана действительная квадратная матрица порядка N (N — нечетное), все элементы которой
# различны. Найти наибольший элемент среди стоящих на главной и побочной диагоналях и поменять
# его местами с элементом, стоящим на пересечении этих диагоналей.


import random

def diagonal(a, n):
    ma = a[0][0]
    i_max1 = 0
    j_max1 = 0

    for i in range(n):
        if a[i][i] > ma:
            ma = a[i][i]
            i_max1 = i
            j_max1 = i

    ma2 = a[0][n-1]
    i_max2 = 0
    j_max2 = 0

    for i in range(n):
        if a[i][n-1-i] > ma2:
            ma2 = a[i][n-1-i]
            i_max2 = i
            j_max2 = n-1-i
    if ma > ma2:
        return(ma, i_max1, j_max1)
    else:
        return(ma2, i_max2, j_max2)

def change(a, n):
    max, i_max, j_max = diagonal(a, n)
    a[n//2][n//2], a[i_max][j_max] = a[i_max][j_max], a[n//2][n//2]


def main():
    n = int(input('Введите нечетное число, порядок матрицы '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(-10, 10))
        a.append(b)

    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()

    change(a, n)
    print()
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()
main()

