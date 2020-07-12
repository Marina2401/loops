#Натуральное десятичное N - значное число называется числом Армстронга, если сумма его цифр, возведенных в степень
# N, равна самому числу.
#Примеры: 153 = 1^3 + 5^3 + 3^3 ; 1634 = 1^4 + 6^4 + 3^4 + 4^4.
#Найти все числа Армстронга для 1<=N<=9.

import math
def count_digit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def check_armstrong(n):
    st = count_digit(n)
    sum = 0
    m = n
    while n > 0:
        a = n % 10
        sum = sum + pow(a, st)
        n = n//10
    if sum == m:
        return True
    else:
        return False

def main():
    n = int(input('Введите число '))
    check = check_armstrong(n)
    if check == True:
        print('yes')
    else:
        print('no')
main()

