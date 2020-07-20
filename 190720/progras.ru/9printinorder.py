# 9. Заполнить список значениями по-порядку, начиная с 1

def cr(a, n):
    for i in range(n):
        a.append(n)

def pr(n):
    for i in range(1, n+1):
        print(i, end=' ')


def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(n)

main()
