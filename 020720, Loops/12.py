#Найдите количество целых чисел от a до b включительно, которые делятся на 12
a = int(input('Введите a '))
b = int(input('Введите b '))
for i in range(a, b+1):
    if i % 12 == 0:
        print(i, end=' ')
