#Вывести сумму четных чисел между заданными числами n и k, если числа натуральные и идут подряд
n = int(input('Введите первое число n '))
k = int(input('Введите второе число k '))
s = 0
flag = False
for i in range(k, n+1):
    if i % 2 == 0 and flag == False:
        s = s + i
    else:
        flag = True
print (s)
