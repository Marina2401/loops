#Дано целое число больше 0, являющееся степенью двойки (два в некоторой степени k равно этому числу).
# Найти показатели степени k. Решить задачу используя циклическую конструкцию while.
import math
n = int(input('Введите число N = '))
i = 0
m = n//2
while m >= 1:
    m = m//2
    i = i+1
print(i)

