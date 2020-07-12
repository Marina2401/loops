n = int(input('Введите количество членов ряда Фибоначчи '))
i = 0
a = 0
b = 1
while i < n:
    c = a + b
    a = b
    b = c
    i = i + 1
    print(c)