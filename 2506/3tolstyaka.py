M1 = int(input('Введите вес первого человека '))
M2 = int(input('Введите вес второго человека '))
M3 = int(input('Введите вес третьего человека '))

if 94 < M1 < 727 and 94 < M2 < 727 and 94 < M3 < 727:
    if M1>=M2 and M1>=M3:
        max = M1
    elif M2>=M1 and M2>=M3:
        max = M2
    else:
        max = M3
    print('Самый тяжёлый ', max)
else:
    print('Не бывает такого веса у толстяков!')