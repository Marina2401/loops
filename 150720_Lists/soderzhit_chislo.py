#Определить, есть ли число в списке
import random
def gen(a, n):
    for i in range(n):
        a.append(random. randint(1, 100))

def pr(a):
    # for i in range(len(a)):
    #     print(a[i])
    for i in a:
        print(i, end=' ')
    print()

def check(a, b):
    for i in a:
        if i == b:
            return True
    return False

def main():
    n = int(input('внесите количество элементов '))
    a = []
    gen(a, n)
    pr(a)
    b = int(input('введите число '))
        #c = check(a, b)
    if b in a:
        print('Есть')
    else:
        print('нет')
main()