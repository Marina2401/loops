# найти количество простых чисел до введенного числа, включая его, если оно простое.
import math
def simple(c):
    i = 2
    while i <= math.sqrt(c):
        if c % i == 0:
            return False
        i += 1
    return True

def quant(d):
    count = 0
    for j in range(2, d+1):
        if simple(d):
            count = count + 1
    return j, count

def main():
    n = int(input('Введите число n '))
    e = quant(n)
    g = simple(n)


    m = n - e #количество чисел больше н, которые надо добавить
    for k in range(1, m):
        if simple(k):
            print(k)
main()