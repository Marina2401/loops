import math
def check(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    n = int(input('Введите число '))
    c = check(n)
    if c == True:
        print('Простое')
    else:
        print('Составное')

main()