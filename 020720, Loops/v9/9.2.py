#2.Среди чисел 1, 5 10, 16, 23, ... найти первое число, большее n. Условный оператор не использовать.
#Решить задачу используя циклическую конструкцию while.
#НЕ ЗНАЮ, КАК СДЕЛАТЬ БЕЗ IF
n = int(input('введите n '))
i = 0
s = 1
while i < n:
    s = s + 4 + i
    i = i + 1
    if s > n:
        break
print(s)