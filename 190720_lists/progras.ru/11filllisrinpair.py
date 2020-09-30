# 11*. Заполнить список значениями по парам с обоих концов:
# 1 3 5 7 9 10 8 6 4 2
def cr(a, n):
    for i in range(n):
        a.append(n)

def pr(n):
    for i in range(1, 10, 2):
        print(i, end=' ')
    for j in range(10, 1, -2):
        print(j, end=' ')

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(n)

main()
