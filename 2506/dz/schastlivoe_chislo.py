def check_happy(a):
    b = a // 100000
    c = a // 10000 % 10
    d = a // 1000 % 10
    e = a // 100 % 10
    f = a // 10 % 10
    g = a % 10
    S1 = d + b + c
    S2 = g + e + f
    if S1 == S2:
        return True
    else:
        return False


def main():
    a = int(input('Введите шестизначное число '))
    check = check_happy(a)
    if check == True:
        print('Это число счастливое! ')
    else:
        print('Увы')

main()