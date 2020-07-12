d = int(input('Введите день '))
m = int(input('Введите месяц '))
y = int(input('введите год '))
if 12 >= m >= 1 and y > 0 and 1 <= d <= 31:
    if m==2:
        count_d=28
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        count_d=31
    else:
        count_d=30
    if d <= count_d:
        print('Всё верно ')
    else:
        print('Не совсем верно ')
else:
    print('Неверно ')

