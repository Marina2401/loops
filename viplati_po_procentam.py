S = int(input('Введите необходимую сумму '))
n = int(input('ведите количество лет '))
p = float(input('Введите процент '))
r = p/100

m = (S*r*(1+r)**n)/(12*((1+r)**n-1))
m = round(m,2)
print(f"Месячная выплата = {m}")