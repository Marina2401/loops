import random

def fill(a, n, m):
    for i in range(n):
        b = []
        for j in range(m):
            num = random.randint(20000, 90000)
            b.append(num)
        a.append(b)

def print_list(a):
    for row in a:
        for col in row:
            print(col, end='\t')
        print()
    print()
    # for i in range(len(a)):
    #     for j in range(len(a[i])):
    #         print(a[i][j], end='\t')
    #     print()

def max_profit_all(a):
    max = 0
    for row in a:
        for col in row:
            if col > max:
                max = col
    return max

def profit_by_shops(a):
    profits = []
    for row in a:
        sum = 0
        for col in row:
            sum += col
        profits.append(sum)
    return profits

#реализовать функцию нахождения прибылей по месячно

def main():
    a = []
    n = int(input('Кол-во магазинов = '))
    m = int(input('Кол-во месяцев = '))
    fill(a, n, m)
    print_list(a)
    max = max_profit_all(a)
    print(f'Max Profit = {max}')
    profits = profit_by_shops(a)
    print(profits)

main()