chasi = int(input('Введите часы отправления (от 0 до 23) '))
minutes = int(input('Введите минуты отправления (от 0 до 59) '))
vremia_otp = print(f'Время отправления {chasi}:{minutes}')
vremya_vputi_chas = int(input('Введите количество часов в пути (от 00 до 23) '))
vremyia_vputi_minuti = int(input('Введите количество минут в пути (от 00 до 59) '))
dlit_puti = print(f'Длительность пути {vremya_vputi_chas}:{vremyia_vputi_minuti}')
kol_chas = chasi+vremya_vputi_chas
kol_min = minutes+vremyia_vputi_minuti

if kol_min <= 59:
    minprib = kol_min
    if kol_chas <= 23:
        chasprib = kol_chas
        print(f'Время прибытия в тот же день {chasprib}:{minprib}')
    else:
        chasprib = kol_chas % 24
        print(f'Время прибытия на другую дату {chasprib}:{minprib}')
else:
    minprib = kol_min - 60
    if kol_chas < 23:
        chasprib = kol_chas+1
        print(f'Время прибытия в тот же день день {chasprib}:{minprib}')
    else:
        chasprib = (kol_chas+1) % 24
        print(f'Время прибытия на другую дату {chasprib}:{minprib}')