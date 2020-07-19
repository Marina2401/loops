#Требуется вывести произведение n простых первых чисел
import math
def simple(c):
    i = 2
    while i <= math.sqrt(c):
        if c % i == 0:
            return False
        i += 1
    return True

def prod(n):
    s = 1
    ct = 0
    k = 2
    while ct < n:
        if simple(k):
            s = k * s
            ct = ct + 1
        k += 1
    return s

def main():
    n = int(input('Введите количество чисел n '))
    p = prod(n)
    print(p)


main()
