#2. Найти сумму и произведение цифр, введенного целого числа.
# Например, если введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).

#Решить задачу используя циклическую конструкцию while.
n = int(input('Введите число n '))
s = 0
p = 1
while n > 0:
    a = n % 10
    s = s + a
    p = p * a
    n = n//10

print(s, p)