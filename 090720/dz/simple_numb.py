#задано 2 положительных натуральных числа. Требуется вывести все простые числа, из которых получатся тоже
# простые числа, если записать их цифры обратно: например, 13 и 31, 17 и  71.
import math
def simple(c):
    i = 2
    while i <= math.sqrt(c):
        if c % i == 0:
            return False
        i = i+1
    return True

def reverse(d):
    res = 0
    while d > 0:
        e = d % 10
        res = res*10+e
        d = d//10
    return res

def main():
    a = int(input('Введите число a '))
    b = int(input('Введите число b '))
    for j in range(a, b+1):
        if simple(j):
            k = reverse(j)
            if simple(k) == True:
                print(j)
main()