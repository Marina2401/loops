#2. Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке
# выбирается
# элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей.
# Вывести на экран новую матрицу.



import random

def mi(a, n, m):
    for i in range(n):
        mi = a[i][0]
        j_mi = 0
        for j in range(m):
            if a[i][j] < mi:
                mi = a[i][j]
                j_mi = j
        if mi % 2 == 0:
            a[i][j_mi] = 0

        else:
            a[i][j_mi] = 1

def main():
    n = int(input('Введите количество строк '))
    m = int(input('Введите количество столбцов '))

    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(random.randint(-10, 10))
        a.append(b)

    for i in range(n):
        for j in range(m):
            print(a[i][j], end='\t')
        print()
    print()

    mi(a, n, m)
    for i in range(n):
        for j in range(m):
            print(a[i][j], end='\t')
        print()
    print()

main()





