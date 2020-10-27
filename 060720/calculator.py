# coding=utf-8
def calculate(first, second, choose):
    if choose == 1:
        res = first + second
    elif choose == 2:
        res = first - second
    elif choose == 3:
        res = first * second
    elif choose == 4:
        res = first / second
    return res

def input_choice(start, end):
    while True:
        num = int(input())
        if start <= num <= end:
            break
        else:
            print(f'Неверный ввод. Число должно быть от {start} до {end}. Повторите ввод!')
    return num


def main():
    while True:
        print('1.Сумма\n2.Разность\n3.Произведение\n4.Частное\n0.Выход')
        choose = input_choice(0, 4)
        if choose == 0:
            break
        else:
            first = int(input('Введите первое число: '))
            second = int(input('Введите второе число: '))
            res = calculate(first, second, choose)
            print(f'Результат = {res}')

main()