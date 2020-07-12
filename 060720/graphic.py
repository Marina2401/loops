
def func(x):
    return x**3 - 2*x*x + 4

def show_table(a, b, h):
    x = a
    print('x\tf(x)')
    while x <= b:
        f = func(x)
        print(f'{x}\t{f}')
        x += h

def main():
    a = float(input('a = '))
    b = float(input('b = '))
    h = float(input('h = '))
    show_table(a, b, h)

main()