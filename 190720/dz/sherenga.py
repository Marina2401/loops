#На входе невозрастающая последовательность натуральных чисел, означающих рост учеников на физкультуре.
#x - рост Пети. Надо определить его порядковый номер в строю. если есть люди с таким же ростом, то Петя
#стоит после них.
import random
def cr(a, n):
    for i in range(n):
        a.append(random.randint(150, 200))

def pr(a):
    for i in a:
        print(i, end=' ')
    print()


def main():
    n = int(input('Введите количество учеников в классе '))
    a = []
    cr(a, n)
    a.sort(reverse=True)
    pr(a)
    x = int(input('Введите рост ученика в см '))

    for i in range(n):
        if x > a[i]:
            pos = i+1
            break
    else:
        pos = n+1
    print(pos)

    # if x in a:
    #     a.append(x)
    #     a.sort(reverse=True)
    #     pr(a)
    #     print(a.index(x)+2)
    # else:
    #     a.append(x)
    #     a.sort(reverse=True)
    #     pr(a)
    #     print(a.index(x)+1)

main()

