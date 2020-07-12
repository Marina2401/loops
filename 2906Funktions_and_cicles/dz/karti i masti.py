def kart(k):
    if k == 6:
        return 'Шестёрка'
    elif k == 7:
        return 'Семёрка'
    elif k == 8:
        return 'Восьмёрка'
    elif k == 9:
        return 'Девятка'
    elif k == 10:
        return 'Десятка'
    elif k == 11:
        return 'Валет'
    elif k == 12:
        return 'Дама'
    elif k == 13:
        return 'Король'
    else:
        return 'Туз'

def mast(m):
    if m == 1:
        return 'пик'
    elif m == 2:
        return 'черви'
    elif m == 3:
        return 'крести'
    else:
        return 'бубен'

def nazv(k, m):
    l = kart(k)
    n = mast(m)
    res = l+" "+n
    return res

def main():
    k = int(input('Введите цифру достоинства карты (от 6 до 14) '))

    m = int(input('Введите номер масти карты (от 1 до 4) '))
    result = nazv(k, m)
    print(f'Получилась карта "{result}"')
main()



