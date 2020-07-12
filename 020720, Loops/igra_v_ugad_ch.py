#Выводить сообщение попытки закончены вы проиграли загаданное число такое то
#возможность продолжить игру (заново начать)
#добавить баланс

def main():
    while True:
        computer = random.randint(1, 10)
        for i in range(3):
            user = int(input('Введите число: '))
            if user > computer:
                print('Загаданное число меньше')
            elif user < computer:
                print('Загаданное число больше')
            else:
                print('Вы угадали!!!')
                break


main()