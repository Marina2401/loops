import random

#добавить баланс = 100
#каждая игра стоит 10, если угадали с первого раза +50, со второго +30, с третьего +20
#если баланса не хватает на игру то выдаем сообщение об этом и завершаем в игру
#статистика игры, кол-во выйгрышей и пройгрышей
#10 стоит игра, сообщение выдавать после игры

def main():
    count = 15
    count_win = 0
    count_game_over = 0
    print(f'У вас есть {count} очков')
    while True:
        computer = random.randint(1, 10)

        #win = False
        for i in range(1, 4):
            user = int(input('Введите число: '))
            if user > computer:
                print('Загаданное число меньше')

            elif user < computer:
                print('Загаданное число больше')

            else:
                #win = True
                if i == 1:
                    count = count + 40
                elif i == 2:
                    count = count + 20
                else:
                    count = count + 10
                count_win += 1
                print(f'Вы угадали!!! Поздравляем! у вас {count} очков!'
                    f'Количество выигрышей: {count_win}, количество проигрышей {count_game_over}')
                break
        else:

            count_game_over = count_game_over + 1
            count = count - 10
            print(f'Попытки закончены. Загаданное число {computer}. у вас {count} очков.'
                  f'Количество выигрышей: {count_win}, количество проигрышей {count_game_over}')
            if count < 10:
                print(f'у Вас {count} очков. На следующую игру не хватит.')
                break


        choose = int(input('1.Продолжить 2.Выход\n'))
        if choose == 2:
            break
main()