#задано 2 положительных натуральных числа. Требуется вывести все простые числа, из которых получатся тоже простые числа, если
#записать их цифры обратно: например, 13 и 31, 17 и  71.
def simple(c):
    i = 2
    while i < c:
        if c % i == 0:
            return False
        i = i+1
    return True

def simple_in_interval(j):
    for j in range(a, b+1):
        if simple(j) == True:
            return True
def main():
    a = int(input('Введите число a '))
    b = int(input('Введите число b '))
    k = simple_in_interval(n)
    if k == True:
        i = 0
        while k > 0:
            c = k % 10
            i = i + 1
            d = 10*c
            d = d + c
        if simple(d) == True:
            print(k)
main()