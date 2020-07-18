# Требуется вывести n простых чисел больше числа m
def simple(a):
    i = 2
    while i < a:
        if a % i == 0:
            return False
        i += 1
    return True

def main():
    n = int(input('Введите количество простых чисел, которые надо вывести '))
    m = int(input('Введите число, больше которого должны быть эти числа '))
    j = 1
    ct = 0
    while j < 100:
        s = m + j
        if simple(s):
            ct = ct + 1
            if ct <= n:
                print(s)
        j += 1
main()