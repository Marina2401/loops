#1. Найти сумму квадратов всех целых чисел от a до 50 (значение a вводится с клавиатуры; 0 ≤a≤50).
# Решить задачу используя циклическую конструкцию for.

a = int(input('Введите a от 0 до 50: '))
s = 0
for i in range(a, 51):
    s = s + i**2
print(s)