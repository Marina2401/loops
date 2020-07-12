def count_money(n1, n2, n3):
    res = n1 * 10 + n2 * 50 + n3 * 100
    return res


def main():
    a = int(input('Кол-во монет по 10: '))
    b = int(input('Кол-во монет по 50: '))
    c = int(input('Кол-во монет по 100: '))
    money = count_money(a, b, c)
    print(f'Сумма = {money}')


main()