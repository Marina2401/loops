def calc(num):
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    s = a + b + c
    p = a * b * c
    return s, p

def main():
    num = int(input('Введите число: '))
    s, p = calc(num)
    print(s, p)

main()