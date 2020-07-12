def y(x):
    return -0.23 * x**2 + x
def table(a, b, h):
    x = a
    print('x\ty(x)')
    while x <= b:
        f = y(x)
        print(f'{x}\t{f}')
        x += h
def main():
    a = int(input('Введите левую координату '))
    b = int(input('Введите правую координату '))
    h = int(input('Введите шаг '))
    table(a, b, h)
main()