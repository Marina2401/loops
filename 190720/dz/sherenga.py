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


def check(a, n, x):
   i = 0
   while i < n:
       if x == a[i]:
           if a[i] == a[i+1]:
               return i+2
           else:
               return i+1
       i += 1


def main():
    n = int(input('Введите количество учеников в классе '))
    a = []
    cr(a, n)
    a.sort(reverse=True)
    pr(a)
    print()
    x = int(input('Введите рост ученика в см '))
    c = check(a, n, x)
    print(c)

main()

