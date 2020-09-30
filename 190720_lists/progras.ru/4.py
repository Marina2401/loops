#4. Удалить первые три элемента
import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(0, 1000))

def pr(a):
    for i in a:
        print(i, end=' ')

def dl(a):
    a = a[3:]
    return a

def main():
    n = int(input('Введите количество элементов '))
    a = []
    cr(a, n)
    pr(a)
    print()
    d = dl(a)
    print(f'{d}')

main()