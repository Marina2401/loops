import math
a = int(input('Введите коэффициент a '))
b = int(input('Введите коэффициент b '))
c = int(input('Введите коэффициент c '))
D = b*b-4*a*c

if a == 0:
    if b == 0:
        if c == 0:
            print('Уравнение такое: 0*x^2+0*x+0 = 0')
            print('Решение - любое число')
        else:
            print(f'Уравнение такое: 0*x^2+0*x+{c}=0')
            print('Если a и b равны 0, то c обязательно должно быть равно 0')
    else:
        print(f'Уравнение такое: {b}*x+{c}=0')
        x = -c/b
        print(f'Корень {x}')
else:
    print(f'Уравнение такое: {a}*x^2+{b}*x+{c}=0')
    print('Дискриминант ', D)
    if D < 0:
        print('Решений нет')
    elif D==0:
        x = -b/(2*a)
        print(f'Решение х = {x}')
    else:
        x1 = (-b+math.sqrt(D))/(2*a)
        x1 = round(x1,3)
        x2 = (-b - math.sqrt(D))/(2*a)
        x2 = round(x2,3)
        print('Корни уравнения: ', x1, x2)