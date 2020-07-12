n = int(input('Введите число, которое нужно перевести в двоичную систему, и для которого нужно посчитать'
              'количество битов в нём '))
res = 0
a = 1
count = 0
while n != 0:
    b = n % 2
    res = b*a + res
    a = a*10
    if b == 1:
        count = count + 1
    n = n // 2
print(res, count)


