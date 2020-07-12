d1 = int(input('Введите день для первой даты '))
m1 = int(input('Введите месяц для первой даты '))
#if m1>12 or m1<1:
    #print('Ошибка ввода месяца')
y1 = int(input('Введите год для первой даты '))
print(f'Первая дата {d1}.{m1}.{y1}')
d2 = int(input('Введите день для второй даты '))
m2 = int(input('Введите месяц для второй даты '))
#if m2>12 or m2<1:
   # print('Ошибка ввода месяца')
y2 = int(input('Введите год для второй даты '))
print('Вторая дата ', d2, m2, y2, sep='.')

if y1 < y2:
    print('yes')
elif y1 == y2 and m1 < m2:
    print('yes')
elif y1 == y2 and m1 == m2 and d1<d2:
    print('yes')
elif y1==y2 and m1==m2 and d1==d2:
    print('даты одинаковые')
else:
    print('no')
