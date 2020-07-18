#Требуется вывести произведение n простых первых чисел
import math
def simple(c):
    i = 2
    while i <= math.sqrt(c):
        if c % i == 0:
            return False
        i += 1
    return True

def main():
    n = int(input('Введите количество чисел n '))
    s = 1
    ct = 0
    for k in range(2, 1000000):
        if simple(k):
            a = k
            s = a * s
            ct = ct + 1
            if ct == n:
                print(k,'=', s)
            elif ct < n:
                print(k, end='*')

main()
