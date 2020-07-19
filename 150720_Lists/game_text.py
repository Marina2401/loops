#написать игру, текстовый квест. в котором игроку предстоит управлять существом.
# Управление осуществляется в консоли при помощи цифр.
# То есть на каждом шаге игроку выдаются все его параметры и задается вопрос, что он собирается делать с
# вариантами ответа, пронумерованными цифрами.

def night(d, z, u, v):
    d = d - 2
    z = z - 20
    u = u - 2
    v = v - 5
    return d, z, u, v
def input_choice(start, end):
    while True:
        num = int(input())
        if start <= num <= end:
            break
        else:
            print(f'Неверный ввод. Число должно быть от {start} до {end}. Повторите ввод!')
    return num

def day(d, z, u, v):
    print(f'Ваши параметры: длина норы: {d}, здоровье: {z}, уважение: {u}, вес: {v}')
    print('Что вы собираетесь делать? ')
    print('1.Копать нору\n2.Поесь траву\n3.Пойти подраться\n4.Спать весь день')
    choose = input_choice(1, 4)
    if choose == 1:
        print('5.Интенсивно?\n6.Или лениво?')
        choose = input_choice(5, 6)
        if choose == 5:
            d = d + 5
            z = z - 30
        else:
            d = d + 2
            z = z - 10
    elif choose == 2:
        print('7.Жухлой?\n8.Или зелёной?')
        choose = input_choice(7, 8)
        if choose == 7:
            v = v + 5
            z = z + 10
        else:
            if u <= 30:
                z = z - 30
            else:
                z = z + 30
                v = v + 30

    elif choose == 3:
        print('9.со слабым существом?\n10.со средним существом?\n')
        choose = input_choice(9, 11)
        if choose == 9:
            v = v + 5
            z = z + 10
        else:
            if u <= 30:
                z = z - 30
            else:
                z = z + 30
                v = v + 30

    elif choose == 4:
        d = d - 2
        z = z - 20
        u = u - 2
        v = v - 5

    return d, z, u, v

def main():
    d = 10
    z = 100
    u = 20
    v = 30
    print(f'Ваши параметры: длина норы: {d}, здоровье: {z}, уважение: {u}, вес: {v}')
    while u <= 100 and d > 0 and z > 0 and v > 0:
        print('наступил день. хорошо, что вы живы')
        d, z, u, v = day(d,z,u,v)
        print('Наступила ночь')
        d, z, u, v = night(d, z, u, v)
        print(f'Ночь прошла, ваши параметры: длина норы: {d}, здоровье: {z}, уважение: {u}, вес: {v}')

    if u > 100:
        print('You win')
    else:
        print('Один из ваших параметров не позволяет продолжать игру')

main()

