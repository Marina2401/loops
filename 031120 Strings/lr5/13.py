#Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки.
# Вывести на экран все символы, расположенные внутри этих скобок.
s = input('Введите строку \n')
c = s.find('(')+1
d = s.find(')')
e = s[c:d]
if not e:
    print('нет символов внутри скобок')
else:
    print(e)