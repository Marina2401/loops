def kolrub(total):
    c = total % 10
    if 5 <= total % 100 <= 20:
        return 'рублей'
    elif c == 1:
        return 'рубль'
    elif 4 >= c > 1:
        return 'рубля'
    else:
        return 'рублей'

def discount(tsum):
    if 2000 >= tsum > 1000:
        final_cost = tsum*0.95
    elif tsum > 2000:
        final_cost = 0.9*tsum
    else:
        final_cost = tsum
    return final_cost

def main():
    #print(kolrub(211))
    count = int(input('Введите кол-во товаров: '))
    i = 0
    total = 0
    while i < count:
        cost = int(input(f'Введите стоимость товара {i + 1}: '))
            # total = total + cost
        total += cost
        i += 1

    okon = kolrub(total)
    tsum = discount(total)
    print(f'Итого = {tsum} {okon} ')

main()