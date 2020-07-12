import sys

#реализовать функцию для расчета стоимости со скидкой
#если сумма покупки свыше 1000 то скидка 5%, если свыше 2000 то 10%
#печатать правильное склонение рубля (функцию отдельная)
#найти самый дешевый товар

def main():
    count = int(input('Введите кол-во товаров: '))
    i = 0
    total = 0
    max_cost = 0
    min_cost = sys.maxsize

    while i < count:
        cost = int(input(f'Введите стоимость товара {i+1}: '))
        #total = total + cost
        total += cost
        if cost > max_cost:
            max_cost = cost

        if cost < min_cost:
            min_cost = cost
        i += 1
        #total = total + cost
    print(f'Итого = {total} рублей')
    #print(f'Максимальная стоимость = {max_cost}')
    print(f'Минимальная стоимость = {min_cost}')

main()