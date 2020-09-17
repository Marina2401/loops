#Задайте количество членов ряда Фибоначчи и выведите его в ряд

def Fib(d, n):
    a = 0
    b = 1
    i = 0
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
        d.append(c)
    return d
def main():
    n = int(input('Введите количество '))
    d = []
    f = Fib(d, n)
    print(f)

main()




n = int(input('Введите количество членов ряда Фибоначчи '))
i = 0
a = 0
b = 1
while i < n:
    c = a + b
    a = b
    b = c
    i += 1
    print(c)