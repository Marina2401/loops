#фигурирует множество значений, выражаемых степенью двойки, то есть чисел вида 2^K, где K – некоторое
# неотрицательное целое число. Назовем такие числа бинарными. Это такие числа как 2, 4, 8, 16, 32 и т.д.
# Действительно, когда речь идет о размере памяти или о разрешении экрана монитора, то мы часто наталкиваемся
# на бинарные числа. Все это связано с принципом хранения информации в памяти ЭВМ.
#Задано целое число N. Требуется определить, является ли оно бинарным.

# непонятно с 1

n = int(input('Введите число n '))
while n % 2 == 0:
    n = n//2
if n != 1:
    print('не является')
else:
    print('является')