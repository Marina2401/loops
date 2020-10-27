# coding=utf-8
t = float(input('Введите время в минутах '))
S = float(input('Введите расстояние в километрах '))
v = (S*1000)/(t*60)
v = round(v, 2)
print(f"Скорость в м/с = {v}")
