# coding=utf-8
#Для делимости числа на 11 необходимо, чтобы разность между суммой цифр, стоящих на четных местах,
# и суммой цифр, стоящих на нечетных местах, делилась на 11.
#Требуется написать программу, которая проверит делимость заданного числа на 11.

def check_11(n):
    sum1 = 0
    sum2 = 0
    i = 0
    while n > 0:
        a = n % 10
        if i % 2 == 0:
            sum1 = sum1 + a
        else:
            sum2 = sum2 + a
        n = n // 10
        i = i + 1

    razn = (sum2 - sum1) % 11
    if razn == 0:
        return True
    else:
        return False

def main():
    n = int(input('Введите число '))
    if check_11(n) == True:
       print('OK')
    else:
        print('No')
main()




