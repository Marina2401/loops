#Произвольным образом вводятся числа.
# Процесс продолжается до тех пор, пока не будет введено число, кратное 3.
# Найти среднее арифметическое введенных чисел (не кратных 3).
#НЕ ЗНАЮ, КАК ВЫВОДИТЬ ПРОСТО ЧИСЛА БЕЗ ЗАДАННОГО КОЛИЧЕСТВА N!!!

i = 0
s = 0
while True:
    a = int(input('введите число '))
    if a % 3 == 0:
        break
    else:
        s = s + a

    i += 1
sr = s/i
print(sr)

