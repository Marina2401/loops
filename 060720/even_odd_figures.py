#Требуется вывести количество четных и нечетных цифр числа, а так же сами цифры
n = int(input('Введите число '))
count1 = 0
count2 = 0
while n > 0:
    b = n % 10
    c = b % 2
    if c == 0:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
    n = n // 10
print(f'Четных цифр {count1},  нечетных {count2}')
